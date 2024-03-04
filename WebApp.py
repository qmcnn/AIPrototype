from flask import Flask, request, render_template, make_response
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd
import os
from collections import Counter

model = joblib.load("../AIPrototype2023/templates/model_webapp.joblib")
app = Flask(__name__)
scaler = StandardScaler()

@app.route('/myapp')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print('upload completed')
        file = request.files['file']
        upload_folder = '../AIPrototype2023/static/folder'
        file_path = os.path.join(upload_folder)

        # Save the uploaded file
        data = pd.read_excel(file)
        file.save(file_path)
        scaled_data = scaler.fit_transform(data)

        # Make predictions using the pre-trained model
        predictions = model.predict(scaled_data)

        # Count occurrences of each class
        class_counts = Counter(predictions)

        # Determine the template to render based on the majority class or the last prediction
        majority_class = class_counts.most_common(1)[0][0]
        last_prediction = predictions[-1]

        if majority_class == 0:
            result_template = 'normal.html'
        elif majority_class == 1 or last_prediction == 1:
            result_template = 'chronic.html'
        # Determine the template to render based on the prediction
        #if all(value == 0 for value in predictions):
        #    result_template = 'normal.html'
        #elif any(value == 1 for value in predictions):
        #    result_template = 'chronic.html'

        # Pass the predictions list to the template
            
        return render_template(result_template, predictions=predictions)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)


  #padding-left: 40px;
  #padding-bottom: 15px;
  #padding-top: 15px;
  #padding-right: 20px;

#style="bottom: 0px; text-align: center; left: 700px;"