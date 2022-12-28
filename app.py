from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Мурат')
            #('<a href="/">Главная</a> | <a href="/about">О сервисе</a> | <a href="/contact">Контакты</a>')


@app.route('/about')
def about():
    return (' '.join([str(2**x) for x in range(1,11)]))
        #('Пока не знаю о чем')


@app.route('/contact')
def contact():
    return('Вебмастер' + i)


if __name__ == '__main__':
    app.run(debug=True)