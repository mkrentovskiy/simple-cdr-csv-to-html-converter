import os

ASTERISK_START = "asterisk"
ASTERISK_STOP = "killall asterisk"

CALL_LIST = "/var/log/asterisk/cdr-csv/Master.csv"
WAV_HOME = "/var/spool/asterisk/logs"
PATTERN = "/var/www/bin/_p.html"

RESULT_HTML = "/var/www/html"
RESULT_MP3 = "/var/www/mp3"

CONVERT = "lame -V2 --quiet %s %s"

def mdir(p):
        try: os.mkdir(p)
        except BaseException: pass

def mp3path(r, s):
        if s[-2:-1] != ".":
                mdir(os.path.join(r, s[-2:-1]))
		mdir(os.path.join(r, s[-2:-1], s[-1:]))
                return os.path.join(s[-2:-1], s[-1:], s + ".mp3")
        else:
                mdir(os.path.join(r, s[-1:]))
                return os.path.join(s[-1:], s + ".mp3")

def htmlpath(r, d, m, y):
	mdir(os.path.join(r, y))
	mdir(os.path.join(r, y, m))
	return os.path.join(r, y, m, d + ".html")

def makehtml(csv, html, now):
	p = file(PATTERN).readlines()
	cs = ""
	for call in csv:
		try:
			s = call.split(",")
			cs += "<tr>"
			# time
			cs += "<td>" + s[9].strip("\"") + "<div class='label'>" + s[11].strip("\"") + "</div></td>"
			# from
			if len(s[1].strip("\"")) > 0: cs += "<td class='phone'>" + s[1].strip("\"") + "</td>"
			else: cs += "<td>-</td>"
			# to
			if len(s[2].strip("\"")) > 0: cs += "<td class='phone'>" + s[2].strip("\"") + "</td>"
			else: cs += "<td>-</td>"
			# record
			if len(s[16].strip("\"")) > 0:
				mp3 = mp3path(RESULT_MP3, s[16].strip("\""))
				if os.path.isfile(os.path.join(RESULT_MP3, mp3)):
					cs += "<td class='c'><a href='/mp3/" + mp3 + "' rel='audio'><img src='/i/r.png' alt='Record'/></a></td>"
				else:
					cs += "<td>-</td>"
			else: cs += "<td>-</td>"
			# tech
			cs += "<td><div class='sm'>" + s[5].strip("\"") + "<br/>" + s[6].strip("\"") + "<br/>" + s[8].strip("\"") +"</div></td></tr>"
		except BaseException: pass
	for i in p:
		html.write(i.replace("_NOW_", now).replace("_CS_", cs))
		
