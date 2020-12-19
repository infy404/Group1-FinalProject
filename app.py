from flask import Flask, jsonify, request, render_template
import pymongo

app = Flask(__name__, template_folder='Templates')

client = pymongo.MongoClient(
    "mongodb+srv://ShrijanK:dummyPassword1234@cluster0.wfpuf.mongodb.net/DprogDb?retryWrites=true&w=majority")
myDb = client["DprogDb"]

@app.route('/')
def google_pie_chart():
    data = {"Provinces": "Total Cases"}
    for coll in myDb.list_collection_names():
        inner_dict = myDb[coll].find_one({}, {"_id": 0, "Date": 0})
        data[coll] = int((inner_dict["Total Cases"].replace(',', '')))  # Returns Total Number of Cases Only
    print(data)
    return render_template('pie-chart.html', data=data)


@app.route('/Ontario')
def line_chart_ON():
    data = []
    val = myDb["Ontario"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/British-Columbia')
def line_chart_BC():
    data = []
    val = myDb["British Columbia"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/Alberta')
def google_line_chart():
    data = []
    val = myDb["Alberta"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/Saskatchewan')
def line_chart_SK():
    data = []
    val = myDb["Saskatchewan"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/Manitoba')
def line_chart_MN():
    data = []
    val = myDb["Manitoba"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/Quebec')
def line_chart_QB():
    data = []
    val = myDb["Quebec"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/New-Brunswick')
def line_chart_NB():
    data = []
    val = myDb["New Brunswick"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/Nova-Scotia')
def line_chart_NS():
    data = []
    val = myDb["Nova Scotia"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/Prince-Edward-Island')
def line_chart_PEI():
    data = []
    val = myDb["Prince Edward Island"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/Newfoundland-and-Labrador')
def line_chart_NaL():
    data = []
    val = myDb["Newfoundland and Labrador"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/Yukon')
def line_chart_YK():
    data = []
    val = myDb["Yukon"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/Northwest-Territories')
def line_chart_NWT():
    data = []
    val = myDb["Northwest Territories"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/Nunavut')
def line_chart_NUT():
    data = []
    val = myDb["Nunavut"].find({}, {"_id": 0})
    for txt in val:
        pair = [v for k, v in txt.items()]
        data.append([pair[0], int(pair[1].replace(',', ''))])

    return render_template('line-chart.html', data=data)


@app.route('/api/all', methods=['GET'])
def api_all():
    data = []
    for coll in myDb.list_collection_names():
        tb_data = myDb[coll].find({}, {"_id": 0})
        for txt in tb_data:
            data.append(txt)
    return jsonify(data)