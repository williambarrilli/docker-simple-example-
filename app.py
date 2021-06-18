from flask import Flask, jsonify
import psycopg2
import pdb

app = Flask(__name__)

@app.route("/")
def getUsuarios(): 
    con = psycopg2.connect(host="0.0.0.0", port='5432', database='chamadosdp', user='postgres', password='postgres')
    cur = con.cursor()
    cur.execute('select * from usuarios')
    recset = cur.fetchall()
    return jsonify(recset)

if __name__ == "__main__":
    app.run(host="0.0.0.0")