from flask import Flask , render_template 
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/' , methods = ["GET" , "POST"])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)