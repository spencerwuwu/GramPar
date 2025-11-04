const fs = require('fs');
const path = require('path');
const simpleParser = require('mailparser').simpleParser;


const args = process.argv.slice(2);

if (args.length !== 4 || args[0] !== '-i' || args[2] !== '-o') {
    console.log('Usage: node extractAttachments.js -i <input_mail_file> -o <output_directory>');
    process.exit(1);
}

const inputFile = args[1];
const outputDir = args[3];

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
}

// Prepare subdirectories
const filenamesDir = path.join(outputDir, 'filenames');
const contentDir = path.join(outputDir, 'content');
fs.mkdirSync(filenamesDir, { recursive: true });
fs.mkdirSync(contentDir, { recursive: true });


fs.readFile(inputFile, (err, data) => {
    if (err) {
        console.error('Error reading input file:', err);
        process.exit(1);
    }

    simpleParser(data, (err, mail) => {
        if (err) {
            console.error('Error parsing mail:', err);
            process.exit(1);
        }

        let attCnt = 0;
        mail.attachments.forEach((attachment) => {
            const serializedName = `attachment_${String(attCnt).padStart(3, '0')}`;
            const originalFilename = attachment.filename || '';

            // Save original filename text
            const filenamePath = path.join(filenamesDir, serializedName);
            fs.writeFileSync(filenamePath, originalFilename, { encoding: 'utf8' });

            // Save attachment content
            const contentPath = path.join(contentDir, serializedName);
            fs.writeFileSync(contentPath, attachment.content);

            attCnt++;
        });
    });
});
