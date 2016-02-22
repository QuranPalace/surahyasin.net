#-*- coding: utf-8 -*-
import glob,re,codecs

from flask import Flask,url_for
app = Flask(__name__)


def getTranslations(surahnumber):
	result = {}
	for f in glob.glob('data\\translation\\*.txt'):
		translator = f.split("\\")[-1].split(".")[-2]
		result[translator] = []
		for l in codecs.open(f,'r','utf-8'):
			if l.startswith("#") or len(l.strip())==0:continue
			try:
				sure,aye = l.split("|")[:2]
				if int(sure)==surahnumber:
					result[translator].append(u"".join(l.split("|")[2:]))				
			except:
				print l
				raise Exception()
	return result

@app.route('/surah/<int:surahnumber>')
def surah(surahnumber):
	translations = getTranslations(surahnumber)
	result = u"<center>\n"
	if surahnumber not in [1,40]:
		result += "<img width=80% src=\""+url_for("static",filename="ayatimages/besm.png")+"\"/></br>"
	x = re.compile(r'static\\ayatimages\\%d_([0-9]*).png'%surahnumber)
	print glob.glob('static\\ayatimages\\%d_*.png'%surahnumber)
	ayat = sorted([ (int(x.search(f).group(1)),f) for f in glob.glob('static\\ayatimages\\%d_*.png'%surahnumber) ], key=lambda t:t[0])
	for a in ayat:
		result += "<img width=80% src=\""+url_for("static",filename="ayatimages/%d_%d.png"%(surahnumber,a[0]))+"\"/></br>\n"
		for translator in translations:
			try:
				result += u"<p>%s:%s</p>"%(translator,translations[translator][a[0]-1])
			except:
				pass
				#print translations[translator]
	result +="</center>"
	return result


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)