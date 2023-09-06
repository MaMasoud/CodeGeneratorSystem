from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from PIL import Image, ImageDraw, ImageFont
import os
import csv

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process_files():
    img_file = request.files['img']
    csv_file = request.files['csv']

    if img_file.filename == '' or csv_file.filename == '':
        return redirect(request.url)

    img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'input_image.jpg')
    img_file.save(img_path)

    csv_path = os.path.join(app.config['UPLOAD_FOLDER'], 'codes.csv')
    csv_file.save(csv_path)

    font_size = int(request.form['font_size'])
    font_color = tuple(int(request.form['font_color'][i:i+2], 16) for i in (1, 3, 5))
    code_position = int(request.form['code_position'])

    output_filenames = process_csv(img_path, csv_path, font_size, font_color, code_position)

    return redirect(url_for('result', filenames=output_filenames))

# ... (الكود السابق)

def process_csv(img_path, csv_path, font_size, font_color, code_position):
    output_filenames = []

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for index, code in enumerate(csvreader):
            code_text = code[0]
            img = Image.open(img_path).convert('RGB')
            draw = ImageDraw.Draw(img)
            
            # استخدام الخط البولد
            font = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", font_size)
            
            y_position = code_position 
            draw.text((120, y_position), code_text, font=font, fill=font_color)
            output_filename = f'output_{index}.jpg'
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            img.save(output_path)
            output_filenames.append(output_filename)

    return output_filenames

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/result')
def result():
    return render_template('result.html', filenames=request.args.getlist('filenames'))

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
