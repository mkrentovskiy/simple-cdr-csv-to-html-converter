#!/usr/bin/env python
import os
import datetime
import config

# stop asterisk
os.system(config.ASTERISK_STOP)

# convert wav to mp3
for root, dirs, files in os.walk(config.WAV_HOME):
	for f in files:
		if f[-3:] == "wav":
			fwav = os.path.join(root, f)
			fmp3 = config.mp3path(config.RESULT_MP3, f[0:-4])
			os.system(config.CONVERT % (fwav, os.path.join(config.RESULT_MP3, fmp3)))
			os.unlink(fwav)

# generate html
csv = file(config.CALL_LIST, "rt").readlines()
d = datetime.date.today()
html = file(config.htmlpath(config.RESULT_HTML, str(d.day), str(d.month), str(d.year)), "wt")
now = str(d.day) + "." + str(d.month) + "." + str(d.year)
config.makehtml(csv, html, now)
os.rename(config.CALL_LIST, config.CALL_LIST + "-" + now)
os.system("chown -R www-data:www-data /var/www/mp3 /var/www/html")

# start asterisk
os.system(config.ASTERISK_START)