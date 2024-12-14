from flask_template.app import Flask, render_template

# 创建 Flask 应用
app = Flask(__name__)

# 路由：主页
@app.route('/')
def home():
    return render_template('index.html')

# 运行应用
if __name__ == '__main__':
    app.run(debug=True)