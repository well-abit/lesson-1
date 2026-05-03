import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 10
        self.sadness = 1
        self.progress = 0
        self.alive = True



    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.sadness += 5

    def to_sleep(self):
        print("I'll sleep")
        self.gladness += 3
        self.sadness -= 5

    def to_playPC(self):
        print("I'd play")
        self.progress -= 0.05
        self.gladness += 5
        self.sadness -= 5

    def to_chill(self):
        print("Rest time")
        self.gladness += 3
        self.progress -= 0.02

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.sadness < -50:
            print("killing oneself")
            self.alive = False
        elif self.progress > 5:
            print("w")

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"progress = {self.progress}")
        print(f"Sadness = {self.sadness}")

    def live(self, day):
        day = f"Day {day} of {self.name} live"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_chill()
        self.end_of_day()
        self.is_alive()



personage = Student(name= "Vasya")

for day in range(365):
    if personage.alive == False:
        break
    personage.live(day)
    if personage.progress > 5:
        print("good study year")
        break