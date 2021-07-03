# "Calculator of Photographer"

from tkinter import *

root = Tk()
root["bg"] = '#808080'
root.title("Calculator of Photographer")
root.geometry("440x280")
root.resizable(False, False)

# Calculator:
"""
Determination of the size of the object on the camera matrix in the analyzed image.
Then calculating the distance to the object from the photo metadata.

Formula: d = f * (x + h) : x

d = Distance to object >>> ???
f = Lens Focal Length >>> millimeter / 1000 = meter!
x = Object Size in Camera Matrix" >>> millimeter / 1000 = meter! >>> should be calculated!
h = Object True Size >>> meter!

Note:

Full-frame cameras have a sensor size of 36 x 24 mm (width / height).
Frame sizes have the following meanings:
HD = 1280 x 720 pixels
Full HD = 1920 x 1080 pixels
"""

frame = LabelFrame(root, text="DISTANCE TO OBJECT", font='Helvetica 20 bold', fg="#F8C729", bg="#808080")
frame.pack(padx=10, pady=10)


def calculate1():  # d = f * (x + h) : x

    x = (int(e3.get()) * float(e1.get()) / int(e2.get())) / 1000
    d1 = (int(e4.get()) / 1000) * (x + float(e5.get())) / x

    if d1 < 0:
        meter["text"] = "Error"
    else:
        meter["text"] = round(d1, 4)

    print(round(d1, 4))


def calculate2():  # d = f * (H + h) : H

    x = (int(e3.get()) * float(e1.get()) / int(e2.get())) / 1000
    d2 = ((int(e4.get()) / 1000) * (x + float(e5.get())) / x) / 1000

    if d2 < 0:
        kilometer["text"] = "Error"
    else:
        kilometer["text"] = round(d2, 4)

    print(round(d2, 4))


l1 = Label(frame, text=' "Camera Matrix Size" in millimeter:', width=32, pady=5, fg="white", bg="#505050")
l1.grid(row=0, column=0)

e1 = Entry(frame, width=10, borderwidth=4)
e1.get()
e1.insert(0, '')
e1.grid(row=0, column=1)

l2 = Label(frame, text=' "Image Full Size" in pixels:', width=32, pady=5, fg="white", bg="#505050")
l2.grid(row=1, column=0)

e2 = Entry(frame, width=10, borderwidth=4)
e2.get()
e2.insert(0, '')
e2.grid(row=1, column=1)

l3 = Label(frame, text=' "Measured Object Size (image)" in pixels:', width=32, pady=5, fg="white", bg="#505050")
l3.grid(row=2, column=0)

e3 = Entry(frame, width=10, borderwidth=4)
e3.get()
e3.insert(0, '')
e3.grid(row=2, column=1)

l4 = Label(frame, text=' "Lens Focal Length" in millimeter:', width=32, pady=5, fg="white", bg="#505050")
l4.grid(row=3, column=0)

e4 = Entry(frame, width=10, borderwidth=4)
e4.get()
e4.insert(0, '')
e4.grid(row=3, column=1)

l5 = Label(frame, text=' "Object True Size" in meter:', width=32, pady=5, fg="white", bg="#505050")
l5.grid(row=4, column=0)

e5 = Entry(frame, width=10, borderwidth=4)
e5.get()
e5.insert(0, '')
e5.grid(row=4, column=1)

c1 = Button(frame, text="CALCULATE - meter:", font='Helvetica 15 bold', width=32, pady=7, borderwidth=2,
            fg="#850000", command=calculate1)
c1.grid(row=5, column=0)

meter = Label(frame, width=11, pady=5, bg="#F8C729")
meter.grid(row=5, column=1)
meter.bind("<Button>", calculate1)

c2 = Button(frame, text="CALCULATE - kilometer:", font='Helvetica 15 bold', width=32, pady=7, borderwidth=2,
            fg="#850000", command=calculate2)
c2.grid(row=6, column=0)

kilometer = Label(frame, width=11, pady=5, bg="#F8C729")
kilometer.grid(row=6, column=1)
kilometer.bind("<Button>", calculate2)

root.mainloop()
