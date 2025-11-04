using System;
using System.IO;
using System.Linq;
using MimeKit;

class Program
{
    static void Main(string[] args)
    {
        string? inputFilePath = null;
        string? outputDirectory = null;

        for (int i = 0; i < args.Length; i++)
        {
            if (args[i] == "-i" && i + 1 < args.Length)
            {
                inputFilePath = args[i + 1];
            }
            else if (args[i] == "-o" && i + 1 < args.Length)
            {
                outputDirectory = args[i + 1];
            }
        }

        if (string.IsNullOrEmpty(inputFilePath) || string.IsNullOrEmpty(outputDirectory))
        {
            Console.WriteLine("Usage: -i <inputfile> -o <outputdirectory>");
            return;
        }

        if (!Directory.Exists(outputDirectory))
        {
            Directory.CreateDirectory(outputDirectory);
        }

        try
        {
            var filenamesDir = Path.Combine(outputDirectory, "filenames");
            var contentDir = Path.Combine(outputDirectory, "content");
            Directory.CreateDirectory(filenamesDir);
            Directory.CreateDirectory(contentDir);
            
            var message = MimeMessage.Load(inputFilePath);

            var attCnt = 0;
            foreach (var attachment in message.Attachments)
            {
                string originalFilename = attachment.ContentDisposition?.FileName
                                           ?? attachment.ContentType.Name
                                           ?? "attachment";

                string serializedName = $"attachment_{attCnt:D3}";

                // Save original filename to filenames directory
                var filenamePath = Path.Combine(filenamesDir, serializedName);
                File.WriteAllText(filenamePath, originalFilename);

                // Save attachment content to content directory
                var contentPath = Path.Combine(contentDir, serializedName);
                using (var stream = File.Create(contentPath))
                {
                    if (attachment is MimePart part)
                    {
                        part.Content.DecodeTo(stream);
                    }
                    else if (attachment is MessagePart messagePart)
                    {
                        // Handle attached message (.eml inside email)
                        messagePart.Message.WriteTo(stream);
                    }
                    Console.WriteLine($"Attachment saved: {contentPath}");
                }

                attCnt++;

            }

            //Console.WriteLine("Attachments extracted successfully.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
