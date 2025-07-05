"""
This project uses functions, loops, conditionals
"""
def encrypt(str):
    encrypted_phrase = ""
    for letter in str:
        if letter == " ":
            letter = " "
            encrypted_phrase += letter
        elif letter in "aeiouAEIOU":
            if letter in "aA":
                letter = "!"
                encrypted_phrase += letter
            elif letter in "Ee":
                letter = "#"
                encrypted_phrase += letter
            elif letter in "Ii":
                letter = "@"
                encrypted_phrase += letter
            elif letter in "Oo":
                letter = "$"
                encrypted_phrase += letter
            elif letter in "Uu":
                letter = "&"
                encrypted_phrase += letter
        else:
            letter = chr(ord(letter)+3)
            encrypted_phrase += letter
    return encrypted_phrase

print("-"*30)
print("Here are the main rules of our language:") 
print("a --> !") 
print("e --> #") 
print("i --> @") 
print("o --> $") 
print("u --> &") 
print("any other letter --> the letter after it by three letters")
print("-"*30)

original_phrase = input("Enter a phrase: ")
print("-"*30)
print(f"The encrypted phrase is: {encrypt(original_phrase)}")
print("-"*30)