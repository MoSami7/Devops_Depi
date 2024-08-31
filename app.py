from ast import Pass
from sqlite3 import Cursor
from flask import Flask , render_template ,request ,url_for ,redirect
from create_db import create_tables
from FuctionDatabase import get_db
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/' , methods = ['GET' , 'POST'])
def index(): 
    if request.method == "POST":
        Title = request.form['Title']
        Author = request.form['Author']
        pages = request.form['pages']
        price = request.form['price']
        RetalPriceDay = request.form['RetalPriceDay']
        RetalPeriod = request.form['RetalPeriod']
        statu = request.form['statu']
        
        
        cursor = conn.cursor()  
        cursor.execute("selecconn = get_db()t * from Book")
        x = cursor.fetchall()
        
        if RetalPriceDay:
            TotalRental =  float(RetalPriceDay) * float(RetalPeriod)
            cursor.execute(f"INSERT INTO Book(Title,Author,pages,price,RetalPriceDay,RetalPeriod,TotalRental,statu) values('{Title}','{Author}','{pages}',{0},{RetalPriceDay},{RetalPeriod},{TotalRental},'{statu}');")
            conn.commit()
        else:
            cursor.execute(f"INSERT INTO Book(Title,Author,pages,price,RetalPriceDay,RetalPeriod,TotalRental,statu) values('{Title}','{Author}','{pages}',{price},{0},{0},{0},'{statu}');")
            conn.commit()
        cursor.close()
        return redirect(url_for("index"))
    conn = get_db()
    cursor = conn.cursor()    
    cursor.execute("select * from Book")
    
    data = cursor.fetchall()
    sumofbook = len(data)
    sumofbookSold = 0
    sumofbookRental = 0
    sumofbookAvailable = 0
    sumofbookprice = 0
    sumofbookrental = 0
    for s in data:
        if(s[8] == "Sold"):
            sumofbookprice += s[4]
        sumofbookrental += s[7]
        if s[8] == 'Available':
            sumofbookAvailable += 1
        elif s[8] == 'Rental':
            sumofbookRental += 1
        else:
            sumofbookSold += 1
    cursor.close()
    TotalPrice = sumofbookprice + sumofbookrental
    return render_template("pages/index.html" , databook = data , allbook = sumofbook , sumofbookRental = sumofbookRental,sumofbookSold = sumofbookSold , sumofbookAvailable = sumofbookAvailable, TotalPrice = TotalPrice , sumofbookprice = sumofbookprice  , sumofbookrental = sumofbookrental)


@app.route('/books' , methods = ['GET' , 'POST'])
def books():
    conn = get_db()
    cursor = conn.cursor()  
    if request.method == "GET":
        cursor.execute("select * from Book")
        data = cursor.fetchall()
        cursor.close()
        return render_template("pages/books.html" , databook = data)
    elif request.method == "POST": 
        Name = request.form['search_name']
        cursor.execute(f"select * from Book WHERE Title LIKE '%{Name}%' ;")
        data = cursor.fetchall()
        cursor.close()
        return render_template("pages/books.html" , databook = data)

@app.route('/Available' , methods = ['GET' , 'POST'])
def Available():
    conn = get_db()
    cursor = conn.cursor()  
    cursor.execute("select * from Book WHERE statu = 'Available' ")
    data = cursor.fetchall()
    cursor.close()    
    return render_template("pages/books.html" , databook = data)

@app.route('/Sold' , methods = ['GET' , 'POST'])
def Sold():
    conn = get_db()
    cursor = conn.cursor()  
    cursor.execute("select * from Book WHERE statu = 'Sold' ")
    data = cursor.fetchall()
    cursor.close()    
    return render_template("pages/books.html" , databook = data)

@app.route('/Rental' , methods = ['GET' , 'POST'])
def Rental():
    conn = get_db()
    cursor = conn.cursor()  
    cursor.execute("select * from Book WHERE statu = 'Rental' ")
    data = cursor.fetchall()
    cursor.close()    
    return render_template("pages/books.html" , databook = data)

@app.route('/delete/<ID>' , methods=['POST' ,'GET'])
def delete(ID):  
    
    if request.method == 'POST':
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Book WHERE ID = {ID};")
        
        conn.commit()
        cursor.close()
    elif request.method == 'GET':
        return render_template("pages/delete.html" )
    return redirect(url_for("index"))
  
@app.route('/update/<ID>' , methods=['POST' ,'GET'])
def update(ID):

    conn = get_db()
    cursor = conn.cursor()
    if request.method == 'POST':
        Title = request.form['Title']
        Author = request.form['Author']
        pages = request.form['pages']
        price = request.form['price']
        RetalPriceDay = request.form['RetalPriceDay']
        RetalPeriod = request.form['RetalPeriod']
        statu = request.form['statu']
        
        
        if RetalPriceDay:
            TotalRental = float(RetalPriceDay) * float(RetalPeriod)
            cursor.execute(f"UPDATE Book SET Title = '{Title}', Author = '{Author}' , pages = {pages}, price = {0}, RetalPriceDay = {RetalPriceDay}, RetalPeriod = {RetalPeriod}, TotalRental = {TotalRental}, statu = '{statu}' WHERE ID = {ID};")
        else:
            cursor.execute(f"UPDATE Book SET Title = '{Title}', Author = '{Author}' , pages = {pages}, price = {price}, RetalPriceDay = {0}, RetalPeriod = {0}, TotalRental = {0}, statu = '{statu}' WHERE ID = {ID};")
        conn.commit()
        cursor.close()
    elif request.method == 'GET':
        cursor.execute(f"select * from Book WHERE ID = {ID}")
        data = cursor.fetchone()
        conn.close()
        return render_template("pages/update.html" , databook = data)
    return redirect(url_for("index"))


if (__name__ == '__main__'):
    conn = get_db()
    create_tables(conn)
    app.run(debug=True , port=8080)