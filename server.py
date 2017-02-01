# coding:utf-8
from flask import Flask, render_template, request
from werkzeug import secure_filename
from classifier import otaku_classifier
import os

app = Flask(__name__)
form_name = 'img'

# ブラウザ用
@app.route('/')
def index():
    return render_template('index.html', name=form_name)

# imgフォームに画像をセットしてPOST
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method != 'POST':
        return "error: POST only\n"
    if form_name not in request.files:
        return "error: Set image to 'img' form\n"

    img = request.files[form_name]
    if not img.filename:
        return "error: Set image to 'img' form\n"

    path = os.path.join('images', secure_filename(img.filename))
    img.save(path)
    return 'yes' if is_otaku(path) else 'no'

# 判別機
def is_otaku(path):
    # オタク識別器を通してオタクか判定
    return otaku_classifier(path)


if __name__ == '__main__':
    app.debug = os.getenv('OTAKU_DEBUG', False)
    app.run(host='0.0.0.0')
