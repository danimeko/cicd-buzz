import os
import signal
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body style="background-image: url("https://vignette.wikia.nocookie.net/prodigy-math-game/images/0/0e/Community-header-background/revision/latest/scale-to-width-down/640?cb=20180106055623");">CI/CD Assignment three<br><h1>'
    page += generator.generate_buzz()
    page += '</h1><hr>the best footer ever</body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))