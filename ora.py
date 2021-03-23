from datetime import *
from turtle import *
from j_clock import *
from j_sampleclock import *

class Digitalclock:

    scr = Screen()
    clk = Clock(scr)

    secturtle = Turtle(shape="turtle")
    minturtle = Turtle(shape="turtle")
    hourturtle = Turtle(shape="turtle")

    def __init__(self):
        self.secturtle._delay(0)
        self.secturtle.speed(0)
        self.minturtle._delay(0)
        self.minturtle.speed(0)
        self.hourturtle._delay(0)
        self.hourturtle.speed(0)

        self.clk.setOnSecondChangeListener(self.writeSec)
        self.clk.setOnMinuteChangeListener(self.writeMin)
        self.clk.setOnHourChangeListener(self.writeHour)

        self.Sectest()

        self.scr.mainloop()

    def Sectest(self):

