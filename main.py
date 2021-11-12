from constants import Const
from flask import Flask, jsonify
import pika

app = Flask(__name__)
constant = Const()


class MorseService:

    @staticmethod
    @app.route('/encrypt/<string:message>/', methods=['GET', 'POST'])
    def encrypt(message):
        cipher = ''
        for letter in message:
            if letter != ' ':
                cipher += constant.MORSE_CODE_DICT[letter.upper()] + ' '
            else:
                cipher += ' '

        return jsonify(
            {
                "message": message,
                "cipher": cipher
            }
        )

    @staticmethod
    def decrypt(cipher):
        pass

### this part does not work .. i could not handle rabbitmq as a message broker
class MessageBroker:
    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

    def send_message(self, message):
        self.channel.basic_publish(
            exchange='exchange',
            routing_key='key',
            body=message
        )
        self.connection.close()
        print("your message has been sent")

    def read_messages(self):
        pass


if __name__ == '__main__':
    massage = MessageBroker()
    massage.send_message('hellow')

    morse = MorseService()
    app.run(host='0.0.0.0', port=1105)
    print(morse.encrypt("Hi Solat"))


