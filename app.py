from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = []  # Data disimpan sementara di memori

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    messages.append({'name': name, 'message': message})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
