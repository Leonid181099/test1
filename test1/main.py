# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tinydb import TinyDB
from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime as dt
import re
from waitress import serve
app=Flask(__name__)

def if_date(date):
    try:
        valid_date = dt.strptime(date, '%d.%m.%Y')
    except:
        try:
            valid_date = dt.strptime(date, '%Y-%m-%d')
        except:
            return False
    return True

def if_phone_number(phone):
    return re.fullmatch(r' 7 \d{3} \d{3} \d{2} \d{2}', phone) is not None

def if_email(email):
    return re.fullmatch(r'\w+@\w+\.\w+', email) is not None

def compare_field(field,field1):
    if field=='text':
        return True
    if field=='date' and if_date(field1):
        return True
    if field=='phone' and if_phone_number(field1):
        return True
    if field=='email' and if_email(field1):
        return True
    return False

def make_form(f):
    f_name='f_name'
    f1={}
    it=0
    for i in f:
        it+=1
        if if_date(f[i]):
            f1[f_name+str(it)]='date'
            continue
        if if_phone_number(f[i]):
            f1[f_name+str(it)]='phone'
            continue
        if if_email(f[i]):
            f1[f_name+str(it)]='email'
            continue
        f1[f_name + str(it)] = 'text'
    return f1
def compare_form(form,f):
    it=0
    name=''
    for field_key in form:
        it+=1
        flag=False
        if field_key=='name':
            name=form[field_key]
            continue
        for field1_key in f:
            if (field_key==field1_key) and compare_field(form[field_key],f[field1_key]):
                flag=True
                break
        if not flag:
            return -1,''
    return it,name

def find_form(f,db):
    max=-1
    form=''
    form_name=''
    no_form_flag=True
    for item in db:
        a,name=compare_form(item,f)
        if a>max:
            max=a
            form=item
            form_name=name
            no_form_flag=False
    if no_form_flag:
        form1=make_form(f)
        return form1,'',False
    return form,form_name,True

@app.route('/')
def hello():
    return 'hello'

@app.route('/get_form',methods=['GET', 'POST'])
def hello1():
    if request.method == 'POST':
        f=request.args
        form,name,form_finded=find_form(f,db)
        if form_finded:
            return name
        else:
            return form
    return render_template('get_form.html')

# if __name__ == '__main__':
if True:
    db = TinyDB('db.json')
    # app.run(host='0.0.0.0', port=5000)
    serve(app, host='0.0.0.0', port=5000)




