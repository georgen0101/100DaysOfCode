from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Running...")

def caesar(plain_text, shift_amount, cipher_direction):
    shifted_text = ""
    for letter in plain_text:
        if letter.isalpha():
            letter_position = alphabet.index(letter)
            shifted_letter_position = letter_position
            if cipher_direction == "encode":
                shifted_letter_position += shift_amount
            elif cipher_direction == "decode":
                shifted_letter_position -= shift_amount
            else:
                    print("Error: Invalid direction!")
            shifted_text += alphabet[shifted_letter_position]
        else:
            shifted_text += letter
    print(f"\n Text: {shifted_text} \n")

# Start
print(logo)
running = True
while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if shift > 26:
        shift = shift % 26
    
    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

    user_choice = input("Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()

    if user_choice == "no":
        running = False
    elif user_choice == "yes":
        continue
    else:
        print("Error: Invalid answer!")
        running = False

print("Exiting...")