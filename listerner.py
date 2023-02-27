import socket
import tweepy


HOST, PORT = 'localhost', 9009
server = socket.socket()
server.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")
server.listen(5)
connection, address = server.accept()
print(f"Recebendo solicitação de {address}")

with open('bearer_token.txt') as token_file:
    TOKEN = token_file.read()
KEYWORD = 'one piece'


class TweetManager(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('='*20)
        connection.send(tweet.text.encode('latin1', 'ignore'))


printer = TweetManager(TOKEN)
printer.add_rules(tweepy.StreamRule(KEYWORD))
printer.filter()
