#coding: utf-8

from flask import Flask, render_template
# appという名前でFlaskオブジェクトをインスタンス化
app = Flask(__name__)

# __view側の設定__
# ルートディレクトリにアクセスした場合の挙動
@app.route('/')
def index():
    # return 'Hello World!'
    return render_template('index.html')

# エントリーポイント
if __name__ == '__main__':
    app.run()




