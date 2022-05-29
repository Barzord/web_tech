from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='laboratory_2', text='Hello, World!')


if __name__ == '__main__':
    app.run()