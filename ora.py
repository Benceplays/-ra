from turtle import *
from j_sampleclock import SampleClock
from j_clock import *
from Numbers import *
from Numbers2 import *
from Numbers3 import *
from Numbers5 import *
from Numbers4 import *

class Kattintgato:
    num = Numbers()
    num1 = Numbers2()
    num2 = Numbers3()
    num4 = Numbers5()
    num3 = Numbers4()
    scr = Screen()
    t = Turtle()
    t2 = Turtle()
    clk = Clock(scr)
    secturtle1 = Turtle(shape="turtle")
    secturtle = Turtle(shape="turtle")
    minturtle = Turtle(shape="turtle")
    hourturtle = Turtle(shape="turtle")

    def writeSec(self):
        self.printToConsole()
        self.masodperc1()
        self.masodperc2()
        self.secturtle.penup()
        self.secturtle.forward(300)
        self.secturtle.pendown()

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


    def writeMin(self):
        self.kirajzoloperc()



    def kirajzoloperc2szam(self):
        if self.clk.min() == 0:
            self.num4.clearer()
        if self.clk.min() == 0:
            self.num4.nulla()
        if self.clk.min() == 1:
            self.num4.clearer()
        if self.clk.min() == 1:
            self.num4.nulla()
        if self.clk.min() == 2:
            self.num4.clearer()
        if self.clk.min() == 2:
            self.num4.nulla()
        if self.clk.min() == 3:
            self.num4.clearer()
        if self.clk.min() == 3:
            self.num4.nulla()
        if self.clk.min() == 4:
            self.num4.nulla()
        if self.clk.min() == 4:
            self.num4.nulla()
        if self.clk.min() == 5:
            self.num4.clearer()
        if self.clk.min() == 5:
            self.num4.nulla()
        if self.clk.min() == 6:
            self.num4.clearer()
        if self.clk.min() == 6:
            self.num4.nulla()
        if self.clk.min() == 7:
            self.num4.clearer()
        if self.clk.min() == 7:
            self.num4.nulla()
        if self.clk.min() == 8:
            self.num4.clearer()
        if self.clk.min() == 8:
            self.num4.nulla()
        if self.clk.min() == 9:
            self.num4.clearer()
        if self.clk.min() == 9:
            self.num4.nulla()
        if self.clk.min() == 10:
            self.num4.clearer()
        if self.clk.min() == 10:
            self.num4.egy()
        if self.clk.min() == 11:
            self.num4.clearer()
        if self.clk.min() == 11:
            self.num4.egy()
        if self.clk.min() == 12:
            self.num4.clearer()
        if self.clk.min() == 12:
            self.num4.egy()
        if self.clk.min() == 13:
            self.num4.clearer()
        if self.clk.min() == 13:
            self.num4.egy()
        if self.clk.min() == 14:
            self.num4.clearer()
        if self.clk.min() == 14:
            self.num4.egy()
        if self.clk.min() == 15:
            self.num4.clearer()
        if self.clk.min() == 15:
            self.num4.egy()
        if self.clk.min() == 16:
            self.num4.clearer()
        if self.clk.min() == 16:
            self.num4.egy()
        if self.clk.min() == 17:
            self.num4.clearer()
        if self.clk.min() == 17:
            self.num4.egy()
        if self.clk.min() == 18:
            self.num4.clearer()
        if self.clk.min() == 18:
            self.num4.egy()
        if self.clk.min() == 19:
            self.num4.clearer()
        if self.clk.min() == 19:
            self.num4.egy()
        if self.clk.min() == 20:
            self.num4.clearer()
        if self.clk.min() == 20:
            self.num4.ketto()
        if self.clk.min() == 21:
            self.num4.clearer()
        if self.clk.min() == 21:
            self.num4.ketto()
        if self.clk.min() == 22:
            self.num4.clearer()
        if self.clk.min() == 22:
            self.num4.ketto()
        if self.clk.min() == 23:
            self.num4.clearer()
        if self.clk.min() == 23:
            self.num4.ketto()
        if self.clk.min() == 24:
            self.num4.clearer()
        if self.clk.min() == 24:
            self.num4.ketto()
        if self.clk.min() == 25:
            self.num4.clearer()
        if self.clk.min() == 25:
            self.num4.ketto()
        if self.clk.min() == 26:
            self.num4.clearer()
        if self.clk.min() == 26:
            self.num4.ketto()
        if self.clk.min() == 27:
            self.num4.clearer()
        if self.clk.min() == 27:
            self.num4.ketto()
        if self.clk.min() == 28:
            self.num4.clearer()
        if self.clk.min() == 28:
            self.num4.ketto()
        if self.clk.min() == 29:
            self.num4.clearer()
        if self.clk.min() == 29:
            self.num4.ketto()
        if self.clk.min() == 30:
            self.num4.clearer()
        if self.clk.min() == 30:
            self.num4.harom()
        if self.clk.min() == 31:
            self.num4.clearer()
        if self.clk.min() == 31:
            self.num4.harom()
        if self.clk.min() == 32:
            self.num4.clearer()
        if self.clk.min() == 32:
            self.num4.harom()
        if self.clk.min() == 33:
            self.num4.clearer()
        if self.clk.min() == 33:
            self.num4.harom()
        if self.clk.min() == 34:
            self.num4.clearer()
        if self.clk.min() == 34:
            self.num4.harom()
        if self.clk.min() == 35:
            self.num4.clearer()
        if self.clk.min() == 35:
            self.num4.harom()
        if self.clk.min() == 36:
            self.num4.clearer()
        if self.clk.min() == 36:
            self.num4.harom()
        if self.clk.min() == 37:
            self.num4.clearer()
        if self.clk.min() == 37:
            self.num4.harom()
        if self.clk.min() == 38:
            self.num4.clearer()
        if self.clk.min() == 38:
            self.num4.harom()
        if self.clk.min() == 39:
            self.num4.clearer()
        if self.clk.min() == 39:
            self.num4.harom()
        if self.clk.min() == 40:
            self.num4.negy()
        if self.clk.min() == 41:
            self.num4.clearer()
        if self.clk.min() == 41:
            self.num4.negy()
        if self.clk.min() == 42:
            self.num4.clearer()
        if self.clk.min() == 42:
            self.num4.negy()
        if self.clk.min() == 43:
            self.num4.clearer()
        if self.clk.min() == 43:
            self.num4.negy()
        if self.clk.min() == 44:
            self.num4.clearer()
        if self.clk.min() == 44:
            self.num4.negy()
        if self.clk.min() == 45:
            self.num4.clearer()
        if self.clk.min() == 45:
            self.num4.negy()
        if self.clk.min() == 46:
            self.num4.clearer()
        if self.clk.min() == 46:
            self.num4.negy()
        if self.clk.min() == 47:
            self.num4.clearer()
        if self.clk.min() == 47:
            self.num4.negy()
        if self.clk.min() == 48:
            self.num4.clearer()
        if self.clk.min() == 48:
            self.num4.negy()
        if self.clk.min() == 49:
            self.num4.clearer()
        if self.clk.min() == 49:
            self.num4.negy()
        if self.clk.min() == 50:
            self.num4.clearer()
        if self.clk.min() == 50:
            self.num4.ot()
        if self.clk.min() == 51:
            self.num4.clearer()
        if self.clk.min() == 51:
            self.num4.ot()
        if self.clk.min() == 52:
            self.num4.clearer()
        if self.clk.min() == 52:
            self.num4.ot()
        if self.clk.min() == 53:
            self.num4.clearer()
        if self.clk.min() == 53:
            self.num4.ot()
        if self.clk.min() == 54:
            self.num4.clearer()
        if self.clk.min() == 54:
            self.num4.ot()
        if self.clk.min() == 55:
            self.num4.clearer()
        if self.clk.min() == 55:
            self.num4.ot()
        if self.clk.min() == 56:
            self.num4.clearer()
        if self.clk.min() == 56:
            self.num4.ot()
        if self.clk.min() == 57:
            self.num4.clearer()
        if self.clk.min() == 57:
            self.num4.ot()
        if self.clk.min() == 58:
            self.num4.clearer()
        if self.clk.min() == 58:
            self.num4.ot()
        if self.clk.min() == 59:
            self.num4.clearer()
        if self.clk.min() == 59:
            self.num4.ot()



    def kirajzoloperc(self):
        if self.clk.min() == 0:
            self.num2.clearer()
        if self.clk.min() == 0:
            self.num2.nulla()
        if self.clk.min() == 1:
            self.num2.clearer()
        if self.clk.min() == 1:
            self.num2.egy()
        if self.clk.min() == 2:
            self.num2.clearer()
        if self.clk.min() == 2:
            self.num2.ketto()
        if self.clk.min() == 3:
            self.num2.clearer()
        if self.clk.min() == 3:
            self.num2.harom()
        if self.clk.min() == 4:
            self.num2.clearer()
        if self.clk.min() == 4:
            self.num2.negy()
        if self.clk.min() == 5:
            self.num2.clearer()
        if self.clk.min() == 5:
            self.num2.ot()
        if self.clk.min() == 6:
            self.num2.clearer()
        if self.clk.min() == 6:
            self.num2.hat()
        if self.clk.min() == 7:
            self.num2.clearer()
        if self.clk.min() == 7:
            self.num2.het()
        if self.clk.min() == 8:
            self.num2.clearer()
        if self.clk.min() == 8:
            self.num2.nyolc()
        if self.clk.min() == 9:
            self.num2.clearer()
        if self.clk.min() == 9:
            self.num2.kilenc()
        if self.clk.min() == 10:
            self.num2.clearer()
        if self.clk.min() == 10:
            self.num2.tiz()
        if self.clk.min() == 11:
            self.num2.clearer()
        if self.clk.min() == 11:
            self.num2.tizenegy()
        if self.clk.min() == 12:
            self.num2.clearer()
        if self.clk.min() == 12:
            self.num2.tizenketto()
        if self.clk.min() == 13:
            self.num2.clearer()
        if self.clk.min() == 13:
            self.num2.tizenharom()
        if self.clk.min() == 14:
            self.num2.clearer()
        if self.clk.min() == 14:
            self.num2.tizennegy()
        if self.clk.min() == 15:
            self.num2.clearer()
        if self.clk.min() == 15:
            self.num2.tizenot()
        if self.clk.min() == 16:
            self.num2.clearer()
        if self.clk.min() == 16:
            self.num2.tizenhat()
        if self.clk.min() == 17:
            self.num2.clearer()
        if self.clk.min() == 17:
            self.num2.tizenhet()
        if self.clk.min() == 18:
            self.num2.clearer()
        if self.clk.min() == 18:
            self.num2.tizennyolc()
        if self.clk.min() == 19:
            self.num2.clearer()
        if self.clk.min() == 19:
            self.num2.tizenkilenc()
        if self.clk.min() == 20:
            self.num2.clearer()
        if self.clk.min() == 20:
            self.num2.husz()
        if self.clk.min() == 21:
            self.num2.clearer()
        if self.clk.min() == 21:
            self.num2.huszonegy()
        if self.clk.min() == 22:
            self.num2.clearer()
        if self.clk.min() == 22:
            self.num2.huszonketto()
        if self.clk.min() == 23:
            self.num2.clearer()
        if self.clk.min() == 23:
            self.num2.huszonharom()
        if self.clk.min() == 24:
            self.num2.clearer()
        if self.clk.min() == 24:
            self.num2.huszonnegy()
        if self.clk.min() == 25:
            self.num2.clearer()
        if self.clk.min() == 25:
            self.num2.huszonot()
        if self.clk.min() == 26:
            self.num2.clearer()
        if self.clk.min() == 26:
            self.num2.huszonhat()
        if self.clk.min() == 27:
            self.num2.clearer()
        if self.clk.min() == 27:
            self.num2.huszonhet()
        if self.clk.min() == 28:
            self.num2.clearer()
        if self.clk.min() == 28:
            self.num2.huszonnyolc()
        if self.clk.min() == 29:
            self.num2.clearer()
        if self.clk.min() == 29:
            self.num2.huszonkilenc()
        if self.clk.min() == 30:
            self.num2.clearer()
        if self.clk.min() == 30:
            self.num2.harminc()
        if self.clk.min() == 31:
            self.num2.clearer()
        if self.clk.min() == 31:
            self.num2.harmincegy()
        if self.clk.min() == 32:
            self.num2.clearer()
        if self.clk.min() == 32:
            self.num2.harmincketto()
        if self.clk.min() == 33:
            self.num2.clearer()
        if self.clk.min() == 33:
            self.num2.harminncharom()
        if self.clk.min() == 34:
            self.num2.clearer()
        if self.clk.min() == 34:
            self.num2.harmincnegy()
        if self.clk.min() == 35:
            self.num2.clearer()
        if self.clk.min() == 35:
            self.num2.harmincot()
        if self.clk.min() == 36:
            self.num2.clearer()
        if self.clk.min() == 36:
            self.num2.harminchat()
        if self.clk.min() == 37:
            self.num2.clearer()
        if self.clk.min() == 37:
            self.num2.harminchet()
        if self.clk.min() == 38:
            self.num2.clearer()
        if self.clk.min() == 38:
            self.num2.harmincnyolc()
        if self.clk.min() == 39:
            self.num2.clearer()
        if self.clk.min() == 39:
            self.num2.harminckilenc()
        if self.clk.min() == 40:
            self.num2.negyven()
        if self.clk.min() == 41:
            self.num2.clearer()
        if self.clk.min() == 41:
            self.num2.negyvenegy()
        if self.clk.min() == 42:
            self.num2.clearer()
        if self.clk.min() == 42:
            self.num2.negyvenketto()
        if self.clk.min() == 43:
            self.num2.clearer()
        if self.clk.min() == 43:
            self.num2.negyvenharom()
        if self.clk.min() == 44:
            self.num2.clearer()
        if self.clk.min() == 44:
            self.num2.negyvennegy()
        if self.clk.min() == 45:
            self.num2.clearer()
        if self.clk.min() == 45:
            self.num2.negyvenot()
        if self.clk.min() == 46:
            self.num2.clearer()
        if self.clk.min() == 46:
            self.num2.negyvenhat()
        if self.clk.min() == 47:
            self.num2.clearer()
        if self.clk.min() == 47:
            self.num2.negyvenhet()
        if self.clk.min() == 48:
            self.num2.clearer()
        if self.clk.min() == 48:
            self.num2.negyvennyolc()
        if self.clk.min() == 49:
            self.num2.clearer()
        if self.clk.min() == 49:
            self.num2.negyvenkilenc()
        if self.clk.min() == 50:
            self.num2.clearer()
        if self.clk.min() == 50:
            self.num2.otven()
        if self.clk.min() == 51:
            self.num2.clearer()
        if self.clk.min() == 51:
            self.num2.otvenegy()
        if self.clk.min() == 52:
            self.num2.clearer()
        if self.clk.min() == 52:
            self.num2.otvenketto()
        if self.clk.min() == 53:
            self.num2.clearer()
        if self.clk.min() == 53:
            self.num2.otvenharom()
        if self.clk.min() == 54:
            self.num2.clearer()
        if self.clk.min() == 54:
            self.num2.otvennegy()
        if self.clk.min() == 55:
            self.num2.clearer()
        if self.clk.min() == 55:
            self.num2.otvenot()
        if self.clk.min() == 56:
            self.num2.clearer()
        if self.clk.min() == 56:
            self.num2.otvenhat()
        if self.clk.min() == 57:
            self.num2.clearer()
        if self.clk.min() == 57:
            self.num2.otvenhet()
        if self.clk.min() == 58:
            self.num2.clearer()
        if self.clk.min() == 58:
            self.num2.otvennyolc()
        if self.clk.min() == 59:
            self.num2.clearer()
        if self.clk.min() == 59:
            self.num2.otvenkilenc()

    def writeHour(self):
        self.kirajzoloora22()

    def kirajzoloora22(self):
        if self.clk.hour24() == 0:
            self.num3.clearer()
        if self.clk.hour24() == 0:
            self.num3.nulla()
        if self.clk.hour24() == 1:
            self.num3.clearer()
        if self.clk.hour24() == 1:
            self.num3.egy()
        if self.clk.hour24() == 2:
            self.num3.clearer()
        if self.clk.hour24() == 2:
            self.num3.ketto()
        if self.clk.hour24() == 3:
            self.num3.clearer()
        if self.clk.hour24() == 3:
            self.num3.harom()
        if self.clk.hour24() == 4:
            self.num3.clearer()
        if self.clk.hour24() == 4:
            self.num3.negy()
        if self.clk.hour24() == 5:
            self.num3.clearer()
        if self.clk.hour24() == 5:
            self.num3.ot()
        if self.clk.hour24() == 6:
            self.num3.clearer()
        if self.clk.hour24() == 6:
            self.num3.hat()
        if self.clk.hour24() == 7:
            self.num3.clearer()
        if self.clk.hour24() == 7:
            self.num3.het()
        if self.clk.hour24() == 8:
            self.num3.clearer()
        if self.clk.hour24() == 8:
            self.num3.nyolc()
        if self.clk.hour24() == 9:
            self.num3.clearer()
        if self.clk.hour24() == 9:
            self.num3.kilenc()
        if self.clk.hour24() == 10:
            self.num3.clearer()
        if self.clk.hour24() == 10:
            self.num3.tiz()
        if self.clk.hour24() == 11:
            self.num3.clearer()
        if self.clk.hour24() == 11:
            self.num3.tizenegy()
        if self.clk.hour24() == 12:
            self.num3.clearer()
        if self.clk.hour24() == 12:
            self.num3.tizenketto()
        if self.clk.hour24() == 13:
            self.num3.clearer()
        if self.clk.hour24() == 13:
            self.num3.tizenharom()
        if self.clk.hour24() == 14:
            self.num3.clearer()
        if self.clk.hour24() == 14:
            self.num3.tizennegy()
        if self.clk.hour24() == 15:
            self.num3.clearer()
        if self.clk.hour24() == 15:
            self.num3.tizenot()
        if self.clk.hour24() == 16:
            self.num3.clearer()
        if self.clk.hour24() == 16:
            self.num3.tizenhat()
        if self.clk.hour24() == 17:
            self.num3.clearer()
        if self.clk.hour24() == 17:
            self.num3.tizenhet()
        if self.clk.hour24() == 18:
            self.num3.clearer()
        if self.clk.hour24() == 18:
            self.num3.tizennyolc()
        if self.clk.hour24() == 19:
            self.num3.clearer()
        if self.clk.hour24() == 19:
            self.num3.tizenkilenc()
        if self.clk.hour24() == 20:
            self.num3.clearer()
        if self.clk.hour24() == 20:
            self.num3.husz()
        if self.clk.hour24() == 21:
            self.num3.clearer()
        if self.clk.hour24() == 21:
            self.num3.huszonegy()
        if self.clk.hour24() == 22:
            self.num3.clearer()
        if self.clk.hour24() == 22:
            self.num3.huszonketto()
        if self.clk.hour24() == 23:
            self.num3.clearer()
        if self.clk.hour24() == 23:
            self.num3.huszonharom()
        if self.clk.hour24() == 24:
            self.num3.clearer()
        if self.clk.hour24() == 24:
            self.num3.huszonnegy()

    def keret(self):
        self.t2.penup()
        self.t2.pendown()
        self.t2.penup()
        self.t2.left(180)
        self.t2.forward(50)
        self.t2.right(90)
        self.t2.forward(250)
        self.t2.left(90)
        self.t2.pendown()
        self.t2.begin_fill()
        self.t2.fillcolor("black")
        self.t2.width(20)
        self.t2.forward(500)
        self.t2.circle(250, 180)
        self.t2.forward(800)
        self.t2.circle(250, 180)
        self.t2.forward(550)
        self.t2.end_fill()
        self.t2.penup()
        self.t2.pencolor("gray")
        self.t2.right(90)
        self.t2.forward(2)
        self.t2.left(90)
        self.t2.pendown()
        self.t2.forward(250)
        self.t2.circle(260, 180)
        self.t2.forward(800)
        self.t2.circle(260, 180)
        self.t2.forward(600)

        self.t2.penup()
        self.t2.home()
        self.t2.forward(450)
        self.t2.right(90)
        self.t2.forward(225)
        self.t2.left(90)

        self.t2.pendown()
        self.t2.begin_fill()
        self.t2.fillcolor("black")
        self.t2.width(15)
        self.t2.penup()
        self.t2.forward(160)
        self.t2.pendown()
        self.t2.forward(140)
        self.t2.circle(125, 180)
        self.t2.forward(125)
        self.t2.circle(125, 180)
        self.t2.forward(10)
        self.t2.end_fill()

        self.t2.penup()
        self.t2.home()
        self.t2.left(180)
        self.t2.forward(125)
        self.t2.left(90)
        self.t2.forward(50)
        self.t2.pendown()
        self.t2.pencolor("lime")
        for i in range(360):
            self.t2.forward(1)
            self.t2.right(8)

        self.t2.penup()
        self.t2.right(180)
        self.t2.forward(125)
        self.t2.left(90)
        self.t2.forward(8)
        self.t2.pendown()
        for i in range(360):
            self.t2.forward(1)
            self.t2.right(8)





    def __init__(self):
        self.scr.bgcolor("orange")
        self.secturtle._delay(0)
        self.secturtle.speed(0)
        self.minturtle._delay(0)
        self.minturtle.speed(0)
        self.hourturtle._delay(0)
        self.hourturtle.speed(0)
        self.clk.setOnSecondChangeListener(self.writeSec)
        self.clk.setOnMinuteChangeListener(self.writeMin)
        self.clk.setOnHourChangeListener(self.writeHour)
        self.keret()
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
# ezt látod?