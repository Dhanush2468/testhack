from flask import Flask, render_template, send_file, make_response, request

app = Flask(__name__)

@app.route("/auth", methods=["POST"])
def auth():
    print(request.form.to_dict())
    return "ok"

@app.route("/")
def index():
    response = make_response(send_file("login.html"))
    # Just for localhost demonstration sake
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/login")
def login():
    return send_file("2fa.html")

if __name__ == "__main__":
    app.run()
