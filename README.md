# Denise Jade Inson — Midterm Portfolio

A personal portfolio website built with Django for my 3rd Year BSIT Midterm requirement at Negros Oriental State University.

## About

This portfolio showcases my graphics design work and academic background. It was built using Django and Python.

## Pages

- **Home** — Introduction, about me, skills, education, and contact
- **Portfolio** — Graphics design projects with image viewer

## Projects Featured

- Newspaper Layout — Adobe InDesign
- Logo Design — Adobe Illustrator
- Flyers Design — Adobe Photoshop
- Logo Design — Adobe Photoshop
- Poster Design — Canva

## Tech Stack

- Python
- Django
- HTML / CSS / JavaScript

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/DeniseJadeInson18/mydjangoPortfolio.git
cd mydjangoPortfolio
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv

# Windows
.venv\Scripts\Activate.ps1

# Mac/Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the development server**
```bash
python manage.py runserver
```

**5. Open in browser**
```
http://127.0.0.1:8000/
```

## Folder Structure

```
mydjangoPortfolio/
├── myportfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── midtermportfolio/
│   ├── static/
│   │   └── midtermportfolio/
│   │       └── imgs/
│   ├── templates/
│   │   └── midtermportfolio/
│   │       ├── base.html
│   │       ├── index.html
│   │       └── portfolio.html
│   ├── views.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

## Author

**Denise Jade Inson**  
3rd Year — BS Information Technology  
Negros Oriental State University  
GitHub: [DeniseJadeInson18](https://github.com/DeniseJadeInson18)
