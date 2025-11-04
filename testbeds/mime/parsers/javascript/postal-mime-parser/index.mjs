import fs from 'fs';
import path from 'path';
import PostalMime from 'postal-mime';

if (process.argv.length < 4) {
    console.error('Usage: node parse_mail.js <input_email_file> <output_dir>');
    process.exit(1);
}

const emailFilePath = process.argv[2];
const outputDir = process.argv[3];

if (!fs.existsSync(emailFilePath)) {
    console.error(`Error: file ${emailFilePath} not found`);
    process.exit(1);
}

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

// Prepare subdirectories
const filenamesDir = path.join(outputDir, 'filenames');
const contentDir = path.join(outputDir, 'content');
fs.mkdirSync(filenamesDir, { recursive: true });
fs.mkdirSync(contentDir, { recursive: true });

const rawEmailBuffer = fs.readFileSync(emailFilePath);

const parser = new PostalMime({
        //attachmentEncoding: "utf8",     
        //attachmentEncoding: 'base64',     
        attachmentEncoding: 'arraybuffer',     
  });

try {
    // NOTE: tweak decode or not
    const email = await parser.parse(rawEmailBuffer);

    //console.log('From:', email.from?.address || '');
    //console.log('To:', email.to?.map(t => t.address).join(', ') || '');
    //console.log('Subject:', email.subject || '');
    //console.log('Text body:', email.text || '');
    //console.log('HTML body:', email.html || '');

    let attCnt = 0;
    for (const attachment of email.attachments) {
        const serializedName = `attachment_${String(attCnt).padStart(3, '0')}`;
        const originalFilename = attachment.filename || '';
        //console.log('Attachment filename:', attachment.filename);

        // Save original filename text
        const filenamePath = path.join(filenamesDir, serializedName);
        fs.writeFileSync(filenamePath, originalFilename, { encoding: 'utf8' });

        const contentPath = path.join(contentDir, serializedName);
        console.log(attachment.content);
        console.log(typeof attachment.content);
        // FIX: Convert ArrayBuffer to Node.js Buffer
        const nodeBuffer = Buffer.from( attachment.content);
        fs.writeFileSync(contentPath, nodeBuffer);

        attCnt++;
    }
} catch (err) {
    console.error('Error processing MIME file:', err);
    process.exit(1);
}

