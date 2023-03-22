from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/web')
def web():
    url = request.args.get('url')
    response = requests.get(url)
    return Response(response.content, content_type=response.headers['Content-Type'])
