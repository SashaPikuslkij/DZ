import random

class Human:
    def __init__(self, name="Human", gun=None, job=None):
        self.name = name
        self.gun = gun
        self.money = 120
        self.gladness = 50
        self.job = job

    def shopping(self, manage):
        if self.gun.shoot():
            pass
        else:
            if self.gun.bullet < 0:
                manage = 'bullet'
            else:
                self.buy_bullet()
                return

    def days_indexes(self, day: object) -> object:
        day = f"Today the {day} of {self.name}'s life"
        print(f'{day:=^50}')

        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:+^50}')
        print(f'Money = {self.money}')
        print(f'Gladness = {self.gladness}')

        gun_indexes = f"{self.gun.brand} gun indexes"
        print(f'{gun_indexes:^50}')
        print(f'Bullet - {self.gun.bullet}')
        print(f'damage = {self.gun.damage}')

        def is_alive(self):
            if self.gladness < 0:
                print("Depression…")
            return False
            if self.money < -500:
                print("......")
            return False

        def live(self, day):
            if self.is_alive() == False:
                return False
            if self.gun is None:
                self.get_gun()
                print(f"i bought a gun {self.gun.brand}")
            if self.job is None:
                self.get_job()
                print(f"I don't a job, going to get a job {self.job.job})"
                      f"with salary {self.job.salary}")
            self.days_indexes(day)
            dice = random.randint(1, 2)
            if dice == 1:
                print("Let's go shooting")
                self.shoot()
            elif dice == 2:
                print('Start working')
                self.work()


    def get_gun(self):
        self.gun = Gun(brands_of_gun)

    def days_indexes(self, day: object) -> object:
        day = f"Today the {day} of {self.name}'s life"
        print(f'{day:=^50}')

        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:+^50}')
        print(f'Money = {self.money}')
        print(f'Gladness = {self.gladness}')


        gun_indexes = f"{self.car.brand} car indexes"
        print(f'{gun_indexes:^50}')
        print(f'Bullet - {self.gun.bullet}')
        print(f'Damage = {self.gun.damage}')

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

class Gun:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.bullet = brand_list[self.brand]['bullet']
        self.damage = brand_list[self.brand]['damage']

brands_of_gun = {"GLock": {'bullet': 20, 'damage': 15},
                 "Beretta": {'bullet': 10, 'damage': 20},
                 "Pm": {'bullet': 8, 'damage': 25 },
                 "DeserEagle": {'bullet': 7, 'damage': 75 }}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['job_gladness']

job_list = {'C++': {'salary': 90, 'job_gladness': 3},
            'Python': {'salary': 50, 'job_gladness': 10},
            'Java': {'salary': 70, 'job_gladness': 7}}


def shooting(self):
    if self.gun.shoot():
        pass
    else:
        if self.gun.bullet < 0:
            self.shopping('bullet')
            return
        else:
            self.shoot()
            return
    self.money += self.job.salary
    self.gladness -= self.job.gladness

    nick = Human(name='Nick')
    for day in range(1, 8):
        if nick.live(day) == False:
            break


