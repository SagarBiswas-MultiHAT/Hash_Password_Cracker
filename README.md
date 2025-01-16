
---

# Hash Password Cracker

Easily crack MD5-hashed passwords using a dictionary attack. This tool demonstrates the importance of strong password security and helps illustrate the vulnerabilities of weak hashing algorithms.

Welcome to the **Hash Password Cracker**, a Python tool designed to crack MD5-hashed passwords using a dictionary attack. This script is intended for educational purposes, showcasing how easily weak passwords can be cracked when proper security measures are not followed.

## Overview

The **Hash Password Cracker** reads a list of potential passwords from a file, hashes each one using MD5, and compares the result to the provided hash. MD5 (Message-Digest Algorithm 5) is a widely used cryptographic hash function that produces a 128-bit hash value. While once considered secure, MD5 is now deemed insecure due to its vulnerabilities to collision and brute-force attacks. This tool demonstrates the importance of using stronger hashing algorithms, as weak passwords hashed with MD5 can often be cracked quickly using dictionary attacks.

The **Hash Password Cracker** reads a list of potential passwords from a file, hashes each one using MD5, and compares the result to the provided hash. If a match is found, the original password is displayed.

## Features
- Simple and intuitive interface
- Dictionary attack to find matching passwords
- Error handling for missing files and incorrect input

## Requirements

- **Python 3.x**

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## Usage

### Running the Script

To run the script, follow these steps:

1. Clone the repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the following command:

   ```bash
   python3 password_cracker.py
   ```

### Input Prompts

- **Hashed Password**: Enter the MD5 hash of the password you want to crack.
- **Password File Path**: Provide the full path to the file containing potential passwords.

### Example

```bash
************** PASSWORD CRACKER ******************

Enter the hashed password (MD5 Hash): 5f4dcc3b5aa765d61d8327deb882cf99

Enter passwords filename including path (e.g., /root/home/): /path/to/passwords.txt

Password found: password

***************** Thank you **********************
```

If the password is found, it will be displayed. Otherwise, you will be notified that the password was not found in the file.

## Code Explanation

### Main Script

- **Banner Display**: The script starts by displaying a welcoming banner using text formatting.
- **User Prompts**: It prompts the user for two pieces of information:
  - **Hashed Password**: The MD5 hash of the password you want to crack.
  - **Password File Path**: The full path to a file containing potential password guesses.
- **File Reading and Hashing**:
  - The script opens the specified file and reads it line by line.
  - Each line is stripped of extra whitespace, and the word is hashed using MD5.
  - The hashed word is then compared to the input hash.
- **Match Found**: If a match is found, the original password is displayed, indicating that the hash corresponds to that password.

### Error Handling

- **File Not Found**: If the specified file does not exist or the path is incorrect, the script catches this error and displays an appropriate message.
- **Input Validation**: Ensures that the user inputs are valid and properly formatted to avoid common errors.

This breakdown helps users understand how the script works and the steps it takes to crack an MD5-hashed password.

### Main Script

- The script starts by displaying a banner.
- It prompts the user for the MD5 hash and the path to the password file.
- It reads the file line by line, hashes each word, and compares it to the input hash.
- If a match is found, it prints the corresponding password.

### Error Handling

- **File Not Found**: If the specified file does not exist, an error message is displayed.
- **Invalid Input**: The script ensures that inputs are properly sanitized and validated.

## Contributing

Contributions are welcome! If you have suggestions for new features or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. This license permits anyone to use, modify, and distribute the software with minimal restrictions, ensuring flexibility for open-source development. See the [LICENSE](LICENSE) file for details.

---

**Note**: This script is intended for educational purposes only. Please use it responsibly.

---
