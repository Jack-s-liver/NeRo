from flask import Flask, render_template, url_for
#from flask_sqlalchemy import SQLAlchemy


#render_template - функция

app = Flask(__name__)  # app - создаем экземпляр класса Flask, для которого
app.config['SQLALCHEMY_DATABASE_URI'] =''  # обращаемся к словарю config, находим элемент по индексу в []


# основным файлом является текущий файл, директива __name__ - имя текущего файла

# @app - декоратор
# route - функция, которой сообщаем, какой url отслеживаем
# '/' - главная страница

@app.route('/')
@app.route('/home')
@app.route('/learn')
def index():
    return render_template("learn.html")


@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return "user name: " + name + " - " + str(id)

# если название текущего файла - main, т.е.
# если этот файл - основной файл для запуска (запускаем программу через этот файл), то
if __name__ == "__main__":
    app.run(debug=True)  # запустит лок.сервер
    # debug=true - выводить все ошибки на странице (оставляем true на время написания)
