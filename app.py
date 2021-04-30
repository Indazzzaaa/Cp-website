import os
from model import integrate
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime

img_file_path = ""  # nothing initially
app = Flask(__name__)
UPLOAD_FOLDER = "static/img_uploaded"


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


# this is code for saving images in the folder
@app.route('/validate', methods=['POST'])
def validate():
    if request.method == "POST":
        f = request.files['myfile']
        file_name = secure_filename(f.filename)
        # print(f"Your requested file found in {file_name} \n\n")
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        img_file_path = img_path
        f.save(img_path)
        # print(f"F file saved")

        # * Testing the model integration
        result_data = predict_the_output(img_path)
        # print(f"\n\n\nyour result data {result_data}\n\n\n")
        # return redirect(url_for("show_result", img_path=img_file_path))
        return render_template("results.html", img_path=img_path, result_data=result_data)


@app.route("/go_back", methods=['GET', 'POST'])
def go_back():

    return redirect('/')


# [Normal Functions]


def predict_the_output(img_url):
    model = integrate.ClassifyTarget(img_url)
    predction = model.get_result()
    # print(f"\n\n\n  your predicted result is : {predction}")
    return predction


if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(debug=True, port=5000)
