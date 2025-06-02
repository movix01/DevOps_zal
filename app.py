from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Prosty Kalkulator</title>
</head>
<body>
    <h1>Kalkulator</h1>
    <form method="post">
        <input type="number" name="num1" step="any" required>
        <select name="operator">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" name="num2" step="any" required>
        <input type="submit" value="Oblicz">
    </form>
    {% if result is not none %}
        <h2>Wynik: {{ result }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operator = request.form["operator"]

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = "Nie można dzielić przez zero!" if num2 == 0 else num1 / num2
        except ValueError:
            result = "Błąd danych wejściowych!"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
