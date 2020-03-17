class Hero(object):
    def __init__(self, hp, mp, speed, strack, id):
        self.hp = hp
        self.mp = mp
        self.speed = speed
        self.strack = strack
        self.__id = id
        Hero.count += 1

    count = 0

class Chen(Hero):
    def __init__(self, hp, mp, speed, strack, id):
        super(Chen, self).__init__(hp, mp, speed, strack, id)
        self.name = "chen yao jing"

chen = Hero(150,100,350,75,2002)
li = Hero(120,130,350,50,1120)
print Hero.count
print li.mp

chen1 = Chen(150,100,350,75,2002)
print chen1.name, chen1.count