

class Postoffice:
    # create an empty list
    _letters = []

    # Python decorator to define class method in a Postoffice class
    @classmethod
    def send_letter(cls, letter):
        """
        Send a letter by adding it to the list of letters in the post office.

        Args:
            letter (Letter): The letter to be sent.
        """
        cls._letters.append(letter)

    # Python decorator to define class method in a Postoffice class
    @classmethod
    def get_letters(cls):
        """
        Get the letters from the post office and clear the list.

        Returns:
            list: A list of Letter objects.
        """
        letters = cls._letters
        cls._letters = []
        return letters
