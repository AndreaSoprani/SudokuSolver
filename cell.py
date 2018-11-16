
class Cell:
    def __init__(self, xPos, yPos, value, domain):
        self.value = value
        self.xPos = xPos
        self.yPos = yPos
        self.domain = domain

    def __str__(self):
        return self.value.str()

    def __setattr__(self, name, val):

        # the set value has to be in the domain and an already set value cannot be modified
        if name == "value":
            if self.value != 0:
                return
            if val in self.domain:
                self.value = val
                self.domain = [val]

        # domain cannot be modified directly
        if name == "domain":
            pass




