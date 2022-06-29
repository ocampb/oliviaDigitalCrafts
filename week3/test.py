class Dog:
    def __init__(self, name, energy, attention, profile):
        self.name = name
        self.energy = energy
        self.attention = attention
        self.profile = profile
    def updateEnergy(self, updateAmount):
        self.energy = self.energy + updateAmount
    def listAttentionSpan(self):
        print ("Attention Span = " + str(self.attention))
    def listEnergy(self):
        print("Energy = " + str(self.energy))
    def listProfile(self):
        print (self.profile)



