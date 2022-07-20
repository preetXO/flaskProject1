import datetime as dt
from flask import Flask, render_template, request

app = Flask(__name__)

entries = []


@app.route('/', methods=['GET', 'POST'])
def home():
    # print(vars(request))
    if request.method == 'POST':
        entry_content = request.form.get('content')
        entries.append((entry_content, dt.datetime.today().strftime('%d-%m-%Y')))
    return render_template('home.html', entries=entries)


if __name__ == '__main__':
    app.run()
