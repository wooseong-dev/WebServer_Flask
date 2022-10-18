from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client=MongoClient("mongodb://localhost", 27017)
#client=MongoClient("mongodb://localhost", 27017, username='username', password='password')
db=client.wooseongweb
todos = db.todos

#test_collection = db.client.wooseongweb
#db=connection["wooseongweb"]
#client = MongoClient("mongodb://%s:%s@localhost" % 27017)
@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content' : content, 'degree' : degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

#@app.post("/login")는 의 바로 가기입니다 . #3907@app.route("/login", methods=["POST"])
@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id" : ObjectId(id)})
    return redirect(url_for('index'))


@app.route("/view")
def view():
    #idx = request.args.get("idx") #id대용 예약어 : idx
    #print(db)
    #print(dir(db))
    #print(db.name)
    
    '''
    post = {
        "Name" : name, 
        "title" : title, 
        "contents":contents
        }
    db.testboard.insert_one(post)
    print(post)'''



    #post_id = db.testboard.insert_one(post).inserted_id
    #print(post_id)
    return render_template("view.html")



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
        db.board.insert_one(inf)
        
        print(name, title, contents)
        
        return ""
    else:
        return render_template("write.html")

@app.route("/crawler_result", methods={"POST"})
def result():
    if request.method == 'POST':
        pass
    else:
        pass

        return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
