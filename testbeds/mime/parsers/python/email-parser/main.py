import argparse
import os
import sys
import email
import re

def save_attachments(input_file, output_dir, verbose=False):
    # Create main output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create subdirectories for filenames and content
    filenames_dir = os.path.join(output_dir, "filenames")
    content_dir = os.path.join(output_dir, "content")
    
    if not os.path.exists(filenames_dir):
        os.makedirs(filenames_dir)
    if not os.path.exists(content_dir):
        os.makedirs(content_dir)

    with open(input_file, 'rb') as f:
        msg = email.message_from_binary_file(f)

    # Traverse all parts of the email
    att_cnt = 0
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if verbose:
            print(list(part.raw_items()))
            print("_"*30)

        if part.get_content_disposition() == "attachment":
            if verbose:
                print('++ ATT: Content-Type: {} '.format(part))

            # Get original filename
            original_filename = part.get_filename()
            if original_filename is None:
                original_filename = ""
            
            # Create serialized filename for content
            serialized_filename = f"attachment_{att_cnt:03d}"
            
            # Save original filename to filenames directory (without .txt extension)
            filename_file = os.path.join(filenames_dir, serialized_filename)
            with open(filename_file, 'w', encoding='utf-8') as f:
                f.write(original_filename)
            
            # Save content to content directory with serialized name
            content_file = os.path.join(content_dir, serialized_filename)

            # Save the original un-decoded payload
            #content = part.get_payload(decode=False)
            content = part.get_payload(decode=True)

            if isinstance(content, bytes):
                with open(content_file, 'wb') as f:
                    f.write(content)
            elif isinstance(content, str):
                with open(content_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                with open(content_file, 'wb') as f:
                    f.write(content.encode(encoding='latin-1', errors='ignore'))
                
            if verbose:
                print(f'Saved filename: {original_filename} -> {filename_file}')
                print(f'Saved content: {content_file}')
                
            att_cnt += 1
        else:
            if verbose:
                print('xx NAT: Content-Type: {}'.format(part))


def main():
    parser = argparse.ArgumentParser(description='Extract attachments from an email file')
    parser.add_argument('-i', '--input', help='Input email file path', required=True)
    parser.add_argument('-o', '--output', help='Output directory for attachments', required=True)
    args = parser.parse_args()

    input_file = args.input
    output_dir = args.output

    if not os.path.isfile(input_file):
        print(f'Error: Input file "{input_file}" does not exist.')
        sys.exit(1)

    save_attachments(input_file, output_dir, verbose=False)

if __name__ == "__main__":
    main()
