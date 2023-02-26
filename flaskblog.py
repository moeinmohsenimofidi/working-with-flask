from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
    "author": "Moein.m.Mofidi",
    "title": "Blog post 1",
    "content": "First post contetn",
    "date" : "May 10, 2022"
    },
    {
    "author": "John champion",
    "title": "Blog post 2",
    "content": "Second post contetn",
    "date" : "Dec 10, 2022"
    },
    {
    "author": "Jack Foden",
    "title": "Blog post 3",
    "content": "Third post contetn",
    "date" : "Feb 10, 2023"
    }
]


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return  render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
