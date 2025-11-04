package org.example;

import org.apache.commons.mail.Email;
import org.apache.commons.mail.EmailAttachment;
import org.apache.commons.mail.EmailException;
import org.apache.commons.mail.MultiPartEmail;
import org.apache.commons.mail.util.MimeMessageParser;
import org.apache.commons.mail.util.MimeMessageUtils;
import java.util.concurrent.atomic.AtomicInteger;

import javax.mail.MessagingException;
import javax.mail.internet.MimeMessage;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        String inputFile = null;
        String outputFolder = null;

        for (int i = 0; i < args.length; i++) {
            if (args[i].equals("-i") && i + 1 < args.length) {
                inputFile = args[i + 1];
            } else if (args[i].equals("-o") && i + 1 < args.length) {
                outputFolder = args[i + 1];
            }
        }

        if (inputFile == null || outputFolder == null) {
            System.out.println("Usage: java EmailAttachmentExtractor -i <inputFile> -o <outputFolder>");
            return;
        }

        File inputEmail = new File(inputFile);
        if (!inputEmail.exists()) {
            System.out.println("Input email file does not exist.");
            return;
        }

        try {
            MimeMessage mimeMessage = MimeMessageUtils.createMimeMessage(null, inputEmail);
            MimeMessageParser parser = new MimeMessageParser(mimeMessage).parse();

            // Create subdirectories
            File filenamesDir = new File(outputFolder, "filenames");
            File contentDir = new File(outputFolder, "content");
            filenamesDir.mkdirs();
            contentDir.mkdirs();

            AtomicInteger index = new AtomicInteger();
            parser.getAttachmentList().forEach(attachment -> {
                int idx = index.getAndIncrement();
                String serializedName = String.format("attachment_%03d", idx);

                try {
                    // Save original filename in filenames/ directory
                    File filenameFile = new File(filenamesDir, serializedName);
                    try (Writer writer = new OutputStreamWriter(new FileOutputStream(filenameFile), "UTF-8")) {
                        writer.write(attachment.getName() != null ? attachment.getName() : "");
                    }

                    // Save content in content/ directory
                    File contentFile = new File(contentDir, serializedName);
                    try (InputStream in = attachment.getInputStream();
                         OutputStream out = new FileOutputStream(contentFile)) {
                        byte[] buf = new byte[8192];
                        int length;
                        while ((length = in.read(buf)) != -1) {
                            out.write(buf, 0, length);
                        }
                    }

                } catch (IOException e) {
                    e.printStackTrace();
                }
            });

            //System.out.println("Attachments extracted successfully.");
        } catch (IOException | MessagingException e) {
            e.printStackTrace();
        }
    }
}
