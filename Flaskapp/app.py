from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with Bootstrap for styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Web Application</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            padding-top: 50px;
        }
        .container {
            max-width: 600px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="text-center">
            <h1>Welcome to the Flask App!</h1>
            <p class="lead">A simple web app with user input and error handling</p>
        </div>

        <div class="card mt-5">
            <div class="card-body">
                <h3 class="card-title">Hello, World!</h3>
                <p class="card-text">Visit the "Form" page to submit your details.</p>
                <a href="/form" class="btn btn-primary">Go to Form</a>
            </div>
        </div>

        {% if message %}
        <div class="alert alert-info mt-4">
            <strong>{{ message }}</strong>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

FORM_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Your Details</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            padding-top: 50px;
        }
        .container {
            max-width: 600px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2 class="text-center">Enter Your Details</h2>
        <form method="POST">
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" name="name" placeholder="Enter your name" required>
            </div>
            <div class="mb-3">
                <label for="age" class="form-label">Age</label>
                <input type="number" class="form-control" id="age" name="age" placeholder="Enter your age" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        <a href="/" class="btn btn-secondary mt-3">Back to Home</a>

        {% if message %}
        <div class="alert alert-info mt-4">
            <strong>{{ message }}</strong>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/form', methods=['GET', 'POST'])
def form():
    message = ""
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        # Basic validation
        if not name or not age:
            message = "Name and Age are required fields!"
        elif not age.isdigit():
            message = "Please enter a valid number for age."
        else:
            message = f"Hello, {name}! You are {age} years old."

    return render_template_string(FORM_TEMPLATE, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
