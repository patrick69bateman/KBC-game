import vlc
import time
import pandas
import csv
import os

list1 = ["The International Literacy Day is observed on? ",
"The language of Lakshadweep. a Union Territory of India, is? ", 
"Which day is observed as the World Standards Day? ", "Bahubali festival is related to? ", 
"September 27 is celebrated every year as? ", 
"Who is the author of 'Manas Ka-Hans'? ", 
"Pongal is a popular festival of which state? ", 
"'Good Friday' is observed to commemorate the event of? ",
"Who is the author of the epic 'Meghdoot'? "]

list2 = ["sep 8", "Malayalam", "Oct 14", "Jainism", "World tourism day", "Amit lal nagar", "Tamil nadu", "crucification 'of Jesus Christ", "Kalidas"]

list3 = ["1 lakh", "5 lakh", "20 lakh", "50 lakh", "80 lakh", "1 cr", "1.5 cr"]


print("Welcome to KBC")
# sound_file = vlc.MediaPlayer("")
# sound_file.play()
# time.sleep(10)

print("Q1")
print(list1[0])
a = input("Enter your answer \n")
if a == (list2[0]):
 print("Well done")
 os.startfile("C:\\Users\\ASUS\\Downloads\\7 CRORE KBC - SOUND EFFECT.mp3")
#   sound_file = vlc.MediaPlayer("C:\Users\ASUS\Downloads\7 CRORE KBC - SOUND EFFECT.mp4")
#   sound_file.play()
#   time.sleep(10)
else: 
 print("loser")
 os.startfile("C:\\Users\\ASUS\Downloads\\The ULTIMATE mashup of sound effects.mp3")

#  sound_file = vlc.MediaPlayer("C:\Users\ASUS\Downloads\The ULTIMATE mashup of sound effects.mp3")
#  sound_file.play()
#  time.sleep(10)