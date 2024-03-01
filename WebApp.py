from flask import Flask, request, render_template, make_response 
import json
import sys
#import pandas as pd

app = Flask(__name__)

@app.route('/myapp')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        #if 'file' not in request.files:
        #    flash('No file part')
        #    return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        #if file.filename == '':
        #    flash('No selected file')
        #    return redirect(request.url)
        file.save('filedata')
        return render_template("normal.html", name='upload completed')
##api post
#@app.route('/request',methods=['POST'])
#def web_service_API():
    
 #   payload = request.data.decode("utf-8")
 #   inmessage = json.loads(payload)

 #   print(inmessage)
    
    
 #   json_data = json.dumps({'y': 'received!'})
 #   return json_data


#@app.route("/")  
#def helloworld():
#    return "Hello, World!"

#@app.route("/name")  
#def hellochanoknan():
#    return "Hello, chanoknan!"

#@app.route("/home2")
#def home2():
 #   return render_template("home.html", name='chanoknan')

#@app.route("/home", methods=['POST','GET'])#เปิดรับpost
#def homefn():
#    if request.method == "GET":
#        print('we are in home(GET)', file=sys.stdout)
        #getting input with name = fname in HTML from
#        namein = request.args.get('fname')
 #       print(namein, file=sys.stdout)
 #       return render_template("home.html", name=namein)
    
#    elif request.method == "POST":
#        print('we are in home(POST)', file=sys.stdout)
#        #getting input with name = fname in HTML from
#        namein = request.form.get('fname')
#        lastnamein = request.form.get('lname')
#        print(namein, file=sys.stdout)
#        print(lastnamein, file=sys.stdout)
#        return render_template("home.html", name=namein)



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001