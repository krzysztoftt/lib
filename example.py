#!/usr/bin/python3
import print_lib as p

p.scr_clear()#clear screen

p.put_char(10, 5, "WITAJ",p.color.BLUE)#print WITAJ 10 clolumns 5 line color blue

p.center_text("Hello World", p.style.BOLD + p.color.REDBG)#print center console text style bold color background red

p.put_char(12, 8 , "Hello World", p.style.END )#print Hello World 12 columns 8 line normal color normal style

print(p.color.YELLOW2)#set color yellow
p.put_char(1, 20, "Hello World")#print 1 column line 20 color yellow


print(p.color.VIOLET2 + p.style.UNDERLINE,"            Hello World          \n")#print color violet style under line

