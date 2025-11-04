import argparse
from mailparser import parse_from_bytes
import os

def extract_attachments(input_file, output_dir):
    # Ensure output dirs exist
    filenames_dir = os.path.join(output_dir, "filenames")
    content_dir = os.path.join(output_dir, "content")
    os.makedirs(filenames_dir, exist_ok=True)
    os.makedirs(content_dir, exist_ok=True)

    # Read and parse the MIME email
    with open(input_file, "rb") as fd:
        mail = parse_from_bytes(fd.read())

    attachments = mail.attachments
    att_cnt = 0
    for attachment in attachments:
        original_filename = str(attachment.get("filename", ""))

        # Store the original filename in filenames_dir
        serialized_filename = f"attachment_{att_cnt:03d}"
        # Save original filename to filenames directory
        filename_file = os.path.join(filenames_dir, f"{serialized_filename}")
        with open(filename_file, 'w', encoding='utf-8') as f:
            f.write(original_filename)

        # Store the attachment content in contents_dir
        # Save content to content directory with serialized name
        content_file = os.path.join(content_dir, serialized_filename)
        payload = attachment.get("payload", b"")

        if isinstance(payload, bytes):
            with open(content_file, "wb") as f:
                f.write(payload)
        elif isinstance(payload, str):
            with open(content_file, "w", encoding="utf-8", errors="ignore") as f:
                f.write(payload)
        else:
            with open(content_file, "wb") as f:
                f.write(str(payload).encode("latin-1", errors="ignore"))
        att_cnt += 1


def main():
    parser = argparse.ArgumentParser(description='Extract attachments from email file')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the input email file')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path to the output directory for attachments')
    args = parser.parse_args()

    extract_attachments(args.input, args.output)
    #print("Attachments extracted successfully!")

if __name__ == "__main__":
    main()
