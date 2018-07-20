from flask import Flask, render_template

app = Flask (__name__)

# http://localhost:5000/
@app.route("/")
def index():
    return "hello flask!"

# http://localhost:5000/hello
@app.route("/hello")
def abc() :
    return render_template("hello.html")
    
if __name__ == "__main__" :
    app.run(debug=True)





