from turtle import *
from datetime import *
from j_clock import *
class Numbers2:
    scr = Screen()
    clk = Clock(scr)
    t1 = Turtle()


    def szamjegyvalto(self):
        self.t1.home()
        self.t1.penup()
        self.t1.backward(300)
        self.t1.pendown()

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

    def nulla(self):
        self.tizespoz()
        self.digi1()
        self.t1.left(90)
        self.t1.penup()
        self.t1.forward(25)
        self.t1.pendown()
        self.digi2()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(35)
        self.t1.pendown()
        self.digi3()
        self.t1.penup()
        self.t1.forward(133)
        self.t1.right(90)
        self.t1.forward(25)
        self.t1.pendown()
        self.digi4()
        self.t1.penup()
        self.t1.forward(170)
        self.t1.right(90)
        self.t1.forward(17.5)
        self.t1.left(90)
        self.t1.pendown()
        self.digi5()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(33)
        self.t1.pendown()
        self.digi6()
        self.t1.penup()
        self.t1.forward(134.5)
        self.t1.right(90)
        self.t1.forward(30)
        self.t1.pendown()
        self.digi7()
        self.reset()

    def digi1(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.end_fill()
        self.t1.back(25)
        self.t1.left(45)

    def digi2(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digi3(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digi4(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digi5(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digi6(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digi7(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digit1(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digit2(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digit3(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digit4(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digit5(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digit6(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digit7(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def clearer(self):
        self.t1.clear()

    def reset(self):
        self.t1.penup()
        self.t1.home()
        self.t1.pendown()

    def tizespoz(self):
        self.t1.penup()
        self.t1.backward(300)
        self.t1.pendown()


    def egy(self):
        self.tizespoz()
        self.digit1()
        self.t1.left(90)
        self.t1.penup()
        self.t1.forward(25)
        self.t1.pendown()
        self.digit2()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(35)
        self.t1.pendown()
        self.digit3()
        self.t1.penup()
        self.t1.forward(133)
        self.t1.right(90)
        self.t1.forward(25)
        self.t1.pendown()
        self.digit4()
        self.t1.penup()
        self.t1.forward(170)
        self.t1.right(90)
        self.t1.forward(17.5)
        self.t1.left(90)
        self.t1.pendown()
        self.digit5()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(33)
        self.t1.pendown()
        self.digit6()
        self.t1.penup()
        self.t1.forward(134.5)
        self.t1.right(90)
        self.t1.forward(30)
        self.t1.pendown()
        self.digit7()
        self.reset()

    def ketto(self):
        self.tizespoz()
        self.szam1()
        self.t1.left(90)
        self.t1.penup()
        self.t1.forward(25)
        self.t1.pendown()
        self.szam2()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(35)
        self.t1.pendown()
        self.szam3()
        self.t1.penup()
        self.t1.forward(133)
        self.t1.right(90)
        self.t1.forward(25)
        self.t1.pendown()
        self.szam4()
        self.t1.penup()
        self.t1.forward(170)
        self.t1.right(90)
        self.t1.forward(17.5)
        self.t1.left(90)
        self.t1.pendown()
        self.szam5()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(33)
        self.t1.pendown()
        self.szam6()
        self.t1.penup()
        self.t1.forward(134.5)
        self.t1.right(90)
        self.t1.forward(30)
        self.t1.pendown()
        self.szam7()
        self.reset()

    def szam1(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)


    def szam2(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def szam3(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def szam4(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def szam5(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def szam6(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def szam7(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def harom(self):
        self.tizespoz()
        self.valami1()
        self.t1.left(90)
        self.t1.penup()
        self.t1.forward(25)
        self.t1.pendown()
        self.valami2()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(35)
        self.t1.pendown()
        self.valami3()
        self.t1.penup()
        self.t1.forward(133)
        self.t1.right(90)
        self.t1.forward(25)
        self.t1.pendown()
        self.valami4()
        self.t1.penup()
        self.t1.forward(170)
        self.t1.right(90)
        self.t1.forward(17.5)
        self.t1.left(90)
        self.t1.pendown()
        self.valami5()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(33)
        self.t1.pendown()
        self.valami6()
        self.t1.penup()
        self.t1.forward(134.5)
        self.t1.right(90)
        self.t1.forward(30)
        self.t1.pendown()
        self.valami7()
        self.reset()

    def valami1(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def valami2(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def valami3(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def valami4(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def valami5(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def valami6(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def valami7(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def negy(self):
        self.tizespoz()
        self.abc1()
        self.t1.left(90)
        self.t1.penup()
        self.t1.forward(25)
        self.t1.pendown()
        self.abc2()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(35)
        self.t1.pendown()
        self.abc3()
        self.t1.penup()
        self.t1.forward(133)
        self.t1.right(90)
        self.t1.forward(25)
        self.t1.pendown()
        self.abc4()
        self.t1.penup()
        self.t1.forward(170)
        self.t1.right(90)
        self.t1.forward(17.5)
        self.t1.left(90)
        self.t1.pendown()
        self.abc5()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(33)
        self.t1.pendown()
        self.abc6()
        self.t1.penup()
        self.t1.forward(134.5)
        self.t1.right(90)
        self.t1.forward(30)
        self.t1.pendown()
        self.abc7()
        self.reset()

    def abc1(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def abc2(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def abc3(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def abc4(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def abc5(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def abc6(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def abc7(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def ot(self):
        self.tizespoz()
        self.asd1()
        self.t1.left(90)
        self.t1.penup()
        self.t1.forward(25)
        self.t1.pendown()
        self.asd2()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(35)
        self.t1.pendown()
        self.asd3()
        self.t1.penup()
        self.t1.forward(133)
        self.t1.right(90)
        self.t1.forward(25)
        self.t1.pendown()
        self.asd4()
        self.t1.penup()
        self.t1.forward(170)
        self.t1.right(90)
        self.t1.forward(17.5)
        self.t1.left(90)
        self.t1.pendown()
        self.asd5()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(33)
        self.t1.pendown()
        self.asd6()
        self.t1.penup()
        self.t1.forward(134.5)
        self.t1.right(90)
        self.t1.forward(30)
        self.t1.pendown()
        self.asd7()
        self.reset()

    def asd1(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def asd2(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def asd3(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def asd4(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def asd5(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def asd6(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def asd7(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def hat(self):
        self.half1()
        self.t1.left(90)
        self.t1.penup()
        self.t1.forward(25)
        self.t1.pendown()
        self.half2()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(35)
        self.t1.pendown()
        self.half3()
        self.t1.penup()
        self.t1.forward(133)
        self.t1.right(90)
        self.t1.forward(25)
        self.t1.pendown()
        self.half4()
        self.t1.penup()
        self.t1.forward(170)
        self.t1.right(90)
        self.t1.forward(17.5)
        self.t1.left(90)
        self.t1.pendown()
        self.half5()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(33)
        self.t1.pendown()
        self.half6()
        self.t1.penup()
        self.t1.forward(134.5)
        self.t1.right(90)
        self.t1.forward(30)
        self.t1.pendown()
        self.half7()
        self.reset()

    def half1(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def half2(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def half3(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def half4(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def half5(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def half6(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def half7(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def het(self):
        self.nemtudom1()
        self.t1.left(90)
        self.t1.penup()
        self.t1.forward(25)
        self.t1.pendown()
        self.nemtudom2()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(35)
        self.t1.pendown()
        self.nemtudom3()
        self.t1.penup()
        self.t1.forward(133)
        self.t1.right(90)
        self.t1.forward(25)
        self.t1.pendown()
        self.nemtudom4()
        self.t1.penup()
        self.t1.forward(170)
        self.t1.right(90)
        self.t1.forward(17.5)
        self.t1.left(90)
        self.t1.pendown()
        self.nemtudom5()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(33)
        self.t1.pendown()
        self.nemtudom6()
        self.t1.penup()
        self.t1.forward(134.5)
        self.t1.right(90)
        self.t1.forward(30)
        self.t1.pendown()
        self.nemtudom7()
        self.reset()

    def nemtudom1(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def nemtudom2(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def nemtudom3(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def nemtudom4(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def nemtudom5(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def nemtudom6(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def nemtudom7(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def nyolc(self):
        self.digt1()
        self.t1.left(90)
        self.t1.penup()
        self.t1.forward(25)
        self.t1.pendown()
        self.digt2()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(35)
        self.t1.pendown()
        self.digt3()
        self.t1.penup()
        self.t1.forward(133)
        self.t1.right(90)
        self.t1.forward(25)
        self.t1.pendown()
        self.digt4()
        self.t1.penup()
        self.t1.forward(170)
        self.t1.right(90)
        self.t1.forward(17.5)
        self.t1.left(90)
        self.t1.pendown()
        self.digt5()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(33)
        self.t1.pendown()
        self.digt6()
        self.t1.penup()
        self.t1.forward(134.5)
        self.t1.right(90)
        self.t1.forward(30)
        self.t1.pendown()
        self.digt7()
        self.reset()

    def digt1(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digt2(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digt3(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digt4(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digt5(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digt6(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def digt7(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def kilenc(self):
        self.kapu1()
        self.t1.left(90)
        self.t1.penup()
        self.t1.forward(25)
        self.t1.pendown()
        self.kapu2()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(35)
        self.t1.pendown()
        self.kapu3()
        self.t1.penup()
        self.t1.forward(133)
        self.t1.right(90)
        self.t1.forward(25)
        self.t1.pendown()
        self.kapu4()
        self.t1.penup()
        self.t1.forward(170)
        self.t1.right(90)
        self.t1.forward(17.5)
        self.t1.left(90)
        self.t1.pendown()
        self.kapu5()
        self.t1.penup()
        self.t1.forward(125)
        self.t1.right(90)
        self.t1.forward(33)
        self.t1.pendown()
        self.kapu6()
        self.t1.penup()
        self.t1.forward(134.5)
        self.t1.right(90)
        self.t1.forward(30)
        self.t1.pendown()
        self.kapu7()
        self.reset()

    def kapu1(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def kapu2(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def kapu3(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def kapu4(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def kapu5(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def kapu6(self):
        self.t1.begin_fill()
        self.t1.fillcolor("Lime")

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)

    def kapu7(self):
        self.t1.begin_fill()
        self.t1.fillcolor(0, 0.05, 0)

        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)
        self.t1.left(45)
        self.t1.forward(100)
        self.t1.left(45)
        self.t1.forward(25)
        self.t1.left(90)
        self.t1.forward(25)

        self.t1.end_fill()

        self.t1.back(25)
        self.t1.left(45)


Numbers2()