print('Hello, Rachel')
name='Jane'
if name == 'Ola':
	print('Hey Ola!')
elif name == 'Rachel':
	print('Hola, Rachel!')
else:
	print ('WHO are you?')
volume=19
if volume<20:
	print("I can't hear anything?!")
elif 40<= volume <60:
	print("Perfect Volume")
elif 60 <=volume <80:
	print('Great for a party')
elif 80 <= volume <100:
	print ('TOO LOUD')
else:
	print('SWITCH OFF')
# change the volume if it's too loud or too quiet
if volume <20 or volume >80:
	volume = 50
	print("That's MUCH better!")
def hi():
	print('HELLO THERE')
	print('How are are?')
hi ()
def hi(name):
	if name == 'Jane':
		print('Hola! Jane')
	elif name == 'Sonja':
		print('Hola! Sonja')
	else:
		print('WHO ARE YOU?')
hi('Sonja')
def hi(name):
	print('Bonjour, ' + name + '! Ca va?')
hi("Rachel")
girls=['Rachel', 'Sonja', 'Jane']
for name in girls:
	hi(name)
	print('Next girl')
for i in range(1, 11):
	print(i)
def is_it_lunch(lunch):
	if 1200 <= lunch <1215:
		print("It's nearly LUNCH!")
	elif 1215<= lunch <1230:
		print("It's lunch SOOOON!")
	elif 1230<= lunch <1300:
		print('LUUUUUUUNCH')
	else:
		print("Uh oh!! You missed lunch")
is_it_lunch (1400)
def Am_I_Rich (money):
	if 10 <= money <20:
		print("you are not rich")
	elif 20 <= money <150:
		print("you're kinda rich")
	elif 150 <= money <200000:
		print ('you are SOOOO rich')
	else:
		print('need more money')
Am_I_Rich (100001)
Am_I_Rich (10)