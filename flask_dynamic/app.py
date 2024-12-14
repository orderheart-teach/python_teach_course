from flask import Flask, render_template

# 创建Flask应用
app = Flask(__name__)

# 路由
@app.route("/")
def home():
    title = "Dynamic Flask Application"
    description = "This is a simple example demonstrating how Flask works with HTML, CSS and Python."
    return render_template("index.html",title = title, description = description)

# 运行应用
if __name__ == "__main__":
    app.run(debug=True)