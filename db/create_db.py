import sqlite3
import os
import pandas as pd


name_db='gazprom'
con = sqlite3.connect(os.getcwd() + '\\db\\' + name_db + '.db')
cursor = con.cursor()


def main():
    data = pd.read_csv(r'C:\Users\STEN CENTER ROSTOV\Desktop\PythonChallenge\AnnikaHansenBot\gazprom.csv')
    df = pd.DataFrame(data)
    cursor.execute('''CREATE TABLE land
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    region TEXT,
                    urlh TEXT,
                    min_price TEXT)
                ''')
    i = 1
    for row in df.itertuples():
        bob = (i, row.Title, row.Region, row.Url, row.Min_price)
        cursor.execute('INSERT INTO land (id, title, region, urlh, min_price) VALUES (?, ?, ?, ?, ?)', bob)
        i+=1
    con.commit()



if __name__ == '__main__':
    main()
