from flask import Flask, jsonify, request
app= Flask(__name__)

@app.route("/chatbot_example", methods=["POST"])
def chatbot():
    age = 30
    sex = "Male"
    return {
        "fulfillmentText": f"It's a {age} year old {sex}."
        }

@app.route("/post_example", methods=["POST"])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        return jsonify(str("Successfully stored  " + str(data)))

@app.route("/get_example", methods=["GET"])
def message():
    posted_data = request.get_json()
    name = posted_data['name']
    return jsonify(" Hope you are having a good time " +  name + "!!!")
if __name__=='__main__':
    app.run(debug=True)


