import re # Used for regular expressions

def validate_email(email):
    # Simple regex for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def process_emails(file_path):
    # list variables for storing the emails that are valid and invalid
    valid_emails = []
    invalid_emails = []

    # Use a try catch block to make sure the file exists 
    try:
        # Read each line in the file and validate the email
        with open(file_path, 'r') as file:
            for line in file:
                email = line.strip()
                if validate_email(email):
                    valid_emails.append(email)
                else:
                    invalid_emails.append(email)
        # Write a text file with the valid emails
        with open('valid_emails.txt', 'w') as valid_file:
            for email in valid_emails:
                valid_file.write(email + '\n')
        # Write a text file with the invalid emails
        with open('invalid_emails.txt', 'w') as invalid_file:
            for email in invalid_emails:
                invalid_file.write(email + '\n')
        
        # Print the number of each type of email found in the file
        print(f"Valid emails: {len(valid_emails)}")
        print(f"Invalid emails: {len(invalid_emails)}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    file_path = input("Enter the path to your email list file: ")
    process_emails(file_path)

