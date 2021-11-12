from constants import Const


class Morse(Const):

    def encrypt(self, message):
        cipher = ''
        for letter in message:
            if letter != ' ':
                cipher += self.MORSE_CODE_DICT[letter.upper()] + ' '

            else:
                cipher += ' '

        return cipher

    def decrypt(self, cipher):
        pass


if __name__ == '__main__':
    morse = Morse()

    print(morse.encrypt("Hi Solat"))

