from flask import Flask

app = Flask(__name__)

# Index view at the base URL
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f"<p>{parameter}</p>"

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(i) for i in range(1, parameter + 1)]
    return "<br>".join(numbers)

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero is undefined"
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return "Error: Modulus by zero is undefined"
        result = num1 % num2
    else:
        return "Invalid operation"
    
    return f"<p>The result of {num1} {operation} {num2} is {result}</p>"

if __name__ == '__main__':
    app.run(debug=True)
