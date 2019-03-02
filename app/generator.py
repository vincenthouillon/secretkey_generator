import os
import random
import string

class Generator:

    def flask_generator(self):
        return os.urandom(24)

    def django_generator(self):
        chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')
        SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])
        return SECRET_KEY