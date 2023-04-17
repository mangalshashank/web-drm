from flask import Flask, render_template, request, redirect,send_file
import hashlib
import endc
import contractBlock as md
from PIL import Image
import io
from werkzeug.datastructures import FileStorage
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check_drm():
    # Code to check DRM
    return "DRM checked"

@app.route('/apply')
def apply_drm():
    return redirect('/apply-page')

@app.route('/apply-page', methods=['GET', 'POST'])
def apply_page():
    if request.method == 'POST':
        # Get uploaded image data
        image = request.files.get('image')
        print(type(image))
        text = request.form.get('text')
        image = Image.open(image)
        image = endc.encode(image,text)
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        file_storage = FileStorage(buffered, filename="processed_image.png")
        return send_file(file_storage, mimetype='image/png',download_name='processed_image.png',as_attachment=True)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
