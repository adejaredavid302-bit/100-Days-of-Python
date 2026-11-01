# Day 61 – Bootstrap-Flask Login Form

##  Project Overview
A Flask login application built with **Flask-WTF** and **Bootstrap-Flask**. It demonstrates how to create and validate forms using WTForms and automatically style them with Bootstrap.

##  Features
- Login form with email and password fields.
- Form validation using WTForms validators.
- Password length validation (8–20 characters).
- CSRF protection.
- Bootstrap styling using Bootstrap-Flask.
- Automatic form rendering with `render_form()`.
- Success page for correct login credentials.
- Access Denied page for incorrect credentials.
- Jinja2 template inheritance using a shared `base.html`.

## ️ Technologies Used
- Python
- Flask
- Flask-WTF
- WTForms
- Bootstrap-Flask
- HTML
- Jinja2

##  Project Structure
```text
Day_61/
│
├── main.py
├── requirements.txt
│
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── success.html
    └── denied.html
```

## ️ How to Run

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   ```

2. Navigate into the project folder:
   ```bash
   cd Day_61
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Open your browser and visit:
   ```text
   http://127.0.0.1:5000/
   ```

##  What I Learned
- How to integrate Bootstrap-Flask with Flask.
- How to use `render_form()` to generate forms from WTForms.
- How to validate user input with WTForms.
- How to use Jinja2 template inheritance.
- How to load Bootstrap CSS and JavaScript.
- How to build a simple login authentication flow with Flask.

---

**100 Days of Python – Day 61 Complete!** 