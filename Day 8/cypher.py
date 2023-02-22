alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type the text that you want to cypher: \n").lower()
steps = int(input("Type the shift number: \n"))


def encrypt(text, steps):
    cypher_text = ""
    for i in range(0, len(text)):
        cypher_text += alphabet[alphabet.index(text[i]) + steps]

    return cypher_text


def decrypt(text, steps):
    decypher_text = ""
    for i in range(0, len(text)):
        decypher_text += alphabet[alphabet.index(text[i]) + 26 - steps]

    return decypher_text


if direction == "encode":
    print(f"The encoded text is: {encrypt(text, steps)}")
else:
    print(f"The decoded text is: {decrypt(text, steps)}")
