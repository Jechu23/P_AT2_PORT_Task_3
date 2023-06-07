"""Posting delivering"""

from postoffice import Postoffice


class Postie:
    """
        Define the class constructor, parameter route,
        When the new instance od the Postie class is created this constructor will be called automatically,
        and the route parameter will be passed to it.
    """

    def __init__(self, route):
        self._route = route

    # Method to deliver letter.
    def deliver_mail(self):
        for letter in Postoffice.get_letters():
            recipient = letter.recipient
            if recipient in self._route:
                recipient_letterbox = self._route[recipient].letterbox
                recipient_letterbox.receive_letter(letter)
