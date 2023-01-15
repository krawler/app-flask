from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'Hello World by Flask', 200

app.run(host='0.0.0.0', port=8000)