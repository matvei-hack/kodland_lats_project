# 🌍 ClimateHero — Learn About Global Warming and Help the Planet!

## What is this site?

ClimateHero is a website where students and everyone else can learn about global warming and get a list of actions picked specifically for their age.

---

## How to run it?

### Step 1 — Install the libraries

Open the terminal and type:

```
pip install flask flask-login flask-sqlalchemy werkzeug
```

### Step 2 — Start the site

```
python app.py
```

### Step 3 — Open your browser

```
http://localhost:5000
```

---

## File structure

```
climatehero/
├── app.py              main file, run this one
├── README.md           this file
├── templates/
│   ├── base.html       header and footer
│   ├── index.html      home page
│   ├── register.html   registration page
│   ├── login.html      login page
│   └── dashboard.html  tips by age
└── climate.db          database (created automatically)
```

---

## How does it work?

- You register and enter your date of birth
- All data is saved to the database
- Password is stored encrypted — nobody can see it
- After logging in the site calculates your age and shows tips

---

## Tips by age

| Age | Group |
|-----|-------|
| under 10 | simple home habits |
| 11–14 | school and home activities |
| 15–17 | activism and conscious choices |
| 18–25 | student and civic actions |
| 26–60 | work and family steps |
| 60+ | sharing wisdom and experience |

---

## Technologies

| Library | Purpose |
|---------|---------|
| Flask | runs the website |
| Flask-Login | handles login and logout |
| Flask-SQLAlchemy | works with the database |
| Werkzeug | encrypts passwords |
| SQLite | the database itself |

---

*Made with care for our planet 💚*
