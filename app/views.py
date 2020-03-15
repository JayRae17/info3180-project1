"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for, flash
from .forms import addProfile 
from flask import session
import datetime
from werkzeug.utils import secure_filename
from app.models import UserProfile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')



def format_date_joined(year,month,day):
    date_joined = datetime.date(year, month, day) # a specific date 
    fdate = date_joined.strftime("%B, %Y") 
    return fdate


@app.route('/profile/' , methods=['GET','POST'])
def profile():
    addprofile = addProfile()

    if request.method == 'POST':
        if addprofile.validate_on_submit():
            fname = addprofile.fname.data
            lname = addprofile.lname.data
            gender = addprofile.gender.data
            email = addprofile.email.data
            location = addprofile.location.data
            bio = addprofile.bio.data
            date = datetime.datetime.now()
            created_on = date.strftime("%B %d, %Y")

            photo = addprofile.photo.data

            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            user = UserProfile(first_name = fname, last_name=lname, gender = gender, email = email, location = location, bio = bio, photo = filename, created_on = created_on)
            db.session.add(user)
            db.session.commit()

            flash('File Uploaded', 'success')
            return redirect(url_for('profiles'))

    flash_errors(addprofile)
    return render_template('profile.html', form=addprofile)


@app.route('/profiles')
def profiles():
    """Render the website's profiles page."""
    return render_template('profiles.html', users = db.session.query(UserProfile).all())



@app.route('/profile/<id>')
def act_profile(id):
    """Render the website's profile page."""
    return render_template("user_profile.html", act = db.session.query(UserProfile).filter_by(id = int(id)).first())
    





###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
