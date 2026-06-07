# kodland_lats_project
#russian
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🌍 ClimateHero — Узнай о глобальном потеплении и помоги планете!
Что это за сайт?
ClimateHero — это сайт, где школьники и все желающие могут:

Узнать, что такое глобальное потепление простым языком
Зарегистрироваться и создать личный профиль
Получить список конкретных действий по борьбе с изменением климата — подобранных именно под твой возраст


Как запустить у себя?
Что нужно установить

Python 3.8 или новее
pip (менеджер пакетов Python, обычно идёт вместе с Python)

Шаги запуска

Скачай проект (или распакуй архив в удобную папку)
Установи зависимости — открой терминал в папке проекта и напиши:

   pip install flask flask-login flask-sqlalchemy werkzeug

Запусти сайт:

   python app.py

Открой браузер и перейди по адресу:

   http://localhost:5000
Готово! Сайт работает на твоём компьютере 🎉

Структура файлов
climatehero/
│
├── app.py              ← главный файл, запускай его
├── README.md           ← этот файл
│
├── templates/          ← HTML-страницы сайта
│   ├── base.html       ← общий шаблон (шапка, футер)
│   ├── index.html      ← главная страница
│   ├── register.html   ← страница регистрации
│   ├── login.html      ← страница входа
│   └── dashboard.html  ← личный кабинет с советами
│
└── climate.db          ← база данных (создаётся автоматически)

Как это работает?

Регистрация — пользователь вводит имя, email, пароль и дату рождения
База данных — все данные сохраняются в файл climate.db (SQLite — не нужно ничего дополнительно устанавливать)
Личный кабинет — после входа система считает возраст и выдаёт персональный список действий:

До 10 лет — простые домашние привычки
11–14 лет — школьные и домашние активности
15–17 лет — активизм, осознанные выборы
18–25 лет — студенческие и гражданские действия
26–60 лет — профессиональные и семейные шаги
60+ лет — передача опыта и мудрости




Технологии
ТехнологияДля чегоPython + FlaskВеб-сервер и логика сайтаSQLiteБаза данных (хранение пользователей)Flask-LoginАвторизация и сессииFlask-SQLAlchemyРабота с базой данныхHTML + CSSВнешний вид сайта

Часто задаваемые вопросы
❓ Где хранятся пароли?
Пароли никогда не хранятся в открытом виде — только зашифрованная версия (хеш).
❓ Можно ли использовать сайт в интернете?
В текущем виде сайт работает только локально. Для публикации в интернет потребуется хостинг (например, Railway, Render, PythonAnywhere — все бесплатные варианты).
❓ Как удалить все данные и начать заново?
Просто удали файл climate.db — при следующем запуске он создастся заново пустым.

Сделано с заботой о нашей планете 💚 #матвейлучшевсех 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#eanglish
🌍 ClimateHero — Learn about global warming and help the planet!
What is this website?
ClimateHero is a website where schoolchildren and anyone can:

Learn about global warming in simple terms
Register and create a personal profile
Get a list of specific actions to combat climate change tailored specifically for your age

How to launch it?
What you need to install

Python 3.8 or later
pip (Python package manager, usually included with Python)

Installation steps

Download the project (or unzip the archive to a convenient folder)
Install dependencies - open a terminal in the project folder and type:

pip install flask flask-login flask-sqlalchemy werkzeug

Launch the website:

python app.py

Open a browser and go to:

http://localhost:5000
Done! The website is running on your computer 🎉

File Structure
climatehero/
│
├── app.py ← main file, run it
├── README.md ← this file
│
├── templates/ ← HTML pages of the site
│ ├── base.html ← general template (header, footer)
│ ├── index.html ← home page
│ ├── register.html ← registration page
│ ├── login.html ← login page
│ └── dashboard.html ← personal account with tips
│
└── climate.db ← database (created automatically)

How it works Is it working?

Registration - the user enters their name, email, password, and date of birth.
Database - all data is saved in the climate.db file (SQLite - no additional installation required).
Personal Account - after logging in, the system calculates your age and provides a personalized action list:

Under 10 — Simple household habits
11–14 years — School and home activities
15–17 years — activism, conscious choices
18–25 years — Student and civic engagement
26–60 years — Professional and family steps
60+ years — Sharing experience and wisdom

Technology Technology What it's for: Python + Flask Web server and website logic SQLite Database (user storage) Flask-Login Authorization and sessions Flask-SQLAlchemy Database management HTML + CSS Website appearance

Frequently Asked Questions
❓ Where are passwords stored?
Passwords are never stored in cleartext—only an encrypted version (hash).
❓ Can the site be used online?
In its current form, the site only works locally. Publishing online requires hosting (for example, Railway, Render, PythonAnywhere—all free options).
❓ How do I delete all data and start over?
Simply delete the climate.db file—it will be recreated empty the next time I launch it.

Made with care for our planet 💚 #matveyisbetterthanever




