from flask import Flask, render_template, url_for, request,redirect

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    task_content=""
    if request.method == 'POST':
        task_content = request.form['content']
        return render_template('index.html',message=task_content)

    else:
        return render_template('index.html',message=task_content)

if __name__ == "__main__":
    app.run(debug=True)