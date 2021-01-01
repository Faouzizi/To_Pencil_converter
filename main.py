import os
from flask import Flask, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from utils.convert_image import convert_images
import base64
import cv2

ci = convert_images()




app = Flask(__name__)
app.config['SECRET_KEY'] = 'qs,dq;,sjdlqksjdopaidhsqkdhqjksSDSsdsHDJNKNDKHJSHD'
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()


photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB



class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    submit = SubmitField(u'Upload')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
        ci.get_image_converted(os.path.join('./'+filename), 'image_cartoon', app.config['UPLOADED_PHOTOS_DEST'])
        img_cartoon = base64.b64encode(open(os.path.join(app.config['UPLOADED_PHOTOS_DEST'] ,'image_cartoon_cartoon.jpg'),'rb').read()).decode('utf-8')
        img_pencil = base64.b64encode(open(os.path.join(app.config['UPLOADED_PHOTOS_DEST'] ,'image_cartoon_pencil.jpg'),'rb').read()).decode('utf-8')
    else:
        file_url = None
        img_cartoon = None
        img_pencil = None
    return render_template('image_path_forms2.html', form=form, file_origin_url=file_url, file_cartoon_url=img_cartoon, file_pencil_url=img_pencil)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')
