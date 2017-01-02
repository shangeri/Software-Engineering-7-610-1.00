<<<<<<< HEAD
from flask import Flask, make_response


app = Flask(__name__)

@app.route("/")
def hello():
	
    return "Hello World!"

if __name__ == "__main__":
=======
from flask import Flask, make_response


app = Flask(__name__)

@app.route("/")
def hello():
	
    return "Hello World!"

if __name__ == "__main__":
>>>>>>> origin/master
    app.run()