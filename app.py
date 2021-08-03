from flask import Flask , render_template , request, jsonify
import json

with open('./mf.json', 'r') as myfile:
    data = myfile.read()


def is_success(arr):
    status = "true"
    for i in range(len(arr)):
        if type(arr[i])!=int:
            if type(int(arr[i]))!=int:
                status = "false"
                return status
            else:
                arr[i] = int(arr[i])
    return status

def oe(arr):
    status = is_success(arr)
    if status == "false":
        pred = ["is_success : false"]
        return pred
    else:
        p1 = "is_success : true"
        p2 = {"is_success" : "true"}
        odd = []
        #odd1 = ["odd",":",odd]
        even = []
        id = "user_id : divyanshu_dev_awasthi_16071999"
        for i in arr:
            if i%2!=0:
                odd.append(i)
            else:
                even.append(i)
        odd1 = {"odd" : odd}
        even1 = {"even": even}
        pred = [p1,id,odd1,even1]
        return pred

        result = {
            "is_success": status,
            "user_id": "divyanshu_dev_awasthi_16071999",
            "odd": "{}".format(odd),
            "even": "{}".format(even)
        }
        #return result
        #return jsonify(results=result)




app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/bfhl',methods=["POST"])

def predict():
    arr= request.form.get('movie').split(",")
    pred =oe(arr=arr)
    return render_template('index.html', prediction_text ="Recommend{}".format(pred), data=pred, len=len(pred))
    #return render_template('index.html', title="page", jsonfile=json.dumps(pred))
    #return jsonify(pred)
if __name__ == '__main__':
    app.run(debug=True , port='8000')
