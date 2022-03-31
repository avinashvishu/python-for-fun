from random import Random
import pyautogui as pg
import time

print("program will rn i 5 sec")
time.sleep(5)

for i in range(100):
    pg.write("Jai Shree Ram")
    time.sleep(0.5)
    pg.press("Enter")