import random
import string


class Helpers:
    @staticmethod
    def generate_random_email():
        return f"test_{''.join(random.choices(string.ascii_lowercase, k=6))}@test.com"
