import datetime as dt
from pymongo import MongoClient
from flask import Flask, render_template, request

app = Flask(__name__)
client = MongoClient('mongodb+srv://preet:preetlearning@microblog.jprlvzr.mongodb.net/test')
app.db = client.Microblog
entries = []

@app.route('/', methods=['GET', 'POST'])
def home():
    # print(vars(request))
    # print([e for e in app.db.entries.find({})])
    if request.method == 'GET':
        [entries.append((e['content'], e['date'])) for e in app.db.entries.find({})]
    elif request.method == 'POST':
        entry_content = request.form.get('content')
        formatted_date = dt.datetime.today().strftime('%d-%m-%Y')
        entries.append((entry_content, formatted_date))
        app.db.entries.insert_one({'content': entry_content, 'date': formatted_date})
    entries_with_dates = [
        (entry[0],
         entry[1],
         dt.datetime.strptime(entry[1], '%d-%m-%Y').strftime('%b %d'))
        for entry in entries
    ]
    return render_template('home.html', entries=entries_with_dates)


if __name__ == '__main__':
    app.run()
