import random


class Human:
    def __init__(self, name="Human", job=None, gun=None, car=None, shoot=None):
        self.name = name
        self.job = job
        self.car = car
        self.gun = gun
        self.money = 120
        self.gladness = 50
        self.satiety = 50
        self.shoot = shoot
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def to_repair(self):
        self.car.strenght += 100
        self.money -= 100

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_gun(self):
        self.gun = Gun(brands_of_gun)

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.gladness -= self.job.gladness
        self.money += self.job.salary
        self.satiety -= 5

    def shoot(self):
        if self.gun.shoot():
            pass
        else:
            if self.gun.bullet < 0:
                self.shopping('bullet')
                return
            else:
                self.to_repair()
                return



    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 50
            self.car.fuel += 100
        elif manage == 'bullet':
            print('bought bullet')
            self.money -= 20
            self.gun.bullet += 2
        elif manage == 'chill':
            print('chill')



    def to_repair(self):
        self.gun.damage += 10
        self.money -= 10

    def days_indexes(self, day: object) -> object:
        day = f"Today the {day} of {self.name}'s life"
        print(f'{day:=^50}')

        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:+^50}')
        print(f'Money = {self.money}')
        print(f'Gladness = {self.gladness}')

        car_indexes = f"{self.car.brand} car indexes"
        print(f'{car_indexes:^50}')
        print(f'Fuel - {self.car.fuel}')
        print(f'Strength = {self.car.strength}')

        gun_indexes = f"{self.gun.brand} gun indexes"
        print(f'{gun_indexes:^50}')
        print(f'Bullet - {self.gun.bullet}')
        print(f'Damage = {self.gun.damage}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression...')
            return False
        if self.money < -500:
            print('Bankrupt...')
            return False

    def live(self, day: object) -> object:
        if self.is_alive() == False:
            return False
        if self.car is None:
            self.get_car()
            print(f"i bought a car {self.car.brand}")
        if self.gun is None:
            self.get_gun()
            print(f"i bought a gun {self.gun.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't a job, going to get a job {self.job.job})"
                  f"with salary {self.job.salary}")


        def shoot(self):
            if self.gun.shoot():
                pass
            else:
                if self.gun.bullet < 0:
                    self.shopping('bullet')
                    return
                else:
                    self.to_repair()
                    return


        self.days_indexes(day)
        if self.satiety < 20:
            print('Time eat')
            self.eat()
        elif self.money < 5:
            print('Time work')
            self.work()
        elif self.gun.damage < 0:
            print('I need to repair my gun')
            self.to_repair()
        dice = random.randint(1, 2)
        if dice == 1:
            print("Let's go shoot")
            self.shoot()
        elif dice == 2:
            print('Start working')
            self.work()


class Gun:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.bullet = brand_list[self.brand]['bullet']
        self.damage = brand_list[self.brand]['damage']

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['job_gladness']

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= 10
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False

brands_of_car = {"BMW": {'fuel': 100, 'strength': 100, 'consumption': 6},
                 "Lada": {'fuel': 50, 'strength': 30, 'consumption': 9},
                 "Ford": {'fuel': 80, 'strength': 150, 'consumption': 8},
                 "Audi": {'fuel': 70, 'strength': 120, 'consumption': 7}}


job_list = {'C++': {'salary': 90, 'job_gladness': 3},
            'Python': {'salary': 50, 'job_gladness': 10},
            'Java': {'salary': 70, 'job_gladness': 7}}


brands_of_gun = {"GLock": {'bullet': 20, 'damage': 15},
                 "Beretta": {'bullet': 10, 'damage': 20},
                 "Pm": {'bullet': 8, 'damage': 25 },
                 "DesertEagle": {'bullet': 7, 'damage': 75 }}

nick = Human(name='Sasha')
for day in range(1, 8):
    if not nick.live(day):
        break