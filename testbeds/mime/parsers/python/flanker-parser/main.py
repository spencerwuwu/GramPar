import argparse
import os
from flanker import mime

def extract_attachments(email_file, output_dir, verbose=False):
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
    
    with open(email_file, 'rb') as f:
        msg = mime.from_string(f.read())
    
    if verbose:
        print("++ Headers:", msg.headers)
    
    att_cnt = 0
    for part in msg.walk(with_self=True):
        if "multipart" in str(part.content_type):
            continue
        if part.is_attachment():
            if verbose:
                print('++ ATT: Content-Type: {} Body: {}'.format(part, part.body))
            
            # Get original filename
            original_filename = part.detected_file_name
            if not original_filename:
                original_filename = ""
            
            # Create serialized filename for content
            serialized_filename = f"attachment_{att_cnt:03d}"
            
            # Save original filename to filenames directory
            filename_file = os.path.join(filenames_dir, f"{serialized_filename}")
            with open(filename_file, 'w', encoding='utf-8') as f:
                f.write(original_filename)
            
            # Save content to content directory with serialized name
            content_file = os.path.join(content_dir, serialized_filename)
            
            content = part.body
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract attachments from an email file.")
    parser.add_argument("-i", "--input", required=True, help="Input email file path.")
    parser.add_argument("-o", "--output", required=True, help="Output directory to save attachments.")
    args = parser.parse_args()

    extract_attachments(args.input, args.output, verbose=False)
