import random


class Human:
    def __int__(self, name="Human", car=None, job=None, home=None):
        self.name = name
        self.gladness = 0
        self.progress = 0
        self.alive = True
        self.money = 100
        self.job = job_list
        self.home = home
        self.car = car

    def get_home(self):
        pass

    def get_job(self):
        pass

    class House:
        def __init__(self):
            self.mess = 0
            self.food = 0

    class Job:
        def __init__(self, job_list):
            self.job = random.choice(list(job_list))
            self.salary = job_list[self.job]["salary"]
            self.gladness_less = job_list[self.job]["gladness_less"]

    job_list = {
        "Java developer":{"salary": 50, "gladness_less": 10},
        "Python developer":{"salary": 40, "gladness_less": 3},
        "C++ developer":{"salary": 45, "gladness_less": 25},
    }


    brands_of_car = {
        "BMW": {"fuel": 100, "strength":100, "consumption": 6},
        "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
        "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
        "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
        }

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def to_study(self):
        print("time to study...")
        self.progress += 0.2
        self.gladness -= 2

    def to_sleep(self):
        print("time to sleep...")
        self.gladness += 3

    def to_chill(self):
        print("time to chill...")
        self.gladness += 5
        self.progress += 0.3

    def is_alive(self):
        if self.progress <= -0.5:
            print("cast out...")
            self.alive = False
        elif self.gladness == 0:
            print("depression")
            self.to_chill()
        elif self.progress >= 5:
            print("externally...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness} ")
        print(f"Progress = {self.progress} ")

    def live(self, day):
        day = "Day" + str(day) + "or" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

class Job:
 def __init__(self, job_list):
      self.job=random.choice(list(job_list))
      self.salary=job_list[self.job]
      ["salary"]
      self.gladness_less=job_list[self.job]
      ["gladness_less"]

def get_job(self):
    if self.car.drive():
       pass
    else:
       self.to_repair()
       return
    self.job = Job(job_list)

job_list = {
 "Java developer": {"salary":50, "gladness_less": 10 },
 "Python developer": {"salary":40, "gladness_less": 3 },
 "C++ developer": {"salary":45, "gladness_less": 25 },
 "Rust developer": {"salary":70, "gladness_less": 1 },
 }

def is_alive(self):
    if self.gladness<0:
       print("Depression…")
       return False
    if self.satiety<0:
       print("Dead…")
       return False
    if self.money<-500:
       print("Bankrupt…")
       return False

nick = Human (name="sasha")

for day in range(365):
    if nick.alive(day) == False:
        break


