import random
class Warriors(object):
    def __init__(self, name, health, attack_max, block_max):
        self.name = name
        self.health = health
        self.attack_max = attack_max
        self.block_max = block_max
    # A warrior can attack with a random damage + 5 
    def Attack(self):
        random_num = random.random()
        random_attack = self.attack_max * random_num + 5
        return random_attack
    # A warrior can block with a random defense shield
    def Block(self):
        random_num = random.random()
        random_block = self.block_max * random_num
        return random_block

class Battle(object):
    def fight(warrior1, warrior2):
        print("The warriors are about to Battle!!!")
        print("{} has {} health".format(warrior1.name, warrior1.health))
        print("{} has {} health".format(warrior2.name, warrior2.health))
        death = False
        while death == False:
            warrior2.health = warrior2.health - (warrior1.Attack() - warrior2.Block())
            print("{} now has {} health because of the attack from {}".format(warrior2.name, warrior2.health, warrior1.name))
            if warrior2.health <= 0:
                print("{} is dead because they have {} health".format(warrior2.name, warrior2.health))
                break
            warrior1.health = warrior1.health - (warrior2.Attack() - warrior1.Block())
            print("{} now has {} health because of the attack from {}".format(warrior1.name, warrior1.health, warrior2.name))
            if warrior1.health <= 0:
                print("{} is dead because they have {} health".format(warrior1.name, warrior1.health))
                break 

