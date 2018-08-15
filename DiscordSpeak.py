# Cat's DiscordSpeak tool
# version 1.0.0

from tkinter import *
import pyperclip

root = Tk()
root.title('DiscordSpeak')
discordSpeak = ''

def translate():
	# Get ready for some ugly ass code
	plainText = plainTextEnt.get()
	listText = list(plainText)
	global discordSpeakLab
	discordSpeak = ''
	for i in listText:
		if i.lower() == 'a':
			discordSpeak += ':regional_indicator_a:'
		elif i.lower() == 'b':
			discordSpeak += ':regional_indicator_b:'
		elif i.lower() == 'c':
			discordSpeak += ':regional_indicator_c:'
		elif i.lower() == 'd':
			discordSpeak += ':regional_indicator_d:'
		elif i.lower() == 'e':
			discordSpeak += ':regional_indicator_e:'
		elif i.lower() == 'f':
			discordSpeak += ':regional_indicator_f:'
		elif i.lower() == 'g':
			discordSpeak += ':regional_indicator_g:'
		elif i.lower() == 'h':
			discordSpeak += ':regional_indicator_h:'
		elif i.lower() == 'i':
			discordSpeak += ':regional_indicator_i:'
		elif i.lower() == 'j':
			discordSpeak += ':regional_indicator_j:'
		elif i.lower() == 'k':
			discordSpeak += ':regional_indicator_k:'
		elif i.lower() == 'l':
			discordSpeak += ':regional_indicator_l:'
		elif i.lower() == 'm':
			discordSpeak += ':regional_indicator_m:'
		elif i.lower() == 'n':
			discordSpeak += ':regional_indicator_n:'
		elif i.lower() == 'o':
			discordSpeak += ':regional_indicator_o:'
		elif i.lower() == 'p':
			discordSpeak += ':regional_indicator_p:'
		elif i.lower() == 'q':
			discordSpeak += ':regional_indicator_q:'
		elif i.lower() == 'r':
			discordSpeak += ':regional_indicator_r:'
		elif i.lower() == 's':
			discordSpeak += ':regional_indicator_s:'
		elif i.lower() == 't':
			discordSpeak += ':regional_indicator_t:'
		elif i.lower() == 'u':
			discordSpeak += ':regional_indicator_u:'
		elif i.lower() == 'v':
			discordSpeak += ':regional_indicator_v:'
		elif i.lower() == 'w':
			discordSpeak += ':regional_indicator_w:'
		elif i.lower() == 'x':
			discordSpeak += ':regional_indicator_x:'
		elif i.lower() == 'y':
			discordSpeak += ':regional_indicator_y:'
		elif i.lower() == 'z':
			discordSpeak += ':regional_indicator_z:'
		elif i.lower() == '1':
			discordSpeak += ':one:'
		elif i.lower() == '2':
			discordSpeak += ':two:'
		elif i.lower() == '3':
			discordSpeak += ':three:'
		elif i.lower() == '4':
			discordSpeak += ':four:'
		elif i.lower() == '5':
			discordSpeak += ':five:'
		elif i.lower() == '6':
			discordSpeak += ':six:'
		elif i.lower() == '7':
			discordSpeak += ':seven:'
		elif i.lower() == '8':
			discordSpeak += ':eight:'
		elif i.lower() == '9':
			discordSpeak += ':nine:'
		elif i.lower() == '0':
			discordSpeak += ':zero:'
		elif i.lower() == '!':
			discordSpeak += ':exclamation:'
		elif i.lower() == '?':
			discordSpeak += ':question:'
		elif i.lower() == ' ':
			discordSpeak += ' '
		else:
			discordSpeak += i
		discordSpeak += ' '
	print(discordSpeak)
	discordSpeakLab.config(text = discordSpeak)
	pyperclip.copy(discordSpeak)
	global copyNoti
	copyNoti = Label(text = 'Copyed to clipboard!')
	copyNoti.grid(row = 3)

plainTextEnt = Entry(root, width = 75)
plainTextEnt.grid(row=0)

traB = Button(root, text="Translate", command=translate)
traB.grid(row=1)

discordSpeakLab = Label(text = '', wraplength=500, justify = CENTER)
discordSpeakLab.grid(row = 2)

root.mainloop()