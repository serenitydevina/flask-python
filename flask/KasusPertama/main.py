from flask import Flask, redirect, url_for

app = Flask(__name__)


#router admin
@app.route('/admin')
def admin():
    return "Halo Admin"

#router tamu dengan parameter orang
@app.route('/guest/<guest>')
def guest(guest):
    return "Halo {} as Guest" .format(guest)

#membuat router untuk mengalihkan router lain

@app.route('/user/<user>')
def user_route(user):
    if user =="admin":
        return redirect(url_for("admin")) #parameter fungsi admin
    else:
        return redirect(url_for("guest", guest= user)) #parameter fungsi guest

if __name__== '__main__':
    app.run(debug=True)