from flask import Flask , render_template , request, redirect , url_for
import openai

app = Flask(__name__)

openai.api_key = "YOUR_API_KEY" 

@app.route('/' , methods = ["GET" , "POST"])
def index():
    if request.method == 'POST':
        title = request.form['title']
        word = request.form['word']
        post = generate_post(title, word)
        return render_template("post.html", post=post, title=title , word = word)
    return render_template("index.html")

@app.route('/post')
def post():
    return render_template('post.html')


def generate_post(title , word):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt = f"I want to write a LinkedIn post that talks about me {title} , write the post in {word} words.",
        # prompt=f"Write a LinkedIn post about {title} with minimum 40 words and hashtags at the end",
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()



if __name__ == "__main__":
    app.run(debug=True)