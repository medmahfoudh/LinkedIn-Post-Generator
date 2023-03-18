from flask import Flask , render_template , request
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route('/' , methods = ["GET" , "POST"])
def index():
    if request.method == 'POST':
        title = request.form['title']
        post = generate_post(title)
        return render_template("index.html", post=post, title=title)
    return render_template("index.html")

def generate_post(title):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Write a LinkedIn post about {title}.",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)