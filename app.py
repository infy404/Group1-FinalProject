from flask import Flask, jsonify, request, render_template
import pymongo

app = Flask(__name__, template_folder='Templates')


@app.route('/')
def hello():
    return render_template('homeFile.html')


@app.route('/google-charts')
def google_pie_chart():
    client = pymongo.MongoClient(
    "mongodb+srv://ShrijanK:dummyPassword1234@cluster0.wfpuf.mongodb.net/DprogDb?retryWrites=true&w=majority")
    myDb = client["DprogDb"]
    data = {"Provinces": "Total Cases"}
    for coll in myDb.list_collection_names():
        inner_dict = myDb[coll].find_one({}, {"_id": 0, "Date": 0})
        data[coll] = int((inner_dict["Total Cases"].replace(',', '')))  # Returns Total Number of Cases Only
    print(data)
    return render_template('pie-chart.html', data=data)
