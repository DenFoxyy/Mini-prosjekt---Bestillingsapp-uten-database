from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/bestilling", methods=["GET", "POST"])
def bestilling():

    produkter = [
        {"name": "Pizza", "image": "pizza.jpg"},
        {"name": "Burger", "image": "burger.jpg"},
        {"name": "Salat", "image": "salad.jpg"},
        {"name": "Wrap", "image": "wrap.jpg"},
    ]

    if request.method == "POST":
        navn = request.form["navn"]
        produkt = request.form["produkt"]
        storrelse = request.form["storrelse"]
        antall = request.form["antall"]
        kommentar = request.form.get("kommentar", "")

        return render_template(
            "bekreftelse.html",
            navn=navn,
            produkt=produkt,
            storrelse=storrelse,
            antall=antall,
            kommentar=kommentar
        )

    return render_template("bestilling.html", produkter=produkter)

if __name__ == "__main__":
    app.run(debug=True)