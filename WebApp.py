from flask import Flask, request, render_template, make_response 
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd
import os

model = joblib.load("../AIPrototype2023/templates/model_webapp.joblib")
app = Flask(__name__)
scaler = StandardScaler()
@app.route('/myapp')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        upload_folder = '../AIPrototype2023/static/data'
        file_path = os.path.join(upload_folder)

        # Save the uploaded file
        data = pd.read_excel(file)
        file.save(file_path)
        scaled_data = scaler.transform(data)

        # Make predictions using the pre-trained model
        predictions = model.predict(scaled_data)

        # Determine the template to render based on the prediction
        if predictions[0] == 0:
            return render_template('normal.html')
        elif predictions[0] == 1:
            return render_template('chronic.html')
        return render_template("normal.html", name='upload completed')


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001