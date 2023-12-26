from flask import Flask , render_template , request, redirect , url_for
import openai
import os

app = Flask(__name__)

openai.api_key = "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" 

@app.route('/' , methods = ["GET" , "POST"])
def index():
    if request.method == 'POST':
        global title 
        title = request.form['title']
        global word 
        word = request.form['word']
        global post 
        post = generate_post(title , word)
        return redirect('post')
    return render_template("index.html")

@app.route('/post')
def post_generated():
    return render_template('post.html', post=post, title=title , word = word)


def generate_post(title , word):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt = f"I want to write a LinkedIn post that talks about me {title} , write the post in minimum {word} words.",
        # prompt=f"Write a LinkedIn post about {title} with minimum 40 words and hashtags at the end",
        max_tokens= 1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip() 



if __name__ == "__main__":
    app.run(debug=True)