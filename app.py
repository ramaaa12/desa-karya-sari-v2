from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Ganti dengan secret key Anda

# Konfigurasi Gmail
EMAIL_ADDRESS = "your_gmail@gmail.com"  # Ganti dengan alamat Gmail Anda
EMAIL_PASSWORD = "your_gmail_password"  # Ganti dengan password Gmail Anda

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profil")
def profil():
    return render_template("profil.html")

@app.route("/profil_en")
def profil_en():
    return render_template("profil_en.html")

@app.route("/atraksi")
def atraksi():
    return render_template("atraksi.html")

@app.route("/galeri")
def galeri():
    return render_template("galeri.html")

@app.route("/kontak", methods=["GET", "POST"])
def kontak():
    if request.method == "POST":
        return render_template("kontak.html", success=True)
    return render_template("kontak.html")

@app.route("/kirim-pesan", methods=["POST"])
def kirim_pesan():
    if request.method == "POST":
        # Ambil data dari formulir
        nama = request.form["nama"]
        email = request.form["email"]
        pesan = request.form["pesan"]

        # Buat email
        subject = f"Pesan dari {nama} melalui Formulir Kontak"
        body = f"Nama: {nama}\nEmail: {email}\n\nPesan:\n{pesan}"

        # Kirim email
        try:
            msg = MIMEMultipart()
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = "yunuswahyu45@gmail.com"  # Email tujuan
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Menggunakan variabel yang benar
                server.send_message(msg)

            flash("Pesan berhasil dikirim!", "success")
        except Exception as e:
            flash(f"Terjadi kesalahan: {e}", "danger")

        return redirect("/kontak")

@app.route("/en")
def index_en():
    return render_template("index_en.html")

@app.route("/tentang_desa")
def tentang_desa():
    return render_template("tentang_desa.html")

@app.route("/aktivitas_wisata")
def aktivitas_wisata():
    return render_template("aktivitas_wisata.html")

@app.route("/pelestarian_budaya")
def pelestarian_budaya():
    return render_template("pelestarian_budaya.html")

@app.route("/atraksi_en")
def atraksi_en():
    return render_template("atraksi_en.html")

@app.route("/galeri_en")
def galeri_en():
    return render_template("galeri_en.html")

@app.route("/kontak_en", methods=["GET", "POST"])
def kontak_en():
    if request.method == "POST":
        return render_template("kontak_en.html", success=True)
    return render_template("kontak_en.html")

@app.route("/tentang_desa_en")
def tentang_desa_en():
    return render_template("tentang_desa_en.html")

@app.route("/aktivitas_wisata_en")
def aktivitas_wisata_en():
    return render_template("aktivitas_wisata_en.html")

@app.route("/pelestarian_budaya_en")
def pelestarian_budaya_en():
    return render_template("pelestarian_budaya_en.html")

# Versi Bahasa Jepang
@app.route("/index_jp")
def index_jp():
    return render_template("index_jp.html")

@app.route("/profil_jp")
def profil_jp():
    return render_template("profil_jp.html")

@app.route("/kontak_jp", methods=["GET", "POST"])
def kontak_jp():
    if request.method == "POST":
        return render_template("kontak_jp.html", success=True)
    return render_template("kontak_jp.html")

@app.route("/tentang_desa_jp")
def tentang_desa_jp():
    return render_template("tentang_desa_jp.html")

@app.route("/aktivitas_wisata_jp")
def aktivitas_wisata_jp():
    return render_template("aktivitas_wisata_jp.html")

@app.route("/pelestarian_budaya_jp")
def pelestarian_budaya_jp():
    return render_template("pelestarian_budaya_jp.html")

@app.route("/atraksi_jp")
def atraksi_jp():
    return render_template("atraksi_jp.html")

@app.route("/galeri_jp")
def galeri_jp():
    return render_template("galeri_jp.html")

if __name__ == "__main__":
    app.run(debug=True)