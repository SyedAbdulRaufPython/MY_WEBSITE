from flask import Flask, render_template, redirect, request
import requests
import ai.learning as learning

app = Flask(__name__)

qusitions_from_ai = []

YOUR_DOMAIN = 'http://127.0.0.1:5000/'


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    return render_template("chat.html")

@app.route("/login") 
def login():
    return render_template("login.html")

@app.route("/Pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/ask-ai", methods=["GET", "POST"])
def ask_ai():
    if request.method == "POST":
        user_input = request.form["user_input"]

        qusitions_from_ai.append(user_input)

        print(qusitions_from_ai)

    return render_template("index.html")

@app.route('/signup', methods=['POST'])
def signup():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # Here you would add code to save the user to your database
    # For example, hash the password and store the user details

    return redirect('/login')  # Redirect to login page after successful sign-up
    
@app.route('/signin', methods=['POST'])
def signin():
    # Get form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Here you would add code to verify the user against your database
    # For example, check the hashed password and authenticate the user

    return redirect('/')  # Redirect to home page after successful sign-in

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    return render_template('checkout.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
