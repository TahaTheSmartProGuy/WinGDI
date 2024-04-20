from tkinter import messagebox
import tkinter as tk
import tkinter

var = messagebox.askokcancel("WinGDI.exe By Taha - Warning!", "Run Malware? (Ok And Cancel Are The Same Thing!)")
var = messagebox.askyesno("WinGDI By Taha - Last Warning!", "Are You Sure? (Yes And No Are The Same Thing!)")

from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from time import *
desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
        255,
        255,
        255
    )) 
    SelectObject(desk, brush)
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush)
    Sleep(0)

from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from time import *

desk = GetDC(0)

x = GetSystemMetrics(0)
y = GetSystemMetrics(1)

Text = "WinGDI.exe"

SetTextColor(desk, 255)
SetBkColor(desk, 0)
for i in range(150000):
    DrawText(desk, Text, len(Text), (randrange(x), randrange(y), randrange(x), randrange(y)), DT_LEFT)

import win32gui
import win32api
import win32con
import random
import ctypes
import time
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
while True:
    hdc = win32gui.GetDC(0)
    color = (random.randint(0, 125), random.randint(0, 450), random.randint(0, 350))
    brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
    win32gui.SelectObject(hdc, brush)
    win32gui.SelectObject(hdc, brush)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.DSTINVERT)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCAND)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.NOTSRCCOPY)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCPAINT)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCINVERT)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.NOTSRCERASE)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.MERGECOPY)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCERASE)