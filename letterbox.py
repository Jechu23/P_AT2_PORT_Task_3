"""Define the clas Letterbox"""


class Letterbox:
    """
    Represents a letterbox to store letters.
    """

    def __init__(self):
        """
        Initialize a new Letterbox instance.
        """
        self._letters = []

    # # Receive a letter to store in the list.
    def receive_letter(self, letter):
        self._letters.append(letter)

    #  # Get all unread letters in the letterbox.
    def get_unread_letters(self):
        return [letter for letter in self._letters if not letter.is_read]

    # # Check for new letters in the letterbox, print them, and mark then as read.
    def check_for_new_letters(self, key):
        unread_letters = self.get_unread_letters()
        for letter in unread_letters:
            print(f'From: {letter.sender}\nTo: {letter.recipient}\nContent: {letter.get_contents(key)}')
            letter.mark_read()
