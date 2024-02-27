from flask import Flask, request, render_template, make_response 
import json
import sys
#import pandas as pd

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        file = request.files['file']
        # Save the file to a specific location (you may need to modify this)
        file.save('uploaded_file.xlsx')
        return render_template("index.html", name='upload completed')
        
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
