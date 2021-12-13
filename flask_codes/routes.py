from flask_codes import app,db
from flask_codes.models import User
from flask import render_template,url_for,redirect,flash,request
from flask_codes.forms import RegisterForm,SearchForm

@app.route('/home',methods=['POST','GET'])
def home():
    form=RegisterForm()
    if form.validate_on_submit():
        user=User(ClientId=form.ClientId.data,ClientName=form.ClientName.data,ClientType=form.ClientType.data,ClientBSI=form.ClientBSI.data,ClientStatus=form.ClientStatus.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Details are added successfully for {form.ClientId.data}',category='success')
        return redirect(url_for('home'))
    return render_template('homepage.html',title='Home Page',form=form)



@app.route('/search',methods=['POST','GET'])
def search():
   
    form=SearchForm()
    if form.validate_on_submit():
        
        user=User.query.filter_by(ClientId=form.ClientId.data).first()
        try:
         if form.ClientId.data==user.ClientId:
           flash(f'Please find the details for Client ID : {form.ClientId.data}',category='success')
           clientids=form.ClientId.data
           clientnames=user.ClientName
           clienttypes=user.ClientType
           clientbsis=user.ClientBSI
           clientstatuss=user.ClientStatus
           #print(clientids)
           #print(clientnames)
           #print(clienttypes)
           #print(clientbsis)
           #print(clientstatuss)
           
    
        
           return redirect(url_for('search_result',clientids=clientids,clientnames=clientnames,clienttypes=clienttypes,clientbsis=clientbsis,clientstatuss=clientstatuss))
        except:
            flash(f'Invalid ID: {form.ClientId.data}.Please search for the valid ID',category='danger')
            return redirect(url_for('search'))
    return render_template('search.html',title='Search Page',form=form)

@app.route('/search_result/<clientids>/<clientnames>/<clienttypes>/<clientbsis>/<clientstatuss>')
def search_result(clientids,clientnames,clienttypes,clientbsis,clientstatuss):
    print(clientids)
    print(clientnames)
    print(clienttypes)
    print(clientbsis)
    print(clientstatuss)
    
    return render_template('search_result.html',title='Result Page',clientids=clientids,clientnames=clientnames,clienttypes=clienttypes,clientbsis=clientbsis,clientstatuss=clientstatuss)

@app.route('/')
def main_page():
    return render_template('main_page.html',title='ELF Page')

@app.route('/all_tskl')
def all_tskl():
    details=User.query.all()
    return render_template('all_tskl.html',title='Tasklist Page',details=details)