import os
from flask import Flask, render_template, request
import imagepro as imgpro
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html', displayFlag=False)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    filename = secure_filename(file.filename)
    f = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(f)

    filtered_img = imgpro.canny_img_pro(f)
    imgpro.save_image('static/' + filename, filtered_img)
    #imgpro.sobel_img_pro(f)

    return render_template('index.html', uploadedfile=filename, displayFlag=True)