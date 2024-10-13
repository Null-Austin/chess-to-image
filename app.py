from flask import Flask, send_file, request
from datatohtml import *

app = Flask(__name__)

@app.route('/image')
def get_image():
    user = request.args.get('user')
    

    image_path = 'users/USER' + user + '.png'

    takescreenshot(user)

    return send_file(image_path, mimetype='image/jpeg')

@app.route('/html')
def get_html():
    user = request.args.get('user')
    return(gethtml(user))

@app.route('/')
def index():
    return(open('index.html').read())

if __name__ == '__main__':
    app.run(debug=True)
