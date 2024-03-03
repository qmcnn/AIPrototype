from flask import Flask, request, render_template, make_response
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd
import os

model = joblib.load("../AIPrototype2023/templates/model_webapp.joblib")
app = Flask(__name__)
scaler = StandardScaler()

# Initialize an empty list to store predictions
predictions = []

@app.route('/myapp')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['GET', 'POST'])
def upload_file():
    global predictions  # Declare predictions as a global variable

    if request.method == 'POST':
        file = request.files['file']
        upload_folder = '../AIPrototype2023/static/data'
        file_path = os.path.join(upload_folder)

        # Save the uploaded file
        data = pd.read_excel(file)
        file.save(file_path)
        scaled_data = scaler.fit_transform(data)

        # Make predictions using the pre-trained model
        predictions = model.predict(scaled_data)

        # Determine the template to render based on the prediction
        if all(value == 0 for value in predictions):
            result_template = 'normal.html'
        elif any(value == 1 for value in predictions):
            result_template = 'chronic.html'

        # Write the predictions to a CSV file
        csv_file_path = 'static/predictions.csv'
        with open(csv_file_path, 'w') as f:
            f.write('predict class\n')
            for result in predictions:
                f.write(f'{result}\n')

        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)

        # Convert DataFrame to HTML table
        table = df.to_html(index=False)

        # Pass the predictions list and table to the template
        return render_template(result_template, predictions=predictions, table=table)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)


  #padding-left: 40px;
  #padding-bottom: 15px;
  #padding-top: 15px;
  #padding-right: 20px;

#style="bottom: 0px; text-align: center; left: 700px;"