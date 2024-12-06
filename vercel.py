from vercel import Vercel
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Vercel!'

# Create a Vercel handler to handle serverless requests.
handler = Vercel(app)


