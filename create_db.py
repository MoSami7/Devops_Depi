
def create_tables(db):
    conn = db.cursor()
    conn = db.execute("CREATE TABLE IF NOT EXISTS Book (ID INTEGER PRIMARY KEY AUTOINCREMENT ,Title TEXT NOT NULL,Author TEXT NOT NULL , pages INTEGER NOT NULL, price FLOAT  ,RetalPriceDay FLOAT ,RetalPeriod INTEGER ,TotalRental Float ,statu TEXT NOT NULL ) ")
    conn.close()
    return True