import feedparser
from bs4 import BeautifulSoup
import urllib
import json
import telegram
from telegram.error import NetworkError, Unauthorized
import time

tokenTELEGRAM = '312313585:AAGkRhdkDWvpaIgT7mtgkaFdfiSYykq0H_U' #rexFBDbot
tokenREADABILITY = "8fee5accb3776ea3657e6ad92a969805aee9bce8"
tokenTWITTER = ""
chat_id = 31923577
bot = telegram.Bot(tokenTELEGRAM)

prevTitleFormulaPassion=""

def FormulaPassion():
	global tokenREADABILITY
	global prevTitleFormulaPassion
	d = feedparser.parse("http://formulapassion.it/feed")
	title =  d["items"][0]["title"]
	link = d["items"][0]["link"]
	if (title != prevTitleFormulaPassion):
		print title, prevTitleFormulaPassion
		url_read_parser = "https://www.readability.com/api/content/v1/parser?url=" + link + "&token=" + tokenREADABILITY 
		readability = urllib.urlopen(url_read_parser).read()
		niceContent = BeautifulSoup(json.loads(readability).get("content"),"lxml").text.split("RIPRODUZIONE VIETATA anche")[0].rstrip()
		prevTitleFormulaPassion = title
		articolo = "<b>" + title +  "</b>" + "\n" + link + "\n" + niceContent
		print articolo
		return articolo
	else:
		return None
def echo():
	a = FormulaPassion()
	#print "echo ", a
	if a is not None:
		bot.sendMessage(chat_id = chat_id, text = a, disable_web_page_preview=True, parse_mode="Html")

while True:
	try:
		echo()
		time.sleep(10)
	except NetworkError:
		sleep(1)
	except Unauthorized:
		update_id += 1
