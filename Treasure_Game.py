import time
from gtts import gTTS
import os

find=False
death=False
while find==False and death==False:
	d=input("Choose the way right or left=")
	if d=="left":
		time.sleep(2)
		d1=input("Choose the way right or left=")
		if d1=="left":
			death=True
			mytext="You have been attacked by Spiders , Game Over"
			langs="en"
			mj=gTTS(text=mytext,lang=langs,slow=False)
			mj.save("voice1.mp3")
			os.system("/storage/emulated/0/my python/voice1.mp3")
			continue
		else:
			time.sleep(2)
			d2=input("Choose the way left or right=")
			if d2=="right":
				death=True
				mytext="You have been attacked by Goblin , Game Over"
				langs="en"
				mj=gTTS(text=mytext,lang=langs,slow=False)
				mj.save("voice2.mp3")
				os.system("/storage/emulated/0/my python/voice2.mp3")
				continue
			else:
				time.sleep(2)
				find=True
				mytext="You have found Treasure Hurray "
				langs="en"
				mj=gTTS(text=mytext,lang=langs,slow=False)
				mj.save("voice3.mp3")
				os.system("/storage/emulated/0/my python/voice3.mp3")
				continue	
	else:
		time.sleep(2)
		d3=input("Choose the way right or left=")
		if d3=="left":
			death=True
			mytext="You have been attacked by Devil , Game Over"
			langs="en"
			mj=gTTS(text=mytext,lang=langs,slow=False)
			mj.save("voice4.mp3")
			os.system("/storage/emulated/0/my python/voice4.mp3")
			continue
		else:
			time.sleep(2)
			d4=input("Choose the way right , centre or left=")
			if d4=="left":
				death=True
				mytext="You have been attacked by Anaconda , Game Over "
				langs="en"
				mj=gTTS(text=mytext,lang=langs,slow=False)
				mj.save("voice5.mp3")
				os.system("/storage/emulated/0/my python/voice5.mp3")
				continue
			elif d4=="centre":
				death=True
				mytext="Oops Fallen in Water ,Game Over "
				langs="en"
				mj=gTTS(text=mytext,lang=langs,slow=False)
				mj.save("voice6.mp3")
				os.system("/storage/emulated/0/my python/voice6.mp3")
				continue
			else:
				time.sleep(2)
				find=True
				mytext="Hurray !! Treasure Found"
				langs="en"
				mj=gTTS(text=mytext,lang=langs,slow=False)
				mj.save("voice7.mp3")
				os.system("/storage/emulated/0/my python/voice7.mp3")
				
print("Thanks For Playing the game")