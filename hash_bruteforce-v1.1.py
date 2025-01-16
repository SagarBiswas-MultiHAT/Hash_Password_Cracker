import hashlib

print("\n************** PASSWORD CRACKER ******************")

# Input the hashed password and password file path
input_hash = input("\nEnter the hashed password (MD5 Hash): ")
pass_file_path = input("\nEnter passwords filename including path (e.g., /root/home/): ")

try:
    with open(pass_file_path, 'r') as pass_file:
        # Iterate over each word in the file
        for word in pass_file:
            # Clean the word and hash it
            hash_word = hashlib.md5(word.strip().encode('utf-8')).hexdigest()
            
            if hash_word == input_hash:
                print(f"Password found: {word.strip()}")
                break
        else:
            print(f"Password not found in the file: {pass_file_path}")
except FileNotFoundError:
    print(f"Error: {pass_file_path} not found. Please provide the correct file path.")

print("\n***************** Thank you **********************")
