from art import logo
print(logo)
alphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]

direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
text=input("Type your message:\n ").lower()
shift=int(input("Type your shift:\n "))
game_over = False
def caesar(original_text,shift_amount,encrypt_or_decrypt):
        output_text = ""
        if encrypt_or_decrypt == "decode":
            shift_amount *= -1
        for letter in original_text:
            if letter not in alphabet:
                output_text+=letter
                continue
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %=len(alphabet)
            output_text += alphabet[shifted_position]
        print(f"Your {encrypt_or_decrypt}d message is:{output_text}")
caesar(original_text=text,shift_amount=shift,encrypt_or_decrypt=direction)
while not game_over:
    restart=input("Type 'yes' to go again,type 'no' to stop: \n").lower()
    if restart=="yes":
        direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
        text=input("Type your message:\n ").lower()
        shift=int(input("Type your shift:\n "))

        caesar(original_text=text, shift_amount=shift, encrypt_or_decrypt=direction)
    elif restart=="no":
        game_over=True
        print("the program is over")
    else:
        print("print type 'yes' or 'no'")

