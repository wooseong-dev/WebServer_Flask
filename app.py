from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client=MongoClient("mongodb://localhost", 27017)
db=client.wooseongweb

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/write", methods=["GET", "POST"])
def write():
    if request.method=="POST":
        name = request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")
        

        inf ={
            "name":name,
            "title":title,
            "contents":contents
        }
        db.boaard.insert_one(inf)
        
        print(name, title, contents)
        
        return ""
    else:
        return render_template("write.html")

if __name__ == "__main__":
    app.run(debug=True)
