from flask import Flask, render_template, request

# Create Flask App
app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Check Profile Route
@app.route("/check", methods=["POST"])
def check():
    username = request.form["username"]
    followers = int(request.form["followers"])
    following = int(request.form["following"])
    posts = int(request.form["posts"])
    bio = request.form["bio"]

    score = 0

    if followers < 50:
        score += 25

    if following > 1000:
        score += 25

    if posts < 3:
        score += 25

    if len(bio) < 5:
        score += 25

    if score >= 50:
        status = "High Risk ❌"
    else:
        status = "Low Risk ✅"

    return render_template(
        "result.html",
        username=username,
        percentage=score,
        status=status
    )

# Run App
if __name__ == "__main__":
    app.run(debug=True)