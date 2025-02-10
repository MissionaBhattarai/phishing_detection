from flask import Flask, render_template, request

app = Flask(__name__)

def is_phishing(url):
    suspicious_keywords = ["login", "signin", "account", "verify", "banking", "paypal"]
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        return True
    if "@" in url or "//" in url.split("/")[2]:
        return True
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        if is_phishing(url):
            result = "⚠️ This URL is likely a phishing attempt!"
        else:
            result = "✅ This URL seems safe."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)