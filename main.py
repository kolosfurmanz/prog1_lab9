#Zachary Kolos-Furman

def encode(string):
    new_string = ""
    for char in string:
        new_string += f"{int(char) + 3}"
    return new_string

def decode(string):
    new_string = ""
    for char in string:
        new_string += f"{int(char) - 3}"
    return new_string

def main():
    loop = True
    n = 0
    while loop:
        print("Menu")
        print("-------------")
        print("1.  Encode")
        print("2.  Decode")
        print("3.  Quit")
        print()
        option = input("Please enter an option: ")
        if n == 0:
            encoded_password = ""
        
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            n += 1           
            print("Your password has been encoded and stored!")
            print()
        
        elif option == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print()
        
        elif option == "3":
            break

        else:
            print("Error. Unrecognized input.")
            print()

if __name__ == "__main__":
    main()

