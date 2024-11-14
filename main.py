#mengimport modul flask ke dalam proyek
from flask import Flask, redirect,url_for,render_template,request
import os 
import time

#Membuat objek aplikasi flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        pesan = request.form['pesan']
        #tampilkan di terminal
        print(f"Nama: {nama}, Email: {email}, Pesan: {pesan}")
        # return redirect(url_for('contact'))
        # title = 'Content Page'

        #pesan konfirmasi
        pesan_konfirmasi=f"Halo {nama}, data anda berhasil dikirim"
        return render_template('contact.html', nama=nama,email=email,pesan=pesan, pesan_konfirmasi=pesan_konfirmasi)

    return render_template('contact.html');

@app.route('/registrasi', methods=['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        nisn = request.form['nisn']
        nama = request.form['nama']
        email = request.form['email']
        tanggal_lahir = request.form['tanggal_lahir']
        asal_sekolah = request.form['asal_sekolah']
        prodi = request.form['prodi']
        foto = request.form['foto']
        if foto:
            timestamp = str(int(time.time()))
            ext = foto.filename.split('.')[-1]
            unique_filename = f"{timestamp}.{ext}"
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            foto.save(foto_path)
            foto_path = f'uploads/{unique_filename}'
        else:
            foto_path = None
        #tampilkan di terminal
        # print(f"NISN {nisn}, Nama: {nama}, Email: {email}, Tanggal Lahir: {tanggal_lahir}, Asal Sekolah: {asal_sekolah}, Prodi: {prodi}")

        #pesan konfirmasi
        pesan_konfirmasi=f"Halo {nama}, data anda berhasil dikirim"
        return render_template('registrasi.html', nisn=nisn,nama=nama,email=email,tanggal_lahir=tanggal_lahir,asal_sekolah=asal_sekolah,prodi=prodi,foto=foto_path, pesan_konfirmasi=pesan_konfirmasi)
    return render_template('registrasi.html');

# @app.route('/aboutme/<name>')
# def aboutme(name):
#     return 'About me,  its {}'.format(name)

# @app.route('/aboutme/<int:umur>')
# def aboutage(umur):
#     return 'Umur Saya adalah {} tahun'.format(umur)

# @app.route('/ipk/<float:ipk>')
# def aboutipk(ipk):
#     return 'Ipk saya sebesar {}'.format(ipk)


#variabel spesial name akan memiliki nilai main
if __name__ == '__main__':
    #Method run menjalankan aplikasi
    app.run(debug=True)