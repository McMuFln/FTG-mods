from telethon import events
from .. import loader, utils
import os
import requests
from PIL import Image,ImageFont,ImageDraw
import re
import io
from textwrap import wrap

def register(cb):
	cb(AverageMod())

class AverageMod(loader.Module):
	"""Любителизатор"""
	strings = {
		'name': 'Любителизатор',
		'usage': 'Напиши <code>.help Любителизатор</code>',
	}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._client = client

	async def avgcmd(self, message):
		""".avg <реплай на сообщение/свой текст>"""

		ufr = requests.get("https://github.com/LaciaMemeFrame/FTG-Modules/blob/master/open-sans.ttf?raw=true")
		f = ufr.content

		pic = requests.get("https://raw.githubusercontent.com/McMuFln/FTG-mods/main/enjoyer.png")
		await message.edit(f"<b>Извиняюсь...</b>")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")

		W, H = img.size
		text = message.text
		tf = text[text.find(" ")+1:text.find("&")]
		tf = "Average\n"+"\n".join(wrap(tf, 29))+"\nFan"
		ts = text[text.find("&")+5:len(text)]
		ts = "Average\n"+"\n".join(wrap(ts, 29))+"\nenjoyer"
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 24, encoding='UTF-8')
		w, h = draw.textsize(ts, font=font)
		imtext = Image.new("RGBA", (W+10, H+1), (0, 0,0,0))
		draw = ImageDraw.Draw(imtext)
		draw.text((10, 1),tf,(0,0,0),font=font, align='left')
		draw.text((360, 1),ts,(0,0,0),font=font, align='left')
		imtext.thumbnail((680, 501))
		img.paste(imtext, (10,7), imtext)
		out = io.BytesIO()
		out.name = "enjoyer.jpg"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out)
		await message.delete()
