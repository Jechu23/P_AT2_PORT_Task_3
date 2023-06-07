"""Define the class Letter"""


class Letter:
    """
    Represents a letter with sender, recipient, contents, and read status.
    """

    def __init__(self, sender, recipient, contents):
        """
        Initialize a new Letter instance.

        Args:
            sender (str): The name of the sender.
            recipient (str): The name of the recipient.
            contents (str): The contents of the letter.
        """
        self._sender = sender
        self._recipient = recipient
        self._contents = self._encrypt(contents)
        self._is_read = False

    # Mark the letter as read.
    def mark_read(self):

        self._is_read = True

    # Mark the letter as unread.
    def mark_unread(self):
        self._is_read = False

    def _encrypt(self, message):
        """
        Encrypts the given message by shifting each character's ASCII value by 1.

        Args:
            message (str): The message to be encrypted.

        Returns:
            str: The encrypted message.
        """
        encrypted = ''
        for char in message:
            encrypted += chr(ord(char) + 1)
        return encrypted

    def _decrypt(self, message, key):
        """
        Decrypts the given message by shifting each character's ASCII value back by the key.

        Args:
            message (str): The message to be decrypted.
            key (int): The decryption key.

        Returns:
            str: The decrypted message.
        """
        decrypted = ''
        for char in message:
            decrypted += chr(ord(char) - key)
        return decrypted

    def get_contents(self, key):
        """
        Get the decrypted contents of the letter.

        Args:
            key (int): The decryption key.

        Returns:
            str: The decrypted contents.
        """
        return self._decrypt(self._contents, key)

    @property
    def sender(self):
        """
        str: The sender of the letter.
        """
        return self._sender

    @property
    def recipient(self):
        """
        str: The recipient of the letter.
        """
        return self._recipient

    @property
    def is_read(self):
        """
        bool: The read status of the letter.
        """
        return self._is_read


