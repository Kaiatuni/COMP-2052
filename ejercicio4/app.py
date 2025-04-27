from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, length

app = Flask(__name__)
app.config['SECRET_KEY'] = "mi_clave_secreta"

class LoginForm(FlaskForm):
    username = StringField("Username",  # definir input box para el username
                           validators=[DataRequired(), length(min=3)],
                           render_kw={"placeholder": "Your email"})
    password = PasswordField("Password",  # definir input box para el password
                           validators=[DataRequired()],
                           render_kw={"placeholder": "Your password"})
    submit = SubmitField("Login",  # definir el botón de submit
                           render_kw={"class": "btn btn-primary"})  # aplicar clases de CSS
    email = EmailField("Email",  # definir input box para el email
                         validators=[DataRequired()],
                         render_kw={"placeholder": "Your email ejemplo@gmail.com"})

@app.route("/", methods=["GET", "POST"])
def index():
    form = LoginForm()  # Define las reglas de validación
    if form.validate_on_submit():  # Validar los datos entrados contra las reglas
        # If the form is submitted successfully, redirect to the login route
        return redirect(url_for('login'))
    return render_template("index.html.jinja2", form=form)  # Pass the form to the template

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()  # Define las reglas de validación
    if form.validate_on_submit():  # Validar los datos entrados contra las reglas
        message = f"Usuario: {form.username.data}"
        return render_template("home.html", message=message)
    # If the form is not submitted or validation fails, re-render the login page
    return render_template("index.html.jinja2", form=form)

if __name__ == "__main__":
    app.run(debug=True)