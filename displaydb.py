#作成した出欠席表を表示するプログラムです
from flask import Flask,render_template,request

app = Flask(__name__)

#トップページ
@app.route("/")
def top():
    return render_template("/displaydb.html")


if __name__ == "__main__":
    app.run(debug=True)
