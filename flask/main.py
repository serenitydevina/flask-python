#mengimport modul flask ke dalam proyek
from flask import Flask, redirect,url_for,render_template

#Membuat objek aplikasi flask
app = Flask(__name__)

#dekorator untuk menentukan URL mana yang diakses
#menentukan route untuk halaman utama
@app.route('/')
#fungsi hello world
def hello_word():
    #ketika '/' diakses maka akan ditampilkan kalimat yang ada di dalam return
    return 'Hello World'

@app.route('/fakultas')
def fakultas():
    fakultas = ['FIKR','FEB'];
    return render_template('fakultas.html',fakultas=fakultas);

@app.route('/prodi')
def prodi():
    prodi = [
        {'nama':'Informatika','fakultas':'FIKR'},
        {'nama': 'Sistem Informasi', 'fakultas':'FIKR'},
        {'nama': 'Akuntasi', 'fakultas':'FEB'},
         ];
    return render_template('prodi.html',prodi=prodi);

@app.route('/contact')
def contact():
    return render_template('contact.html');

@app.route('/aboutme/<name>')
def aboutme(name):
    return 'About me,  its {}'.format(name)

@app.route('/aboutme/<int:umur>')
def aboutage(umur):
    return 'Umur Saya adalah {} tahun'.format(umur)

@app.route('/ipk/<float:ipk>')
def aboutipk(ipk):
    return 'Ipk saya sebesar {}'.format(ipk)


#variabel spesial name akan memiliki nilai main
if __name__ == '__main__':
    #Method run menjalankan aplikasi
    app.run(debug=True)