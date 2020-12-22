###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request, flash
from utils.forms import image_path_forms
from utils.convert_image import convert_images
###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'skjqsdkqsmldkùpkp09!!;dslqnk'

###############################################
#       Render Contact page                   #
###############################################
@app.route('/', methods=["GET","POST"])
def get_contact():
    form = image_path_forms()
    if request.method == 'POST':
        path =  request.form["path"]
        convert_images(path, 'resultat_apres_modifications')
        return render_template('image_path_forms.html', form=form)
        flash('Your changes have been saved.')
    else:
        return render_template('image_path_forms.html', form=form)

###############################################
#                Run app                      #
###############################################
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')