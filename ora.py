from turtle import *
from j_sampleclock import SampleClock
from j_clock import *

class Kattintgato:

    scr = Screen()
    t = Turtle()
    clk = Clock(scr)
    secturtle1 = Turtle(shape="turtle")
    secturtle = Turtle(shape="turtle")
    minturtle = Turtle(shape="turtle")
    hourturtle = Turtle(shape="turtle")

    def writeSec(self):
        self.printToConsole()
        self.masodperc1(1)
        self.masodperc2(10)

    def pozicio(self):
        self.secturtle1.penup()
        self.secturtle1.backward(100)
        self.secturtle1.pendown()

    def masodperc2(self, x):
        self.secturtle.reset()
        self.printToConsole()
        if self.clk.sec() == x:
            self.secturtle1.left(90)
            self.secturtle1.forward(100)
            self.secturtle1.left(120)
        if self.clk.sec() != x:
            self.secturtle1.clear()


    def masodperc1(self, x):
        self.secturtle.reset()
        self.printToConsole()
        if self.clk.sec() == x:
            self.secturtle.left(90)
            self.secturtle.forward(100)
            self.secturtle.left(120)
        if self.clk.sec() > x:
            self.secturtle.clear()

    def writeMin(self):
        self.minturtle.clear()
        self.minturtle.reset()
        self.minturtle.penup()
        self.minturtle.setheading(90)
        self.minturtle.forward(180)
        self.minturtle.right(90 + 3)
        self.minturtle.pendown()
        for i in range(self.clk.min()):
            self.minturtle.forward(18.849555921538759430775860299677)
            self.minturtle.right(6)

    def writeHour(self):
        self.hourturtle.clear()
        self.hourturtle.reset()
        self.hourturtle.penup()
        self.hourturtle.setheading(90)
        self.hourturtle.forward(160)
        self.hourturtle.right(90 + 3)
        self.hourturtle.pendown()
        for i in range(self.clk.hour12() * 6):
            self.hourturtle.forward(83.775804095727819692337156887453 / 6)
            self.hourturtle.right(30 / 6)

    def __init__(self):
        self.secturtle._delay(0)
        self.secturtle.speed(0)
        self.minturtle._delay(0)
        self.minturtle.speed(0)
        self.hourturtle._delay(0)
        self.hourturtle.speed(0)
        self.pozicio()
        self.clk.setOnSecondChangeListener(self.writeSec)
        self.clk.setOnMinuteChangeListener(self.writeMin)
        self.clk.setOnHourChangeListener(self.writeHour)
        self.printToConsole()
        self.scr.mainloop()

    def printToConsole(self):
        print("Hour: " + str(self.clk.leftNumber(self.clk.hour24())) + "_" + str(
            self.clk.rightNumber(self.clk.hour24())))
        print(
            "Minute: " + str(self.clk.leftNumber(self.clk.min())) + "_" + str(self.clk.rightNumber(self.clk.min())))
        print(
            "Second: " + str(self.clk.leftNumber(self.clk.sec())) + "_" + str(self.clk.rightNumber(self.clk.sec())))

Kattintgato()