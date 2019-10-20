from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__, template_folder='E:/python/Flask' )


db_uri = app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wishlist.db'
db = SQLAlchemy(app)

engine = create_engine(db_uri)


engine.execute('CREATE TABLE "wishlist" ('
               'wishlistname VARCHAR, '
               'wish VARCHAR,'
               'date VARCHAR);')
                       
@app.route("/")
def index():
    return render_template('index.html')
    
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    wishlistname = request.form['wishlistname']
    wish = request.form['wish']
    date = request.form['date']
    wish1 = request.form['wish1']
    date1 = request.form['date1']
    
    engine.execute('INSERT INTO "wishlist" (wishlistname, wish, date) VALUES (?,?,?)',(wishlistname, wish, date))
    engine.execute('INSERT INTO "wishlist" (wishlistname, wish, date) VALUES (?,?,?)',(wishlistname, wish1, date1))
    db.session.commit()

    return render_template('pass.html', wishlistname=wishlistname, wish=wish, date=date, wish1=wish1, date1=date1 ) 

if __name__ == '__main__':
    app.run(debug=True)