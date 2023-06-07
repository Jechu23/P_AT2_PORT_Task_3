"""Define the class Person in this case Alice and Bob"""

from letterbox import Letterbox
from letter import Letter
from postoffice import Postoffice


class Person:
    # method initializes a new Person instance with a given name, Letterbox instance to store as an attribute.

    def __init__(self, name):
        """
        Initialize a new Person instance.

        Args:
            name (str): The name of the person.
        """
        self._name = name
        self._letterbox = Letterbox()

    def write_letter(self, recipient, contents):
        """
        Write a letter to the recipient and drop it off at the Post Office.

        Args:
            recipient (Person): The recipient of the letter.
            contents (str): The contents of the letter.
        """
        letter = Letter(self._name, recipient.name, contents)
        encrypted_message = letter.get_contents(1)
        encrypted_letter = Letter(self._name, recipient.name, encrypted_message)
        Postoffice.send_letter(encrypted_letter)

    def read_letters(self, key):
        """
        Read the letters in the person's letterbox.

        Args:
            key (int): The decryption key to read the contents of the letters.
        """
        self._letterbox.check_for_new_letters(key)

    @property
    def name(self):
        # str: The name of the person.
        return self._name

    @property
    def letterbox(self):
        # Letterbox: The letterbox of the person.
        return self._letterbox


