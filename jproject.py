import string

# Function to encode a message using the Caesar Cipher
def encode(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encoded_message += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encoded_message += char
    return encoded_message

# Function to decode a message using the Caesar Cipher
def decode(encoded_message, shift):
    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decoded_message += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decoded_message += char
    return decoded_message

# Function to validate user input
def validate_input(input_string, input_type):
    if input_type == 'int':
        try:
            return int(input_string)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return None
    elif input_type == 'str':
        if input_string.strip():
            return input_string
        else:
            print("Invalid input. Please enter a non-empty string.")
            return None

# Function to display the main menu
def display_menu():
    print("\nMenu:")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. View Examples")
    print("4. Quit")

# Function to get the shift value from the user
def get_shift_value():
    while True:
        try:
            shift_input = input("Enter the shift value: ")
            shift = int(shift_input)
            return shift
        except ValueError:
            print("Error: Shift value must be a valid integer. Please try again.")

# Function to handle encoding process
def process_encoding(shift):
    while True:
        message = input("Enter the message to encode (or type 'back' to return to menu): ")
        if message.lower() == 'back':
            break
        valid_message = validate_input(message, 'str')
        if valid_message:
            print("Encoded message:", encode(valid_message, shift))

# Function to handle decoding process
def process_decoding(shift):
    while True:
        encoded_message = input("Enter the message to decode (or type 'back' to return to menu): ")
        if encoded_message.lower() == 'back':
            break
        valid_message = validate_input(encoded_message, 'str')
        if valid_message:
            print("Decoded message:", decode(valid_message, shift))

# Function to display examples of encoding and decoding
def show_examples():
    print("\nExamples:")
    print("Original: Hello World!")
    print("Encoded with shift 3: ", encode("Hello World!", 3))
    print("Decoded back: ", decode(encode("Hello World!", 3), 3))
    print("\nOriginal: Python Programming")
    print("Encoded with shift 5: ", encode("Python Programming", 5))
    print("Decoded back: ", decode(encode("Python Programming", 5), 5))

# Main function to control program flow
def main():
    print("Welcome to the Coding and Decoding Program")
    shift = get_shift_value()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            process_encoding(shift)
        elif choice == '2':
            process_decoding(shift)
        elif choice == '3':
            show_examples()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Additional functionality for advanced encoding
def advanced_encode(message, shift, preserve_case=True):
    alphabet = string.ascii_lowercase
    encoded_message = ""
    for char in message:
        if char.lower() in alphabet:
            base = alphabet if char.islower() else alphabet.upper()
            encoded_message += base[(base.index(char) + shift) % 26]
        else:
            encoded_message += char
    return encoded_message

# Advanced decoding function
def advanced_decode(message, shift, preserve_case=True):
    return advanced_encode(message, -shift, preserve_case)

# Example usage of advanced features
def demo_advanced_features():
    print("\nAdvanced Encoding Examples:")
    print("Original: Hello Advanced World!")
    print("Encoded with shift 4: ", advanced_encode("Hello Advanced World!", 4))
    print("Decoded back: ", advanced_decode(advanced_encode("Hello Advanced World!", 4), 4))

if __name__ == "__main__":
    main()
    # Only call demo_advanced_features if needed
    demo_advanced_features()
