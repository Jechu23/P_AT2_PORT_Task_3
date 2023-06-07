"""
Name: Jesus Huanambal
ID: 20096888
Date: 17/03/2023
Assessment : Part AT2 Task 2
"""


import time
from person import Person
from postie import Postie
from letter import Letter
from postoffice import Postoffice

if __name__ == '__main__':
    alice = Person('Alice')
    bob = Person('Bob')
    # key to open the letter
    key = 1

    # Create a postie and assign a route
    postie = Postie({'Bob': bob})

    message = 'Hi Bob, how are you mate?.\nWhats news?\nBye\nAlice\n'
    encrypted_message = Letter('Alice', 'Bob', message).get_contents(key)
    alice.write_letter(bob, encrypted_message)

    # Postie picks up the letter from the Postoffice and delivers it to Bob's letterbox
    postie.deliver_mail()

    # Read letters
    while True:
        try:
            input_key = int(input("Enter the decryption key to open the letter: "))
            if input_key == key:
                # Bob checks his letterbox
                bob.read_letters(key)
                break
            else:
                print("Incorrect key. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer key.")




