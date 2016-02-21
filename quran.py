from flask import Flask
app = Flask(__name__)

@app.route('/surah/<int:surahnumber>')
def surah(surahnumber):
    if surahnumber== 36:
        print ":)"
    else:
        print ":("

if __name__ == '__main__':
    app.run(host='0.0.0.0')