from flask import Flask, render_template, request

app = Flask(__name__)

# Список для хранения данных пользователей
user_data_list = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Добавление новых данных в список
        user_data_list.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})

    return render_template('index.html', user_data_list=user_data_list)


if __name__ == '__main__':
    app.run(debug=True)
