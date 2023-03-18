from flask import Flask , render_template , request, redirect , url_for
import openai

app = Flask(__name__)

openai.api_key = "YOUR_API_KEY"

@app.route('/' , methods = ["GET" , "POST"])
def index():
    if request.method == 'POST':
        title = request.form['title']
        post = generate_post(title)
        return render_template("post.html", post=post, title=title)
    return render_template("index.html")

@app.route('/post')
def post():
    return render_template('post.html' , post = post )


def generate_post(title):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Write a LinkedIn post about {title} with hashtags.",
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)