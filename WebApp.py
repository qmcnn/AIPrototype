from flask import Flask, request, render_template, make_response 
from sklearn.preprocessing import StandardScaler
import joblib

model = joblib.load("../AIPrototype2023/templates/model_webapp.joblib")

def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path, encoding='latin1')
    return data.values

app = Flask(__name__)

@app.route('/myapp')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        # Save the uploaded file
        file_path = f"{file.filename}"
        file.save(file_path)

        # Load the data from the file
        data = load_data(file_path)

        # Rescale the data using the previously created scaler
        scaler = StandardScaler()
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