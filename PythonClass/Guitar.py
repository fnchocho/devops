class Guitar:
    def __init__(self, name, NumStrings=6):
        self.name = name
        self.NumStrings = NumStrings
        self.play()      # init method called each time we create a new object
    def details(self):
        print(f'My {self.name} has {self.NumStrings} strings')
    
    def play(self):
        print("pam pam pam pam!!!")

class Electric_Guitar(Guitar):
    def __init__(self, name, NumStrings=8):
        super().__init__(name, NumStrings)
        self.NumStrings = 8
        self.playLouder()

    def playLouder(self):
        print("pam pam pam pam!!!".upper())
        

class Bass_Guitar(Guitar):
    def __init__(self, name, NumStrings=4):
        super().__init__(name, NumStrings)
        self.playBass()

    def playBass(self):
        print("BAM BAM BAM BAM BAM!!")
      

my_guitar = Bass_Guitar("Bass_Guitar", ) 
my_guitar.details()

