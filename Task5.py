# На Flask cоздать форму регистрации для пользователя. Форма должна содержать поля: имя, электронная почта,
# пароль (с подтверждением), дата рождения, согласие на обработку персональных данных.
# Валидация должна проверять, что все поля заполнены корректно
# (например, дата рождения должна быть в формате дд.мм.гггг).
# При успешной регистрации пользователь должен быть перенаправлен на страницу подтверждения регистрации.

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        date_of_birth = request.form['date_of_birth']
        agreed = request.form.get('agreed')

        if not (name and email and password and confirm_password and date_of_birth and agreed):
            return 'Пожалуйста, заполните все поля формы'

        if len(date_of_birth) != 10 or date_of_birth[2] != '.' or date_of_birth[5] != '.':
            return 'Пожалуйста, введите дату рождения в формате дд.мм.гггг'

        return redirect('/confirmation')

    return render_template('register5.html')

@app.route('/confirmation')
def confirmation():
    return 'Регистрация выполнена успешно!'

if __name__ == '__main__':
    app.run(debug=True)


