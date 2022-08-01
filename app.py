import datetime as dt
from pymongo import MongoClient
from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)
    client = MongoClient('mongodb+srv://preet:preetlearning@microblog.jprlvzr.mongodb.net/test')
    app.db = client.Microblog
    entries = []


    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            entry_content = request.form.get('content')
            formatted_date = dt.datetime.today().strftime('%d-%m-%Y')
            app.db.entries.insert_one({'content': entry_content, 'date': formatted_date})

        entries_with_dates = [
            (entry['content'],
             entry['date'],
             dt.datetime.strptime(entry['date'], '%d-%m-%Y').strftime('%b %d'))
            for entry in app.db.entries.find({})
        ]
        return render_template('home.html', entries=entries_with_dates, name='Preet')
    return app

if __name__ == '__main__':
    create_app().run(debug=True)
