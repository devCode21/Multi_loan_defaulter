from flask import Flask ,render_template,request ,send_file
from src.pipelines.test_pipeline import test_Csv_Data
import os
app=Flask(__name__)

@app.route('/')
def home_page():
    return "hello world"


@app.route('/prediction' )
def Prediction_to_csv():
    return render_template('uploadcsv.html')


@app.route('/predict', methods=['POST'])
def predict():
   
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]

    # Your function that processes and saves CSV in artifacts/
    test_Csv_Data().test_Csv_data(file)

    file_path = os.path.join("artifacts", "test_data.csv")

    return send_file(
        file_path,
        mimetype="text/csv",
        as_attachment=True,
        download_name="test_data.csv"
    )

    

if __name__=='__main__':
    app.run(debug=True)