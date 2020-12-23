###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request, flash, redirect, url_for
from utils.forms import image_path_forms
from utils.convert_image import convert_images
from werkzeug.utils import secure_filename
import cv2
ci = convert_images()
###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'skjqsdkqsmldkùpkp09!!;dslqnk'

###############################################
#       Render Contact page                   #
###############################################
@app.route('/', methods=["GET","POST"])
def upload_file():
    filename=''
    if request.method == 'POST':
        image = request.files["file"]
        if image.filename != '':
            print('image uploaded')
            print(image)
            ci.get_image_converted(secure_filename(image.filename), 'test')
            filename1 = '.././results/test_pencil1.jpg'
            filename2 = '.././results/test_pencil2.jpg'
            filename3 = '.././results/test_cartoon.jpg'
            return render_template('render_results.html', filename=filename1, filename2=filename2, filename3=filename3)
    return render_template('image_path_forms.html', filename=filename)

###############################################
#       Render image results                   #
###############################################
@app.route('/render_results', methods=["GET","POST"])
def render_images():
    filename1 = '.././results/test_pencil1.jpg'
    filename2 = '.././results/test_pencil2.jpg'
    filename3 = '.././results/test_cartoon.jpg'
    return render_template('render_results.html', filename=filename1, filename2=filename2, filename3=filename3)



###############################################
#                Run app                      #
###############################################
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')