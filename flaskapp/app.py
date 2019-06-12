from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test/')
def test():
    return 'Test'


@app.route('/test/<some_var>')
def test_var(some_var):
    return f'Test {some_var}'


@app.route('/healthcheck')
def healthcheck():
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
