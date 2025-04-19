from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if not name or not age or not age.isdigit():
            return "Invalid input. Please enter a valid name and age."
        return f"Hello, {name}! You are {age} years old."
    return '''
        <form method="POST">
            Name: <input name="name"><br>
            Age: <input name="age"><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
