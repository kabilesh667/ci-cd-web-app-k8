from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the input form

@app.route('/result')
def result():
    name = request.args.get('name')  # Retrieves the 'name' parameter from the URL
    return render_template('result.html', name=name)  # Passes the name to the result template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
