from textwrap import dedent

class Plant ( object ):

    def __init__( self ):
        self.current_growth = 3
        self.growth_rate = 1
        self.max_growth = 20

    def report_growth( self ):
        if self.growth_rate >= 5:
            print("Time is ticking...the plants are growing really fast now!")
        plant_percent = int((self.current_growth*100)/self.max_growth)
        print("The plants now cover", plant_percent, "% of the building.")

    def check_over_growth( self ):
        """check whether game over"""
        if self.current_growth > self.max_growth:
            return True
        else:
            return False

    def grow( self ):
        self.current_growth += self.growth_rate
        print("The plants are growing.")

    def wither( self ):
        self.current_growth -= self.growth_rate
        print("The plants die a bit.")

    def increase_growth_rate( self ):
        self.growth_rate += 0.5
        print("The plants are growing faster")

    def decrease_growth_rate( self ):
        self.growth_rate -= 1
        if self.growth_rate < 0:
            self.growth_rate = 0.1
        print("The plants are growing slower")

    def grow_and_report( self ):
        self.grow()
        self.report_growth()

    def wither_and_report( self ):
        self.wither()
        self.report_growth()

    def increase_growth_rate_and_report( self ):
        self.increase_growth_rate()
        self.report_growth()

    def decrease_growth_rate_and_report( self ):
        self.decrease_growth_rate()
        self.report_growth()

plant = Plant()
