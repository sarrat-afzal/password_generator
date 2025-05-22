import random #random lets us pick random characters
import string #string has letter, numbers, and symbols

def generate_password(length): #function to generate password of a certain length
    #combine letters, digits, and punctuation into one string
    characters = string.ascii_letters + string.digits + string.punctuation 

    #pick 'length' random characters and join them into a password string
    password = ''.join(random.choice(characters) for _ in range(length))

    return password #return the password generated

#main function
def main():
    print('Password Generator') #prints a header
    try:
        length = int(input('Enter desired password length: ')) #prompts user for password length and takes integer input
        if length <= 0: #input validation for length
            print('Length must be greater than 0.') #warning message if length is not positive
        else:
            print('Generate password:', generate_password(length)) #calls the function to generate password and prints it
    except ValueError: #if input is not an integer
        print('Invalid input. Please enter a positive integer.') #error message 

if __name__ == '__main__': #run the main function if this script is executed
    main() #calls the main function