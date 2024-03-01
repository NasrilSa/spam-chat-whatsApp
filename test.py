import pyautogui as pg
import time
time.sleep(10)

for i in range(1000): #humlah pesan yang ingin dikirim
    pg.write("test") #pesan yang ingin ditulis
    pg.press('Enter') 

