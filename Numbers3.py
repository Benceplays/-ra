from turtle import *
from datetime import *
from j_clock import *
class Numbers3:
    scr = Screen()
    clk = Clock(scr)
    percturtle = Turtle()


    def szamjegyvalto(self):
        self.percturtle.home()
        self.percturtle.penup()
        self.percturtle.backward(300)
        self.percturtle.pendown()

    def tiz(self):
        self.nulla()
        self.szamjegyvalto()
        self.egy()

    def tizenegy(self):
        self.egy()
        self.szamjegyvalto()
        self.egy()

    def tizenketto(self):
        self.ketto()
        self.szamjegyvalto()
        self.egy()

    def tizenharom(self):
        self.harom()
        self.szamjegyvalto()
        self.egy()

    def tizennegy(self):
        self.negy()
        self.szamjegyvalto()
        self.egy()

    def tizenot(self):
        self.ot()
        self.szamjegyvalto()
        self.egy()

    def tizenhat(self):
        self.hat()
        self.szamjegyvalto()
        self.egy()

    def tizenhet(self):
        self.het()
        self.szamjegyvalto()
        self.egy()

    def tizennyolc(self):
        self.nyolc()
        self.szamjegyvalto()
        self.egy()

    def tizenkilenc(self):
        self.kilenc()
        self.szamjegyvalto()
        self.egy()

    def husz(self):
        self.nulla()
        self.szamjegyvalto()
        self.ketto()

    def huszonegy(self):
        self.egy()
        self.szamjegyvalto()
        self.ketto()

    def huszonketto(self):
        self.ketto()
        self.szamjegyvalto()
        self.ketto()

    def huszonharom(self):
        self.harom()
        self.szamjegyvalto()
        self.ketto()

    def huszonnegy(self):
        self.negy()
        self.szamjegyvalto()
        self.ketto()

    def huszonot(self):
        self.ot()
        self.szamjegyvalto()
        self.ketto()

    def huszonhat(self):
        self.hat()
        self.szamjegyvalto()
        self.ketto()

    def huszonhet(self):
        self.het()
        self.szamjegyvalto()
        self.ketto()

    def huszonnyolc(self):
        self.nyolc()
        self.szamjegyvalto()
        self.ketto()

    def huszonkilenc(self):
        self.kilenc()
        self.szamjegyvalto()
        self.ketto()

    def harminc(self):
        self.nulla()
        self.szamjegyvalto()
        self.harom()

    def harmincegy(self):
        self.egy()
        self.szamjegyvalto()
        self.harom()

    def harmincketto(self):
        self.ketto()
        self.szamjegyvalto()
        self.harom()

    def harminncharom(self):
        self.harom()
        self.szamjegyvalto()
        self.harom()

    def harmincnegy(self):
        self.negy()
        self.szamjegyvalto()
        self.harom()

    def harmincot(self):
        self.ot()
        self.szamjegyvalto()
        self.harom()

    def harminchat(self):
        self.hat()
        self.szamjegyvalto()
        self.harom()

    def harminchet(self):
        self.het()
        self.szamjegyvalto()
        self.harom()

    def harmincnyolc(self):
        self.nyolc()
        self.szamjegyvalto()
        self.harom()

    def harminckilenc(self):
        self.kilenc()
        self.szamjegyvalto()
        self.harom()

    def negyven(self):
        self.nulla()
        self.szamjegyvalto()
        self.negy()

    def negyvenegy(self):
        self.egy()
        self.szamjegyvalto()
        self.negy()

    def negyvenketto(self):
        self.ketto()
        self.szamjegyvalto()
        self.negy()

    def negyvenharom(self):
        self.harom()
        self.szamjegyvalto()
        self.harom()

    def negyvennegy(self):
        self.negy()
        self.szamjegyvalto()
        self.negy()

    def negyvenot(self):
        self.ot()
        self.szamjegyvalto()
        self.negy()

    def negyvenhat(self):
        self.hat()
        self.szamjegyvalto()
        self.negy()

    def negyvenhet(self):
        self.het()
        self.szamjegyvalto()
        self.negy()

    def negyvennyolc(self):
        self.nyolc()
        self.szamjegyvalto()
        self.negy()

    def negyvenkilenc(self):
        self.kilenc()
        self.szamjegyvalto()
        self.negy()

    def otven(self):
        self.nulla()
        self.szamjegyvalto()
        self.ot()

    def otvenegy(self):
        self.egy()
        self.szamjegyvalto()
        self.ot()

    def otvenketto(self):
        self.ketto()
        self.szamjegyvalto()
        self.ot()

    def otvenharom(self):
        self.harom()
        self.szamjegyvalto()
        self.ot()

    def otvennegy(self):
        self.negy()
        self.szamjegyvalto()
        self.ot()

    def otvenot(self):
        self.ot()
        self.szamjegyvalto()
        self.ot()

    def otvenhat(self):
        self.hat()
        self.szamjegyvalto()
        self.ot()

    def otvenhet(self):
        self.het()
        self.szamjegyvalto()
        self.ot()

    def otvennyolc(self):
        self.nyolc()
        self.szamjegyvalto()
        self.ot()

    def otvenkilenc(self):
        self.kilenc()
        self.szamjegyvalto()
        self.ot()

    def nulla(self):
        self.tizespoz()
        self.digi1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.digi2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.digi3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.digi4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.digi5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.digi6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.digi7()
        self.reset()

    def digi1(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.end_fill()
        self.percturtle.back(25)
        self.percturtle.left(45)

    def digi2(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digi3(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digi4(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digi5(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digi6(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digi7(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digit1(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digit2(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digit3(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digit4(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digit5(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digit6(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digit7(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def clearer(self):
        self.percturtle.clear()

    def reset(self):
        self.percturtle.penup()
        self.percturtle.home()
        self.percturtle.pendown()

    def tizespoz(self):
        self.percturtle.penup()
        self.percturtle.backward(600)
        self.percturtle.pendown()


    def egy(self):
        self.tizespoz()
        self.digit1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.digit2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.digit3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.digit4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.digit5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.digit6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.digit7()
        self.reset()

    def ketto(self):
        self.tizespoz()
        self.szam1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.szam2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.szam3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.szam4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.szam5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.szam6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.szam7()
        self.reset()

    def szam1(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)


    def szam2(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def szam3(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def szam4(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def szam5(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def szam6(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def szam7(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def harom(self):
        self.tizespoz()
        self.valami1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.valami2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.valami3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.valami4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.valami5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.valami6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.valami7()
        self.reset()

    def valami1(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def valami2(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def valami3(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def valami4(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def valami5(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def valami6(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def valami7(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def negy(self):
        self.tizespoz()
        self.abc1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.abc2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.abc3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.abc4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.abc5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.abc6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.abc7()
        self.reset()

    def abc1(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def abc2(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def abc3(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def abc4(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def abc5(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def abc6(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def abc7(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def ot(self):
        self.tizespoz()
        self.asd1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.asd2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.asd3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.asd4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.asd5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.asd6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.asd7()
        self.reset()

    def asd1(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def asd2(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def asd3(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def asd4(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def asd5(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def asd6(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def asd7(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def hat(self):
        self.half1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.half2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.half3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.half4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.half5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.half6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.half7()
        self.reset()

    def half1(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def half2(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def half3(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def half4(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def half5(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def half6(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def half7(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def het(self):
        self.nemtudom1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.nemtudom2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.nemtudom3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.nemtudom4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.nemtudom5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.nemtudom6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.nemtudom7()
        self.reset()

    def nemtudom1(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def nemtudom2(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def nemtudom3(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def nemtudom4(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def nemtudom5(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def nemtudom6(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def nemtudom7(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def nyolc(self):
        self.digt1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.digt2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.digt3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.digt4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.digt5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.digt6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.digt7()
        self.reset()

    def digt1(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digt2(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digt3(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digt4(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digt5(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digt6(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def digt7(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def kilenc(self):
        self.tizespoz()
        self.kapu1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.kapu2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.kapu3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.kapu4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.kapu5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.kapu6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.kapu7()
        self.reset()

    def kapu1(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def kapu2(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def kapu3(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def kapu4(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def kapu5(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def kapu6(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor("Lime")

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)

    def kapu7(self):
        self.percturtle.begin_fill()
        self.percturtle.fillcolor(0, 0.05, 0)

        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)
        self.percturtle.left(45)
        self.percturtle.forward(100)
        self.percturtle.left(45)
        self.percturtle.forward(25)
        self.percturtle.left(90)
        self.percturtle.forward(25)

        self.percturtle.end_fill()

        self.percturtle.back(25)
        self.percturtle.left(45)


    def percpoz (self):
        self.percturtle.penup()
        self.percturtle.backward(900)
        self.percturtle.pendown()

    def nulla2(self):
        self.percpoz()
        self.digi1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.digi2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.digi3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.digi4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.digi5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.digi6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.digi7()
        self.reset()

    def egy2(self):
        self.percpoz()
        self.digit1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.digit2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.digit3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.digit4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.digit5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.digit6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.digit7()
        self.reset()

    def ketto2(self):
        self.percpoz()
        self.szam1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.szam2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.szam3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.szam4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.szam5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.szam6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.szam7()
        self.reset()

    def harom2(self):
        self.percpoz()
        self.valami1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.valami2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.valami3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.valami4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.valami5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.valami6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.valami7()
        self.reset()

    def negy2(self):
        self.percpoz()
        self.abc1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.abc2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.abc3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.abc4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.abc5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.abc6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.abc7()
        self.reset()

    def ot2(self):
        self.percpoz()
        self.asd1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.asd2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.asd3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.asd4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.asd5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.asd6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.asd7()
        self.reset()

    def hat2(self):
        self.percpoz()
        self.half1()
        self.percturtle.left(90)
        self.percturtle.penup()
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.half2()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(35)
        self.percturtle.pendown()
        self.half3()
        self.percturtle.penup()
        self.percturtle.forward(133)
        self.percturtle.right(90)
        self.percturtle.forward(25)
        self.percturtle.pendown()
        self.half4()
        self.percturtle.penup()
        self.percturtle.forward(170)
        self.percturtle.right(90)
        self.percturtle.forward(17.5)
        self.percturtle.left(90)
        self.percturtle.pendown()
        self.half5()
        self.percturtle.penup()
        self.percturtle.forward(125)
        self.percturtle.right(90)
        self.percturtle.forward(33)
        self.percturtle.pendown()
        self.half6()
        self.percturtle.penup()
        self.percturtle.forward(134.5)
        self.percturtle.right(90)
        self.percturtle.forward(30)
        self.percturtle.pendown()
        self.half7()
        self.reset()

Numbers3()