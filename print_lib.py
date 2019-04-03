# a few some useful function

#clear screen
def scr_clear():
	print(chr(27)+'[2j')
	#print('\033c')#alternative
	print('\x1bc')

def put_char(x,y,char,color=''):
	print(color)
	print("\033["+str(y)+";"+str(x)+"H"+char)

#print center text
def center_text(text,color=''):
	import os
	console_size = os.get_terminal_size()
	w = console_size.columns
	h = console_size.lines
	print(color)
	put_char(int(w/2), int(h/2), text)


# color value
class color:

	BLACK  = '\033[30m'
	RED    = '\033[31m'
	GREEN  = '\033[32m'
	YELLOW = '\033[33m'
	BLUE   = '\033[34m'
	VIOLET = '\033[35m'
	BEIGE  = '\033[36m'
	WHITE  = '\033[37m'

	BLACKBG  = '\033[40m'
	REDBG    = '\033[41m'
	GREENBG  = '\033[42m'
	YELLOWBG = '\033[43m'
	BLUEBG   = '\033[44m'
	VIOLETBG = '\033[45m'
	BEIGEBG  = '\033[46m'
	WHITEBG  = '\033[47m'

	GREY    = '\033[90m'
	RED2    = '\033[91m'
	GREEN2  = '\033[92m'
	YELLOW2 = '\033[93m'
	BLUE2   = '\033[94m'
	VIOLET2 = '\033[95m'
	BEIGE2  = '\033[96m'
	WHITE2  = '\033[97m'

	GREYBG    = '\033[100m'
	REDBG2    = '\033[101m'
	GREENBG2  = '\033[102m'
	YELLOWBG2 = '\033[103m'
	BLUEBG2   = '\033[104m'
	VIOLETBG2 = '\033[105m'
	BEIGEBG2  = '\033[106m'
	WHITEBG2  = '\033[107m'
	    
#style value
class style:

	END = '\033[0m'
	BOLD     = '\033[1m'
	ITALIC   = '\033[3m'
	BLINK    = '\033[5m'
	BLINK2   = '\033[6m'
	SELECTED = '\033[7m'
	UNDERLINE = '\033[4m'
