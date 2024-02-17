class day: 
    def __init__(self) -> None:
        self.day = 1
        self.color = "Red"
        self.duration = 4000 #duration of message printed to screen
    def update(self):
        self.day += 1
        self.color = "Blue"