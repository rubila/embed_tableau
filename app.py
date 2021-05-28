from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    
    return render_template('index.html', title='The Cost of 1 GB Mobile Data')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
