# Day 8 Project: Caesar Cipher
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

is_running = True

while(is_running):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(start_text, shift_amount, cypher_direction):
        end_text = ""
        for letter in start_text:
            if letter in alphabet:
                index = alphabet.index(letter)
                new_index = 0
                if cypher_direction == "encode":
                    new_index = (index + shift_amount) % len(alphabet)
                else:
                    new_index = (index - shift_amount) % len(alphabet)
                new_letter = alphabet[new_index]
                end_text += new_letter
            else:
                end_text += letter

        print(f"The {cypher_direction}d is {end_text}")

    caesar(start_text=text, shift_amount=shift, cypher_direction=direction)

    choice = input(
        f"Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if choice == 'no':
        is_running = False
        print("Goodbye")
