import pyautogui
import pwn
import time 
import os

run = os.system

pyautogui.hotkey('ctrl','alt','T')		#open new terminal
time.sleep(3)
pyautogui.hotkey('ctrl','+')			# zoom in
pyautogui.hotkey('ctrl','+')
pyautogui.hotkey('ctrl','+')
pyautogui.hotkey('ctrl','+')
pyautogui.hotkey('ctrl','+')
time.sleep(2)

pyautogui.typewrite("cd Desktop/saniyactf/")		# change to directory were the file is
pyautogui.press('enter')
time.sleep(1)

#-----------------------------------------------------------------------------------------------------------------------

pyautogui.typewrite('echo "case 1 of buffer overflow"')		# when to count digit we enter more data it gives error 
pyautogui.press('enter')
time.sleep(1)

pyautogui.typewrite('./try1')		# the executable file name to rum the file
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('55555555555555')		#this digits are more than 10 characters so its crash
pyautogui.press('enter')
time.sleep(2)

#------------------------------------------------------------------------------------------------------------------------

time.sleep(2)
pyautogui.typewrite('echo "case 2 of buffer overflow"')		# when to count digit we enter any 10 digit and in second line to store data when we enter more data program crash 
pyautogui.press('enter')
time.sleep(1)

pyautogui.typewrite('./try1')
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('1234567891')		#this digits is only 10 characters so it will not give crash
pyautogui.press('enter')
pyautogui.typewrite('12345678911234')		#this digits is more than 10 characters give crash
pyautogui.press('enter')
time.sleep(2)

#------------------------------------------------------------------------------------------------------------------------

time.sleep(2)
pyautogui.typewrite('echo "case 3 of buffer overflow"')		# when to count digit we enter digit 15 (only no greater than 15 no will crash) and in lines to store data when we enter the random no till 15 after that program crash 
pyautogui.press('enter')
time.sleep(1)

pyautogui.typewrite('./try1')
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('15')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('1')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('2')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('3')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('4')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('5')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('6')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('7')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('8')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('9')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('10')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('11')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('12')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('13')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('14')		#enter 15 no  
pyautogui.press('enter')
time.sleep(2)


#------------------------------------------------------------------------------------------------------------------------

time.sleep(2)
pyautogui.typewrite('echo "case 4 of buffer overflow"')		# when to count digit we enter any no from 1 to 10 and in second line to store data when we enter more data program crash 
pyautogui.press('enter')
time.sleep(1)

pyautogui.typewrite('./try1')
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('7')		# enter any no in range 1 to 10
pyautogui.press('enter')
pyautogui.typewrite('12345678911234')		#this digits is more than 10 characters give crash the program and prints the same no of line 
pyautogui.press('enter')
time.sleep(2)

