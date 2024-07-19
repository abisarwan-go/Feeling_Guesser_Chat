import json
from channels.generic.websocket import WebsocketConsumer

from chatDjango.nlp_utils import predict_sentiment_message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        result = predict_sentiment_message(message)
        result = "negative message" if result == 0 else "positive message"
        self.send(text_data=json.dumps({
            'message': result
        }))
