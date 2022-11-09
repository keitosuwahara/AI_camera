#作成した出欠席表を表示するプログラムです
from flask import Flask,render_template,request
from operatedb import operatedb as opdb
app = Flask(__name__)

#トップページ
@app.route("/", methods=["GET","POST"])
def top():
    username=opdb()
    return render_template("/displaydb.html",users=username)


if __name__ == "__main__":
    app.run(debug=True)
