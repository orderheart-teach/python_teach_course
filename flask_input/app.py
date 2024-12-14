from flask_input.app import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)