from turtle import *
from j_sampleclock import SampleClock
from j_clock import *
from Numbers import *
from Numbers2 import *
from Numbers3 import *

class Kattintgato:
    num = Numbers()
    num1 = Numbers2()
    num2 = Numbers3()
    num3 = Numbers4()
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
        self.masodperc2()
        self.perc()
        self.perctizes()

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
                self.num.nulla()
            if x == 11:
                self.num.egy()
            if x == 12:
                self.num.ketto()
            if x == 13:
                self.num.harom()
            if x == 14:
                self.num.negy()
            if x == 15:
                self.num.ot()
            if x == 16:
                self.num.hat()
            if x == 17:
                self.num.het()
            if x == 18:
                self.num.nyolc()
            if x == 19:
                self.num.kilenc()
            if x == 20:
                self.num.nulla()
            if x == 21:
                self.num.egy()
            if x == 22:
                self.num.ketto()
            if x == 23:
                self.num.harom()
            if x == 24:
                self.num.negy()
            if x == 25:
                self.num.ot()
            if x == 26:
                self.num.hat()
            if x == 27:
                self.num.het()
            if x == 28:
                self.num.nyolc()
            if x == 29:
                self.num.kilenc()
            if x == 30:
                self.num.nulla()
            if x == 31:
                self.num.egy()
            if x == 32:
                self.num.ketto()
            if x == 33:
                self.num.harom()
            if x == 34:
                self.num.negy()
            if x == 35:
                self.num.ot()
            if x == 36:
                self.num.hat()
            if x == 37:
                self.num.het()
            if x == 38:
                self.num.nyolc()
            if x == 39:
                self.num.kilenc()
            if x == 40:
                self.num.nulla()
            if x == 41:
                self.num.egy()
            if x == 42:
                self.num.ketto()
            if x == 43:
                self.num.harom()
            if x == 44:
                self.num.negy()
            if x == 45:
                self.num.ot()
            if x == 46:
                self.num.hat()
            if x == 47:
                self.num.het()
            if x == 48:
                self.num.nyolc()
            if x == 49:
                self.num.kilenc()
            if x == 50:
                self.num.nulla()
            if x == 51:
                self.num.egy()
            if x == 52:
                self.num.ketto()
            if x == 53:
                self.num.harom()
            if x == 54:
                self.num.negy()
            if x == 55:
                self.num.ot()
            if x == 56:
                self.num.hat()
            if x == 57:
                self.num.het()
            if x == 58:
                self.num.nyolc()
            if x == 59:
                self.num.kilenc()

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

    def masodperc2(self):
        if self.clk.sec() == 0:
            self.num1.nulla()
        if self.clk.sec() == 9:
            self.num1.clearer()
        if self.clk.sec() == 10:
            self.num1.egy()
        if self.clk.sec() == 20:
            self.num1.clearer()
        if self.clk.sec() == 20:
            self.num1.ketto()
        if self.clk.sec() == 30:
            self.num1.clearer()
        if self.clk.sec() == 30:
            self.num1.harom()
        if self.clk.sec() == 40:
            self.num1.clearer()
        if self.clk.sec() == 40:
            self.num1.negy()
        if self.clk.sec() == 50:
            self.num1.clearer()
        if self.clk.sec() == 50:
            self.num1.ot()
        if self.clk.sec() == 59:
            self.num1.clearer()

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
        self.kirajzolo(16)
        self.kirajzolo(17)
        self.kirajzolo(18)
        self.kirajzolo(19)
        self.kirajzolo(20)
        self.kirajzolo(21)
        self.kirajzolo(22)
        self.kirajzolo(23)
        self.kirajzolo(24)
        self.kirajzolo(25)
        self.kirajzolo(26)
        self.kirajzolo(27)
        self.kirajzolo(28)
        self.kirajzolo(29)
        self.kirajzolo(30)
        self.kirajzolo(31)
        self.kirajzolo(32)
        self.kirajzolo(33)
        self.kirajzolo(34)
        self.kirajzolo(35)
        self.kirajzolo(36)
        self.kirajzolo(37)
        self.kirajzolo(38)
        self.kirajzolo(39)
        self.kirajzolo(40)
        self.kirajzolo(41)
        self.kirajzolo(42)
        self.kirajzolo(43)
        self.kirajzolo(44)
        self.kirajzolo(45)
        self.kirajzolo(46)
        self.kirajzolo(47)
        self.kirajzolo(48)
        self.kirajzolo(49)
        self.kirajzolo(50)
        self.kirajzolo(51)
        self.kirajzolo(52)
        self.kirajzolo(53)
        self.kirajzolo(54)
        self.kirajzolo(55)
        self.kirajzolo(56)
        self.kirajzolo(57)
        self.kirajzolo(58)
        self.kirajzolo(59)

    def perc(self):
        self.kirajzolo3(1)
        self.kirajzolo3(2)
        self.kirajzolo3(3)
        self.kirajzolo3(4)
        self.kirajzolo3(5)
        self.kirajzolo3(6)
        self.kirajzolo3(7)
        self.kirajzolo3(8)
        self.kirajzolo3(9)

    def perctizes(self):
        if self.clk.min() == 0:
            self.num2.nulla2()
        if self.clk.min() == 9:
            self.num2.clearer()
        if self.clk.min() == 10:
            self.num2.egy2()
        if self.clk.min() == 20:
            self.num2.clearer()
        if self.clk.min() == 20:
            self.num2.ketto2()
        if self.clk.min() == 30:
            self.num2.clearer()
        if self.clk.min() == 30:
            self.num2.harom2()
        if self.clk.min() == 40:
            self.num2.clearer()
        if self.clk.min() == 40:
            self.num2.negy2()
        if self.clk.min() == 50:
            self.num2.clearer()
        if self.clk.min() == 50:
            self.num2.ot2()
        if self.clk.min() == 59:
            self.num2.clearer()

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

    def pozicio2(self):
        self.minturtle.penup()
        self.minturtle.backward(500)
        self.minturtle.pendown()


    def kirajzolo3(self, x):
        if self.clk.min() != x:
            self.num2.clearer()
        if self.clk.min() == x:
            if x == 0:
                self.num2.nulla()
            if x == 1:
                self.num2.egy()
            if x == 2:
                self.num2.ketto()
            if x == 3:
                self.num2.harom()
            if x == 4:
                self.num2.negy()
            if x == 5:
                self.num2.ot()
            if x == 6:
                self.num2.hat()
            if x == 7:
                self.num2.het()
            if x == 8:
                self.num2.nyolc()
            if x == 9:
                self.num2.kilenc()
            if x == 10:
                self.num2.nulla()
            if x == 11:
                self.num2.egy()
            if x == 12:
                self.num2.ketto()
            if x == 13:
                self.num2.harom()
            if x == 14:
                self.num2.negy()
            if x == 15:
                self.num2.ot()
            if x == 16:
                self.num2.hat()
            if x == 17:
                self.num2.het()
            if x == 18:
                self.num2.nyolc()
            if x == 19:
                self.num2.kilenc()
            if x == 20:
                self.num2.nulla()
            if x == 21:
                self.num2.egy()
            if x == 22:
                self.num2.ketto()
            if x == 23:
                self.num2.harom()
            if x == 24:
                self.num2.negy()
            if x == 25:
                self.num2.ot()
            if x == 26:
                self.num2.hat()
            if x == 27:
                self.num2.het()
            if x == 28:
                self.num2.nyolc()
            if x == 29:
                self.num2.kilenc()
            if x == 30:
                self.num2.nulla()
            if x == 31:
                self.num2.egy()
            if x == 32:
                self.num2.ketto()
            if x == 33:
                self.num2.harom()
            if x == 34:
                self.num2.negy()
            if x == 35:
                self.num2.ot()
            if x == 36:
                self.num2.hat()
            if x == 37:
                self.num2.het()
            if x == 38:
                self.num2.nyolc()
            if x == 39:
                self.num2.kilenc()
            if x == 40:
                self.num2.nulla()
            if x == 41:
                self.num2.egy()
            if x == 42:
                self.num2.ketto()
            if x == 43:
                self.num2.harom()
            if x == 44:
                self.num2.negy()
            if x == 45:
                self.num2.ot()
            if x == 46:
                self.num2.hat()
            if x == 47:
                self.num2.het()
            if x == 48:
                self.num2.nyolc()
            if x == 49:
                self.num2.kilenc()
            if x == 50:
                self.num2.nulla()
            if x == 51:
                self.num2.egy()
            if x == 52:
                self.num2.ketto()
            if x == 53:
                self.num2.harom()
            if x == 54:
                self.num2.negy()
            if x == 55:
                self.num2.ot()
            if x == 56:
                self.num2.hat()
            if x == 57:
                self.num2.het()
            if x == 58:
                self.num2.nyolc()
            if x == 59:
                self.num2.kilenc()

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

    def hour12(self):
        self.kirajzolo4(1)

    def pozicio3(self):
        self.minturtle.penup()
        self.minturtle.backward(500)
        self.minturtle.pendown()

    def kirajzolo4(self, x):
        if self.clk.hour12() != x:
            self.num.clearer()
        if self.clk.hour12() == x:
            if x == 0:
                self.num4.nulla()
            if x == 1:
                self.num4.egy()
            if x == 2:
                self.num4.ketto()
            if x == 3:
                self.num4.harom()
            if x == 4:
                self.num4.negy()
            if x == 5:
                self.num4.ot()
            if x == 6:
                self.num4.hat()
            if x == 7:
                self.num4.het()
            if x == 8:
                self.num4.nyolc()
            if x == 9:
                self.num4.kilenc()
            if x == 10:
                self.num4.nulla()
            if x == 11:
                self.num4.egy()
            if x == 12:
                self.num4.ketto()
            if x == 13:
                self.num4.harom()
            if x == 14:
                self.num4.negy()
            if x == 15:
                self.num4.ot()
            if x == 16:
                self.num4.hat()
            if x == 17:
                self.num4.het()
            if x == 18:
                self.num4.nyolc()
            if x == 19:
                self.num4.kilenc()
            if x == 20:
                self.num4.nulla()
            if x == 21:
                self.num4.egy()
            if x == 22:
                self.num4.ketto()
            if x == 23:
                self.num4.harom()
            if x == 24:
                self.num4.negy()
            if x == 25:
                self.num4.ot()
            if x == 26:
                self.num4.hat()
            if x == 27:
                self.num4.het()
            if x == 28:
                self.num4.nyolc()
            if x == 29:
                self.num4.kilenc()
            if x == 30:
                self.num4.nulla()
            if x == 31:
                self.num4.egy()
            if x == 32:
                self.num4.ketto()
            if x == 33:
                self.num4.harom()
            if x == 34:
                self.num4.negy()
            if x == 35:
                self.num4.ot()
            if x == 36:
                self.num4.hat()
            if x == 37:
                self.num4.het()
            if x == 38:
                self.num4.nyolc()
            if x == 39:
                self.num4.kilenc()
            if x == 40:
                self.num4.nulla()
            if x == 41:
                self.num4.egy()
            if x == 42:
                self.num4.ketto()
            if x == 43:
                self.num4.harom()
            if x == 44:
                self.num4.negy()
            if x == 45:
                self.num4.ot()
            if x == 46:
                self.num4.hat()
            if x == 47:
                self.num4.het()
            if x == 48:
                self.num4.nyolc()
            if x == 49:
                self.num4.kilenc()
            if x == 50:
                self.num4.nulla()
            if x == 51:
                self.num4.egy()
            if x == 52:
                self.num4.ketto()
            if x == 53:
                self.num4.harom()
            if x == 54:
                self.num4.negy()
            if x == 55:
                self.num4.ot()
            if x == 56:
                self.num4.hat()
            if x == 57:
                self.num4.het()
            if x == 58:
                self.num4.nyolc()
            if x == 59:
                self.num4.kilenc()

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