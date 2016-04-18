#!/bin/env python
# -*- coding: utf-8 -*-


import re
from flask import Flask, render_template, request, Response
app = Flask(__name__)


LOGFILE='opencast.log'


class Logline():
	msgtype = None
	msg = None

	def __init__(self, msgtype, msg):
		self.msgtype = msgtype
		self.msg = msg


@app.route('/favicon.ico')
def favicon():
	return '', 404


@app.route("/")
@app.route("/<path:filterval>")
def home(filterval=''):

	filterarr = [x.upper() for x in filterval.split('/') if x]

	with open(LOGFILE) as f:
		log = f.read()

	r = re.compile('^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} \| (TRACE|DEBUG|INFO|WARN|ERROR) * \| \(\S+:\d+\) - .*$')
	logline = []
	level = ''
	logs = []
	for line in log.split('\n'):
		if logline and r.match(line):
			if not filterarr or level in filterarr:
				logs.append(Logline(level, '\n'.join(logline)))
			level = line.split('|')[1].strip()
			logline = []
		logline.append(line)

	#return Response(log, mimetype='text/plain')

	return render_template('home.html', logs=logs, filterarr=filterarr)


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
