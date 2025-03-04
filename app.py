from flask import Flask

app = Flask(__name__)

@app.route("/")
def homePage():
    return "Welcome to Budget Tracker"

@app.route("/addtransaction")
def addExpense():
    return "Here we can add Transacations"

@app.route("/showtransactions")
def showExpense():
    return "We can show all transacations here"

if __name__ == "__main__":
    app.run(debug=True)