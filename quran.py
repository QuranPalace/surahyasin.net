#-*- coding: utf-8 -*-
import glob,re

from flask import Flask,url_for
app = Flask(__name__)

@app.route('/surah/<int:surahnumber>')
def surah(surahnumber):
	result = u"<center>"
	x = re.compile(r'static\\ayatimages\\%d_([0-9]*).png'%surahnumber)
	print glob.glob('static\\ayatimages\\%d_*.png'%surahnumber)
	ayat = sorted([ (int(x.search(f).group(1)),f) for f in glob.glob('static\\ayatimages\\%d_*.png'%surahnumber) ], key=lambda t:t[0])
	for a in ayat:
		result += "<img width=80% src=\""+url_for("static",filename="ayatimages/%d_%d.png"%(surahnumber,a[0]))+"\"/></br>\n"
	result +="</center>"
	return result


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)