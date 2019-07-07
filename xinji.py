from struct import *
from enum import Enum

class ScreenOrienatation(Enum):
	UNKNOWN = -1
	ALBUM = 0
	PORTRAIT = 1

class FontWeight(Enum):
	UNKNOWN = 0
	COMMON = 0x190
	BOLD = 0x2BC
	
class FontStyle(Enum):
	UNKNOWN = -1
	COMMON = 0
	ITALIC = 0xFF
	
class FontCharset(Enum):
	UNKNOWN = -1
	ANSI = 0
	DEFAULT = 1
	SYMBOL = 2
	ARABIC = 0xB2
	CYRILIC = 0xCC
	EASTEUROPE = 238
	SHIFTJIS = 0x80
	HANGEUL = 129
	GB2312 = 134
	CHINESEBIG5 = 136
	OEM = 255
	JOHAB = 130
	HEBREW = 177
	GREEK = 161
	TURKISH = 162
	VIETNAMESE = 163
	THAI = 222
	MAC = 77
	BALTIC = 186
	
class PrinterDPI(Enum):
	UNKNOWN = -1
	DPI24 = 0
	DPI8 = 1
	
class PrinterHor(Enum):
	UNKNOWN = -1
	LEFT2RIGHT = 0
	RIGHT2LEFT = 1
	
class PrinterVer(Enum):
	UNKNOWN = -1
	TOP2DOWN = 0
	DOWN2TOP = 1

def sb(v):
	return unpack("<b", v[:1])[0]

def rb(v):
	return unpack("<B", v[:1])[0]
	
def rw(v):
	return unpack("<H", v[:2])[0]

def sd(v):
	return unpack("<i", v[:4])[0]

def rd(v):
	return unpack("<I", v[:4])[0]
	
class stringXinji():
	signature = b"\xff\xfe\xff"
	length = 0
	count_bytes = 0
	content = ""
	def __init__(self, data):
		if data[0:3] == self.signature:
			self.length = rb(data[3:4])
			self.count_bytes = self.length*2 + 4
			self.content = data[4:4+self.length*2].decode("utf-16-le")
		else:
			print(data[0:3])

	def __str__(self):
		return self.content
	
	def __repr__(self):
		return self.content

class headerXinji():
	signature = b"xinje_display_file"
	version = ""
	hash = 0
	modify_time = ""
	def __init__(self, data):
		if data[0:18] == self.signature:
			self.version = data[0x19:0x1f]
			self.hash =	rd(data[0x24:0x28])
			self.modify_time = data[0x44:0x70].decode("utf-16-le")
		else:
			print(data[0:18])

class structsXinji():
	count = 0;
	def __init__(self, data):
		self.count = rd(data[0:4])
		
class settingsXinji():
	name_project = "UNKNOWN";
	type_panel = "UNKNOWN"
	subtype_panel = "UNKNOWN"
	screen_orientation = ScreenOrienatation(-1)
	start_screen = -1
	password1 = -1
	password2 = -1
	password3 = -1
	password4 = -1
	password5 = -1
	password6 = -1
	password7 = -1
	password8 = -1
	password9 = -1
	screensave_interval = -1
	screensave = -1
	author = "UNKNOWN"
	description = "UNKNOWN"
	size_font = -1;
	color_font = -1;
	weight_font = FontWeight(0);
	style_font = FontStyle(-1);
	underlined = -1;
	crossed_out = -1;
	charset = FontCharset(-1);
	family_font = "UNKNOWN";
	printer_dpi = PrinterDPI(-1)
	printer_ver = PrinterVer(-1)
	printer_hor = PrinterHor(-1)
	timeout = -1;
	def __init__(self, data):
		self.name_project = stringXinji(data[0:])
		shift = self.name_project.count_bytes
		
		self.type_panel = stringXinji(data[shift:])
		shift += self.type_panel.count_bytes
		
		self.subtype_panel = stringXinji(data[shift:])
		shift += self.subtype_panel.count_bytes
		
		self.screen_orientation = ScreenOrienatation(rd(data[shift:shift+4]))
		shift += 4
		
		self.start_screen = sd(data[shift:shift+4])
		shift += 4
		
		self.password1 = rd(data[shift:shift+4])
		shift += 4
		
		self.password2 = rd(data[shift:shift+4])
		shift += 4
		
		self.password3 = rd(data[shift:shift+4])
		shift += 4
		
		self.password4 = rd(data[shift:shift+4])
		shift += 4
		
		self.password5 = rd(data[shift:shift+4])
		shift += 4
		
		self.password6 = rd(data[shift:shift+4])
		shift += 4
		
		self.password7 = rd(data[shift:shift+4])
		shift += 4
		
		self.password8 = rd(data[shift:shift+4])
		shift += 4
		
		self.password9 = rd(data[shift:shift+4])
		shift += 8
		
		self.screensave_interval = rb(data[shift:shift+1])
		shift += 2
		
		self.screensave = rw(data[shift:shift+2])
		shift += 10
		
		self.author = stringXinji(data[shift:])
		shift += self.author.count_bytes
		
		self.description = stringXinji(data[shift:])
		shift += self.description.count_bytes + 20
		
		self.size_font = round(sb(data[shift:shift+1]) * -0.75)
		shift += 16
		
		self.weight_font = FontWeight(rw(data[shift:shift+2]))
		shift += 4
		
		self.style_font = FontStyle(rb(data[shift:shift+1]))
		shift += 1
		
		self.underlined = rb(data[shift:shift+1])
		shift += 1
		
		self.crossed_out = rb(data[shift:shift+1])
		shift += 1
		
		self.charset = FontCharset(rb(data[shift:shift+1]))
		shift += 5
		
		self.family_font = data[shift:shift+64].decode("utf-16-le").rstrip("\x00")
		shift += 64
		
		self.printer_dpi = PrinterDPI(rd(data[shift:shift+4]))
		shift += 4
		
		self.printer_ver = PrinterVer(rd(data[shift:shift+4]))
		shift += 4
		
		self.printer_hor = PrinterHor(rd(data[shift:shift+4]))
		shift += 4
		
		self.timeout = sd(data[shift:shift+4])
		shift += 4
		
class page4Xinji():
	name = "";
	def __init__(self, data):
		self.name = stringXinji(data[0:])


with open("C:\\Users\\User\\Documents\\НТЦ\\tests\\before.txp", "rb") as f:
	d = f.read()

header = headerXinji(d[0:0x10004])
structs = structsXinji(d[0x10004:0x10400])
settings = settingsXinji(d[0x10800:0x10c00])
pages4 = []

for i in range(3, structs.count):
	pages4.append(page4Xinji(d[0x10000 + i*0x400:0x10000 + (i+1)*0x400]))

for i in range(0, len(d), 2):
	#print(type(d[i]))
	if rw(d[i:i+2]) != 0:
		pass#print("%8.x %2.x%2.x" % (i, d[i], d[i+1]))
		
print("header=", vars(header))
print("structs=", vars(structs))
print("settings=", vars(settings))
for page4 in pages4:
	print(page4.name)