import os
import re

# Function to create the output directory if it doesn't exist
def ensure_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Get the path to scan from the user
scan_path = input("Enter the path to scan: ")
if not os.path.isdir(scan_path):
    print("Error: The specified path does not exist or is not a directory.")
    exit(1)

# Get the output directory from the user
default_output_dir = "../Scan_Results/Grep"
output_dir = input(f"Enter the output directory (default: {default_output_dir}): ") or default_output_dir
ensure_dir_exists(output_dir)

# Define file extensions to include
file_extensions = ('.java', '.ts', '.clj', '.json', '.html', '.htm', '.sql', '.yaml', '.yml', '.pom', '.xml', '.sh')

# Define the search patterns and their corresponding output files
patterns = {
    "debug": os.path.join(output_dir, "debug1.txt"),
    "version": os.path.join(output_dir, "version.txt"),
    "logger": os.path.join(output_dir, "logger.txt"),
    "base64": os.path.join(output_dir, "base64.txt"),
    "RSA": os.path.join(output_dir, "RSA.txt"),
    "session": os.path.join(output_dir, "session.txt"),
    "header": os.path.join(output_dir, "header.txt"),
    "Header": os.path.join(output_dir, "Header.txt"),
    "DES": os.path.join(output_dir, "des.txt"),
    "RC2": os.path.join(output_dir, "rc2.txt"),
    "DC4": os.path.join(output_dir, "dc4.txt"),
    "cookie": os.path.join(output_dir, "cookie.txt"),
    "password": os.path.join(output_dir, "password.txt"),
    "userPassword": os.path.join(output_dir, "userpassword.txt"),
    "httponly": os.path.join(output_dir, "httponly.txt"),
    "secure flag": os.path.join(output_dir, "secureflag.txt"),
    "SHA-1": os.path.join(output_dir, "Sha1.txt"),
    "stacktrace": os.path.join(output_dir, "stacktrace.txt"),
    "e.printstacktrace": os.path.join(output_dir, "printstacktrace.txt"),
    "log.": os.path.join(output_dir, "log.txt"),
    "execute();": os.path.join(output_dir, "execute.txt"),
    "exec(=": os.path.join(output_dir, "exec.txt"),
    "query(.": os.path.join(output_dir, "query.txt"),
    "$_GET": os.path.join(output_dir, "Find_user_supplied_input.txt"),
    "http://": os.path.join(output_dir, "http.txt"),
    "ftp://": os.path.join(output_dir, "ftp.txt"),
    "file://": os.path.join(output_dir, "file.txt"),
    "(eval|assert|preg_replace()": os.path.join(output_dir, "PHP_functions.txt"),
    "(mcrypt|openssl|mhash|random|crack_)": os.path.join(output_dir, "Crypto_operations.txt"),
    "(\$|->)?(\[)?(user|pass|username|password)(\])?\s=\s\".\"": os.path.join(output_dir, "Hardcoded_creds.txt"),
}

# Function to scan the specified path for a given pattern
def scan_for_pattern(pattern, output_file):
    pattern_escaped = re.escape(pattern)  # Escape special characters to avoid regex errors
    with open(output_file, 'w') as out_f:
        # Traverse the directory and find files with specified extensions
        for root, _, files in os.walk(scan_path):
            for file in files:
                if file.endswith(file_extensions):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', errors='ignore') as f:
                        # Search for the escaped pattern in the file
                        for line_num, line in enumerate(f, 1):
                            if re.search(pattern_escaped, line):
                                out_f.write(f"{file_path}:{line_num}:{line}")

# Scan for each pattern and write the results to the corresponding file
for pattern, output_file in patterns.items():
    print(f"Scanning for '{pattern}' in '{scan_path}'...")
    scan_for_pattern(pattern, output_file)

print("Scanning completed.")
