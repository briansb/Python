import platform

class carClass:
    """"""

    def __init__(self, color, make, model, year):
        """Constructor"""
        self.color = color
        self.make = make
        self.model = model
        self.year = year

        if "Windows" in platform.platform():
            print("You're using Windows!")

        self.weight = self.getWeight(3)

    def getWeight(self, this):
        """"""
        return "2000 lbs"
