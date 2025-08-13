from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"  # Bắt buộc để dùng session

# Tài khoản mẫu
USERNAME = "admin"
PASSWORD = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        pw = request.form["password"]
        if name == USERNAME and pw == PASSWORD:
            session["user"] = name  # Lưu vào session
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Sai tên đăng nhập hoặc mật khẩu")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))  # Không đăng nhập thì về trang login
    return render_template("dashboard.html")

@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("home.html")

@app.route("/history")
def history():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("history.html")

@app.route("/settings")
def settings():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("settings.html")

@app.route("/logout")
def logout():
    session.pop("user", None)  # Xoá phiên đăng nhập
    return redirect(url_for("login"))

if __name__ == "__main__":
    # host="0.0.0.0" → cho phép truy cập từ IP LAN
    # debug=True → bật chế độ debug
    app.run(host="0.0.0.0", port=5000, debug=True)
