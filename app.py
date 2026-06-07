from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'climatehero-secret-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///climate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Войди, чтобы увидеть свои советы!'


#пользователь

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_age(self):
        today = date.today()
        b = self.birthdate
        return today.year - b.year - ((today.month, today.day) < (b.month, b.day))  


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#разделениее по возрасту

def get_tips_by_age(age):
    if age <= 10:
        return {
            "group": "Юный защитник планеты 🌱",
            "subtitle": f"Тебе {age} лет — ты уже можешь изменить мир!",
            "color": "#4ade80",
            "tips": [
                ("🚰", "Закрывай кран, пока чистишь зубы", "Это экономит до 6 литров воды в минуту!"),
                ("💡", "Выключай свет, когда выходишь из комнаты", "Простая привычка сохраняет электроэнергию"),
                ("♻️", "Помогай родителям сортировать мусор", "Раздельный сбор мусора — твоё первое взрослое дело"),
                ("🌳", "Посади дерево вместе с семьёй", "Одно дерево поглощает 20 кг CO₂ в год"),
                ("🥗", "Ешь больше овощей и фруктов", "Растительная еда требует меньше ресурсов для производства"),
                ("🚶", "Ходи пешком в школу, если она близко", "Меньше машин — чище воздух"),
                ("📚", "Расскажи друзьям, что узнал о климате", "Знание — самое мощное оружие!"),
            ]
        }
    elif age <= 14:
        return {
            "group": "Климатический активист 🌿",
            "subtitle": f"Тебе {age} лет — время действовать серьёзно!",
            "color": "#34d399",
            "tips": [
                ("📱", "Не заряжай телефон всю ночь", "Зарядка за 2 часа — лишнее электричество тратится впустую"),
                ("🥤", "Откажись от одноразового пластика", "Купи многоразовую бутылку и стакан"),
                ("🎒", "Организуй в школе акцию по уборке мусора", "Один субботник = чистый район"),
                ("🌡️", "Узнай про углеродный след и посчитай свой", "Поищи калькулятор CO₂ онлайн"),
                ("📖", "Прочитай одну книгу или посмотри документалку о климате", "Знание меняет отношение к миру"),
                ("🛒", "Не бери пакет в магазине", "Возьми тканевую сумку — привычка на всю жизнь"),
                ("🌱", "Вырасти растение дома", "Зелёный уголок дома — вклад в экологию"),
                ("🚲", "Езди на велосипеде вместо машины", "Велосипед = 0 выбросов CO₂"),
            ]
        }
    elif age <= 17:
        return {
            "group": "Молодой лидер перемен 🔥",
            "subtitle": f"Тебе {age} лет — пора становиться голосом поколения!",
            "color": "#fb923c",
            "tips": [
                ("✊", "Присоединись к климатическому движению в своём городе", "Пятницы для будущего, Greenpeace и другие"),
                ("📝", "Напиши петицию в школе об экологии", "Сбор подписей — реальный инструмент давления"),
                ("🌐", "Веди соцсети с экотемой", "Один пост может охватить тысячи людей"),
                ("🥦", "Попробуй один день в неделю без мяса", "Производство мяса — 15% мировых выбросов"),
                ("💸", "Покупай в секонд-хенде", "Производство новой одежды загрязняет воду и воздух"),
                ("🏫", "Предложи школе перейти на экономные лампочки", "LED-лампы потребляют на 80% меньше энергии"),
                ("🧪", "Выбери тему экологии для школьного проекта", "Покажи учителям и одноклассникам реальные данные"),
                ("📊", "Изучи, как голосуют политики по климату", "Молодёжь — будущий электорат"),
            ]
        }
    elif age <= 25:
        return {
            "group": "Студент — агент изменений ⚡",
            "subtitle": f"Тебе {age} лет — у тебя есть энергия и знания!",
            "color": "#60a5fa",
            "tips": [
                ("🎓", "Выбирай специальность, связанную с устойчивым развитием", "Зелёная экономика — будущее рынка труда"),
                ("🏢", "Вступи в экоклуб в университете или создай свой", "Коллективные действия в 10 раз эффективнее"),
                ("🌱", "Перейди на зелёный банк или инвестиции", "Твои деньги не должны финансировать нефтянку"),
                ("🚌", "Используй общественный транспорт вместо такси", "Один автобус = 40 меньше машин на дороге"),
                ("💻", "Участвуй в хакатонах по климатическим технологиям", "Программисты и дизайнеры нужны климату"),
                ("🥗", "Освой веганские или вегетарианские рецепты", "Это вкусно, дёшево и полезно для планеты"),
                ("📣", "Пиши депутатам и в органы власти", "Один email от гражданина — это официальное обращение"),
                ("🌍", "Волонтёрь в экоорганизациях", "Опыт + нетворкинг + реальная польза"),
            ]
        }
    elif age <= 60:
        return {
            "group": "Ответственный взрослый 💼",
            "subtitle": f"Тебе {age} лет — ты влияешь на целое поколение вокруг!",
            "color": "#a78bfa",
            "tips": [
                ("🏠", "Утепли квартиру или дом", "Хорошее утепление снижает расход энергии на 30–40%"),
                ("☀️", "Рассмотри установку солнечных панелей", "В России и СНГ уже есть хорошие субсидии"),
                ("🚗", "При покупке следующей машины рассмотри электро или гибрид", "Выбросы CO₂ — в 5 раз меньше"),
                ("🛒", "Покупай местные продукты на рынке", "Местная еда не летит через полмира"),
                ("💼", "Поднимай климатическую повестку на работе", "ESG-отчётность теперь важна для бизнеса"),
                ("🌱", "Посади сад или участвуй в городском озеленении", "Деревья в городе снижают температуру на 3–5°C"),
                ("🗳️", "Голосуй за кандидатов с зелёной программой", "Политическая воля — ключ к системным изменениям"),
                ("👨‍👩‍👧", "Объясни детям и подросткам важность климата", "Ты — пример для следующего поколения"),
            ]
        }
    else:
        return {
            "group": "Мудрый наставник планеты 🌎",
            "subtitle": f"Тебе {age} лет — твой опыт бесценен!",
            "color": "#f472b6",
            "tips": [
                ("🌳", "Передай традиции бережного отношения к природе", "Расскажи внукам и детям, как жили экологично раньше"),
                ("📖", "Поддержи местные экоинициативы и НКО", "Опыт и связи важнее денег"),
                ("🏡", "Компостируй органические отходы", "Компост = удобрение + меньше мусора на свалке"),
                ("💬", "Участвуй в общественных слушаниях по экологии", "Голос опытного человека весомее"),
                ("📰", "Читай и делись достоверной информацией о климате", "Бороться с фейками — тоже важная работа"),
                ("🤝", "Организуй экособрание в своём доме или дворе", "Сообщества меняют районы"),
                ("🌱", "Вырасти огород — хотя бы на балконе", "Свои овощи = нет упаковки, нет перевозки"),
                ("❤️", "Поддержи молодых климатических активистов", "Твоя поддержка даёт им силы"),
            ]
        }

#пути в разные окна

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        password2 = request.form.get('password2', '')
        birthdate_str = request.form.get('birthdate', '')

        if not all([name, email, password, birthdate_str]):
            flash('заполни все', 'error')
            return render_template('register.html')

        if password != password2:
            flash('Пароли не совпадает', 'error')
            return render_template('register.html')

        if len(password) < 6:
            flash('не кароче 6 символов', 'error')
            return render_template('register.html')

        if User.query.filter_by(email=email).first():
            flash('Этот эмаил уже есть', 'error')
            return render_template('register.html')

        try:
            birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
        except ValueError:
            flash('неверная дата', 'error')
            return render_template('register.html')

        if birthdate >= date.today():
            flash('в будущем не щитаеться тупой', 'error')
            return render_template('register.html')

        user = User(name=name, email=email, birthdate=birthdate)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f'привет, {name}! ', 'success')
        return redirect(url_for('dashboard'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Неверная почта или пароль', 'error')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('пока', 'info')
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    age = current_user.get_age()
    tips_data = get_tips_by_age(age)
    return render_template('dashboard.html', age=age, tips_data=tips_data)


#включить

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
