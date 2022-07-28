# "Calculator of Photographer"

from tkinter import *
import math


root = Tk()
root["bg"] = '#707070'
root.title("YouTube @ R-VideoReview")
root.geometry("460x340")
root.resizable(False, False)

# Calculator:
"""
Determination of the size of the object on the camera matrix in the analyzed image.
Then calculating the distance to the object from the photo metadata.

Formula: d = f * (x + h) : x

d = Distance to object >>> ???
f = Lens Focal Length >>> millimeter / 1000 = meter!
x = Object Size in Camera Matrix >>> millimeter / 1000 = meter! >>> should be calculated!
h = Object True Size >>> meter!

Note:

Full-frame cameras have a sensor size of 36 x 24 mm (width / height).
Frame sizes have the following meanings:
HD = 1280 x 720 pixels
Full HD = 1920 x 1080 pixels
"""

frame = LabelFrame(root, text="Distance to Object", font='Times 22 bold', fg="#F8C729", bg="#707070")
frame.pack(padx=10, pady=10)


def calculate1():  # Lens Angle of View - degrees:

    """
    AOV = 2 * (atan * x) / (2 * f))
    x = Camera Matrix Size = 36 mm
    f = Lens Focal Length = 50 mm
    AOV = 39.5978 degrees
    """

    result1 = 2 * math.degrees(math.atan(float(e1.get()) / (2 * float(e4.get()))))

    lens_angle["text"] = f"{round(result1, 4)}°"

    print(f"1. Lens Angle of View = {result1} degrees")


def calculate2():  # Distance to Object: d = f * (x + h) : x  >>  x = kilometers - should be calculated

    x = (float(e3.get()) * float(e1.get()) / float(e2.get())) / 1000  # millimeters >> meters
    d = ((float(e4.get()) / 1000) * (x + float(e5.get())) / x)  # meters

    if d >= 1000:
        result2 = d / 1000
        distance["text"] = f"{round(result2, 3)} km"
    elif d < 1:
        result2 = d * 100
        distance["text"] = f"{round(result2, 1)} cm"
    else:
        result2 = d
        distance["text"] = f"{round(result2, 3)} m"

    print(f"2.1. Object Size in Camera Matrix = {x} millimeters")
    print(f"2.2. Distance to Object = {d} meters")


def calculate3():  # Object Angle of View = degrees:
    """
    1. AOV (lens angle of view) = 2 * math.degrees(math.atan(float(e1.get()) / (2 * float(e4.get()))))
    2. float(e2.get())  # габарит кадра в пикселях
    3. float(e3.get())  # габарит объекта в пикселях
        e2 == AOV
        e3 == object_angle
    4. object_angle = float(e3.get()) * AOV / float(e2.get())
    """

    aov = 2 * math.degrees(math.atan(float(e1.get()) / (2 * float(e4.get()))))
    result3 = float(e3.get()) * aov / float(e2.get())

    object_angle["text"] = f"{round(result3, 4)}°"

    print(f"3. Object Angular Diameter = {result3} degrees")


def calculate4():  # Space Size in Image - kilometers:

    """
    e1.get() - camera matrix size == e1 (millimeters)
    e2.get() - image full size == e2 (pixels)
    e3.get() - object size in image == e3 (pixels)
    e4.get() - lens focal length == e4 (millimeters)
    e5.get() - object true size == e5 (meters)

    1. object size in camera matrix:
    x = (float(e3.get()) * float(e1.get()) / float(e2.get())) / 1000  # millimeter >> meter

    2. distance to object:
    d = ((float(e4.get()) / 1000) * (x + float(e5.get())) / x)  # meter

    3. lens angle of view:
    angle = 2 * math.degrees(math.atan(float(e1.get()) / (2 * float(e4.get()))))

    4. space size at the investigated distance:
    space = (d * math.tan(math.radians(angle))) * 2
    """

    x = (float(e3.get()) * float(e1.get()) / float(e2.get())) / 1000  # millimeter >> meter
    d = ((float(e4.get()) / 1000) * (x + float(e5.get())) / x)  # meters
    angle = (2 * math.degrees(math.atan(float(e1.get()) / (2 * float(e4.get()))))) / 2  # half angle
    space = (d * math.tan(math.radians(angle))) * 2  # meters >> half.side * 2 = full.side

    if space >= 1000:
        result4 = space / 1000
        space_size["text"] = f"{round(result4, 3)} km"
    elif space < 1:
        result4 = space * 100
        space_size["text"] = f"{round(result4, 1)} cm"
    else:
        result4 = space
        space_size["text"] = f"{round(result4, 3)} m"

    print(f"4.1. Object Size in Camera Matrix  = {x} millimeters")
    print(f"4.2. Distance to Object  = {d} kilometers")
    print(f"4.3. Lens Angle of View (half) = {angle} degrees")
    print(f"4.4. Space Size in Image = {space} meters")


# Entries:

l1 = Label(frame, text="Camera Matrix Size - millimeters:", width=35, pady=5, fg="white", bg="#454545")
l1.grid(row=0, column=0)

e1 = Entry(frame, width=10, borderwidth=4, justify=CENTER)
e1.get()
e1.insert(0, '')
e1.grid(row=0, column=1)

l2 = Label(frame, text="Image Full Size - pixels:", width=35, pady=5, fg="white", bg="#454545")
l2.grid(row=1, column=0)

e2 = Entry(frame, width=10, borderwidth=4, justify=CENTER)
e2.get()
e2.insert(0, '')
e2.grid(row=1, column=1)

l3 = Label(frame, text="Object Size in Image - pixels:", width=35, pady=5, fg="white", bg="#454545")
l3.grid(row=2, column=0)

e3 = Entry(frame, width=10, borderwidth=4, justify=CENTER)
e3.get()
e3.insert(0, '')
e3.grid(row=2, column=1)

l4 = Label(frame, text="Lens Focal Length - millimeters:", width=35, pady=5, fg="white", bg="#454545")
l4.grid(row=3, column=0)

e4 = Entry(frame, width=10, borderwidth=4, justify=CENTER)
e4.get()
e4.insert(0, '')
e4.grid(row=3, column=1)

l5 = Label(frame, text="Object True Size - meters:", width=35, pady=5, fg="white", bg="#454545")
l5.grid(row=4, column=0)

e5 = Entry(frame, width=10, borderwidth=4, justify=CENTER)
e5.get()
e5.insert(0, '')
e5.grid(row=4, column=1)

# Calculations:

c1 = Button(frame, text="Lens Angle of View  =  degrees:", font='Helvetica 15 bold', width=32, pady=1.5,
            borderwidth=2, fg="#850000", command=calculate1)
c1.grid(row=5, column=0)

lens_angle = Label(frame, width=11, pady=5, bg="#F8C729")
lens_angle.grid(row=5, column=1)
lens_angle.bind("<Button>", calculate1)

c2 = Button(frame, text="Distance to Object  =  cm: m: km:", font='Helvetica 15 bold', width=32, pady=1.5,
            borderwidth=2, fg="#850000", command=calculate2)
c2.grid(row=6, column=0)

distance = Label(frame, width=11, pady=5, bg="#F8C729")
distance.grid(row=6, column=1)
distance.bind("<Button>", calculate2)

c3 = Button(frame, text="Object Angle of View  =  degrees:", font='Helvetica 15 bold', width=32, pady=1.5,
            borderwidth=2, fg="#850000", command=calculate3)
c3.grid(row=7, column=0)

object_angle = Label(frame, width=11, pady=5, bg="#F8C729")
object_angle.grid(row=7, column=1)
object_angle.bind("<Button>", calculate3)

c4 = Button(frame, text="Space Size in Image  =  cm: m: km:", font='Helvetica 15 bold', width=32, pady=1.5,
            borderwidth=2, fg="#850000", command=calculate4)
c4.grid(row=8, column=0)

space_size = Label(frame, width=11, pady=5, bg="#F8C729")
space_size.grid(row=8, column=1)
space_size.bind("<Button>", calculate4)

root.mainloop()
