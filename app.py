import io

from flask import Flask, request, jsonify
import re
import urllib.request
import requests
from PIL import Image

import base64
import os
import numpy as np
import cv2
import urllib
import json
from face_util_first import compare_faces, face_rec

app = Flask(__name__)


@app.route('/face_match', methods=['POST', 'GET'])
def face_match():
    if request.method == 'POST':
        # check if the post request has the file part
        if ('file1' in request.files) and ('file2' in request.files):
            file1 = request.files.get('file1')
            file2 = request.files.get('file2')
            ret = compare_faces(file1, file2)
            resp_data = {"match": bool(ret)} # convert numpy._bool to bool for json.dumps
            return json.dumps(resp_data)



@app.route('/face_rec', methods=['POST','GET'])
def face_recognition():
    print("text")
    if request.method == 'POST':
        print_request(request)
        print("text")
        # check if the post request has the file part
        if 'file' in request.files:
            file = request.files.get('file')
            name = face_rec(file)
            resp_data = {'name': name }
            return json.dumps(resp_data)

        else:

            body = request.get_json(silent=True)

            # response = urllib.request.urlopen(body.get("url"))
            # image = Image.open(io.BytesIO(response))

            imgURL = body.get("url")
            path = urllib.request.urlretrieve(imgURL, "image/test.jpg")
            filename = "test.jpg"
            print('Image successfully Downloaded: ', filename)
            files = "./image/test.jpg"

            name = face_rec(files)
            resp_data = {'name': name}
            return json.dumps(resp_data)

    return '''
       <!doctype html>
       <title>Face Recognition</title>
       <h1>Upload an image</h1>
       <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=Upload>
       </form>
       '''


def print_request(request):
    # Print request url
    print(request.url)
    # print relative headers
    print('content-type: "%s"' % request.headers.get('content-type'))
    print('content-length: %s' % request.headers.get('content-length'))
    # print body content
    body_bytes = request.get_data()
    # replace image raw data with string '<image raw data>'
    body_sub = re.sub(b'(\r\n\r\n)(.*?)(\r\n--)',br'\1<image raw data>\3', body_bytes,flags=re.DOTALL)
    print(body_sub.decode('utf-8'))

if __name__ == '__main__':
    app.run()

