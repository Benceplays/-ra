from turtle import *
from j_sampleclock import SampleClock
from j_clock import *
from Numbers import *

class Kattintgato:
    num = Numbers()
    num1 = Numbers()
    scr = Screen()
    t = Turtle()
    clk = Clock(scr)
    secturtle1 = Turtle(shape="turtle")
    secturtle = Turtle(shape="turtle")
    minturtle = Turtle(shape="turtle")
    hourturtle = Turtle(shape="turtle")

    def writeSec(self):
        self.printToConsole()
        self.masodperc1()


    def pozicio(self):
        self.secturtle1.penup()
        self.secturtle1.backward(100)
        self.secturtle1.pendown()

    def kirajzolo(self, x):
        if self.clk.sec() != x:
            self.num.clearer()
        if self.clk.sec() == x:
            if x == 0:
                self.num.nulla()
            if x == 1:
                self.num.egy()
            if x == 2:
                self.num.ketto()
            if x == 3:
                self.num.harom()
            if x == 4:
                self.num.negy()
            if x == 5:
                self.num.ot()
            if x == 6:
                self.num.hat()
            if x == 7:
                self.num.het()
            if x == 8:
                self.num.nyolc()
            if x == 9:
                self.num.kilenc()
            if x == 10:
                self.num.tiz()
            if x == 11:
                self.num.tizenegy()
            if x == 12:
                self.num.tizenketto()
            if x == 13:
                self.num.tizenharom()
            if x == 14:
                self.num.tizennegy()
            if x ==15:
                self.num.tizenot()
    def kirajzolo2(self, x):
        if self.clk.sec() != x:
            self.num1.clearer()
        if self.clk.sec() == x:
            if x == 0:
                self.num1.nulla()
            if x == x < 20:
                self.num1.egy()
            if x == x < 30:
                self.num1.ketto()
            if x == x < 40:
                self.num1.harom()
            if x == x < 50:
                self.num1.negy()
            if x == x < 60:
                self.num1.ot()



    def masodperc1(self):
        self.printToConsole()
        self.kirajzolo(0)
        self.kirajzolo(1)
        self.kirajzolo(2)
        self.kirajzolo(3)
        self.kirajzolo(4)
        self.kirajzolo(5)
        self.kirajzolo(6)
        self.kirajzolo(7)
        self.kirajzolo(8)
        self.kirajzolo(9)
        self.kirajzolo(10)
        self.kirajzolo(11)
        self.kirajzolo(12)
        self.kirajzolo(13)
        self.kirajzolo(14)
        self.kirajzolo(15)

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
        self.scr.bgcolor('black')
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