from constants import Const
from flask import Flask

# creating app
app = Flask(__name__)
constant = Const()


class Morse:

    @staticmethod
    @app.route('/encrypt/<string:message>/', methods=['GET', 'POST'])
    def encrypt(message):
        cipher = ''
        for letter in message:
            if letter != ' ':
                cipher += constant.MORSE_CODE_DICT[letter.upper()] + ' '

            else:
                cipher += ' '

        return cipher

    @staticmethod
    def decrypt(cipher):
        pass


if __name__ == '__main__':
    morse = Morse()
    app.run(host='0.0.0.0', port=1105)
    print(morse.encrypt("Hi Solat"))
