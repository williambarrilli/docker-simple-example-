from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/")
def getUsuarios(): 
    con = psycopg2.connect(host='postgres', port='5432', database='postgres',user='postgres', password='postgres')
    cur = con.cursor()
    cur.execute("SELECT * FROM usuarios")
    recset = cur.fetchall()
    return jsonify(recset)

if __name__ == "__main__":
    app.run(host="0.0.0.0")