from flask import Flask,jsonify,request
from llm import submit_ocr_query,submit_image_buffer_query,submit_hybrid_query
from preprocessing import encode_image

app=Flask(__name__)

@app.route('/api/ocr',methods=['POST'])
def ocr_endpoint():

    fileName=request.files['file']

    r=submit_ocr_query(fileName)

    return jsonify({'message':r})


@app.route('/api/llm_image',methods=['POST'])
def llm_image_endpoint():

    fileName=request.files['file']

    r=submit_image_buffer_query(fileName)

    return jsonify({'message':r})


@app.route('/api/hybrid',methods=['POST'])
def hybrid_endpoint():

    fileName=request.files['file']

    r=submit_image_buffer_query(fileName)

    return jsonify({'message':r})


if __name__=='__main__':

    app.run(debug=True)
