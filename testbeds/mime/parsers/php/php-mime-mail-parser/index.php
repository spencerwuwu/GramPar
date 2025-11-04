<?php

require_once __DIR__.'/vendor/autoload.php';
//use eXorus\PhpMimeMailParser\Parser;


$options = getopt("i:o:");

if (!isset($options['i']) || !isset($options['o'])) {
    echo "Usage: php script.php -i <input_file> -o <output_file>\n";
    exit(1);
}

$emailFilePath = $options['i'];
//$attach_dir = $options['o'];
$outputDir = $options['o'];


if (!file_exists($emailFilePath)) {
    echo "Error: Input file does not exist.\n";
    exit(1);
}


//$Parser = new Parser();
$Parser = new PhpMimeMailParser\Parser();
$Parser->setPath($emailFilePath); 

$attCnt = 0;

//$to = $Parser->getHeader('to');
//var_dump($to);
//$from = $Parser->getHeader('from');
//$subject = $Parser->getHeader('subject');
//
//$text = $Parser->getMessageBody('text');
//$html = $Parser->getMessageBody('html');
//$html_embedded = $Parser->getMessageBody('html', TRUE);


//if (!file_exists($attach_dir)) {
//    mkdir($attach_dir, 0777, true);
//}

// Create output subdirectories
$filenamesDir = $outputDir . DIRECTORY_SEPARATOR . "filenames";
$contentDir   = $outputDir . DIRECTORY_SEPARATOR . "content";
if (!is_dir($filenamesDir)) mkdir($filenamesDir, 0777, true);
if (!is_dir($contentDir)) mkdir($contentDir, 0777, true);


$attachments = $Parser->getAttachments();
$attCnt = 0;

//$Parser->saveAttachments($attach_dir, TRUE, $Parser::ATTACHMENT_DUPLICATE_SUFFIX);
foreach ($attachments as $attachment) {
    $serializedName = sprintf("attachment_%03d", $attCnt);
    $originalFilename = $attachment->getFilename() ?? "";

    // Save original filename to filenames/
    $filenamePath = $filenamesDir . DIRECTORY_SEPARATOR . $serializedName;
    file_put_contents($filenamePath, $originalFilename);

    // Save content to content/
    $contentPath = $contentDir . DIRECTORY_SEPARATOR . $serializedName;
    file_put_contents($contentPath, $attachment->getContent());

    $attCnt++;
}
?>
