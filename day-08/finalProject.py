import arts

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(arts.logo)

def caeser(cipher_direction, message, shift_amount):
    if cipher_direction == "encode":
        cipher_text = ""
        for letter in message:
            if letter not in alphabet:
                cipher_text += letter
                continue
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is: {cipher_text}")
    elif cipher_direction == "decode":
        plain_text = ""
        for letter in message:
            if letter not in alphabet:
                plain_text += letter
                continue
            position = alphabet.index(letter)
            original_position = position - shift_amount
            original_letter = alphabet[original_position]
            plain_text += original_letter
        print(f"The decoded text is: {plain_text}")

retry = True
while retry:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > 26:
            print("Please enter a value less than 26 to the shift number.")
        elif shift < 0:
            print("Please enter a number greater than 0 to the shift number.")
        else:
            caeser(cipher_direction=direction, message=text, shift_amount=shift)
    else:
        print("Please run the code again and type a valid option")

    
    users_decision = input("Type 'yes' if you wnat to go again. Otherwise type 'no'.").lower()
    if users_decision == 'no':
        retry = False
