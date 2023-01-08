from flask import Flask, request, render_template
"""
app = Flask(__name__)

@app.route('/')
def form_page():
  return render_template('index.html')


@app.route('/search')
def search_page():
  p = request.args['y']
  return f'Вы ввели слово {p}'

app.run()
"""

app = Flask(__name__)

@app.route('/')
def page_form():
  return render_template('form_content.html')

@app.route('/upload', methods=['POST'])
def page_upload():
  picture = request.files.get("picture")

  # Получаем имя файла у загруженного файла
  filename = picture.filename

  # Сохраняем картинку под родным именем в папку uploads
  picture.save(f"./uploads/{filename}")


  return f"Загружен и сохранен файл"

@app.route('/post', methods=['POST'])
def create_post():
    picture = request.files.get('picture')
    content = request.form.get("content")

app.run()