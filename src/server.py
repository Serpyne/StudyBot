from flask import Flask
from flask_cors import CORS
from threading import Thread


class Server(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config['DEBUG'] = False
        CORS(self)

        self.create_routes()

    def create_routes(self):
        @self.route("/")
        def index():
            return "Hello, World!"

    def start(self, *args, **kwargs):
        thread = Thread(target=self.run, args=args, kwargs=kwargs)

        thread.start()
