

from os import name
from flask import Flask, redirect, url_for


app=Flask(__name__)

@app.route('/admin')
def admin():
    return 'this is admin'

@app.route('/university')
def admin():
    return 'this is university'

@app.route('/staff')
def admin():
    return 'this is staff'

@app.route('/students')
def admin():
    return 'this is students'


@app.route('/user<name>')
def shine():
    if name=='admin':
        return redirect(url_for('admin'))
    
    # return 'please try'
    if name=='university':
        return redirect(url_for('university'))
    if name=='students':
        return redirect(url_for('students'))
    if name=='staff':
        return redirect(url_for('staff'))





if __name__=='__main__':
    app.run()