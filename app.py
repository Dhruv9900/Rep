from flask import Flask, render_template, request
from wtforms import Form, StringField, validators, SelectField

app = Flask(__name__)

class Search(Form):
    acName = StringField("Name", validators=[validators.InputRequired()])
    fName = StringField("Father Name")
    gender = SelectField("Gender", validators=[validators.InputRequired()],choices=[(1,"Male"),(2,"Female"),(3,"Other")])

@app.route('/',methods=["GET","POST"])
def home():
    form =  Search(request.form)
    if request.method == "POST":
        print("Accused=",form.acName.data)
        print("Father Name=",form.fName.data)
        print("Gender:",form.gender.data)
    return render_template("Wtf.html.j2", form=form)

app.run(host='0.0.0.0',port=50100,debug=True) 