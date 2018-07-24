class Ninja:
    # ham tao constructor
    def __init__(self,n,s,d,h):
        self.name = n
        self.atk = s
        self.defense = d
        self.hp = h

    def print(self):
        print(self.name)
        print(self.atk)
        print(self.defense)
        print(self.hp)

    def attack(self, other):
        hploss=self.atk - (other.defense) / 2 
        other.hp = other.hp - hploss

ninja1 = Ninja("kakashi",7,9,10)
# n : obj
ninja2 = Ninja("Itachi",4,10,10)

ninja1.print()

print("******************")

ninja2.print()

print("Kakashi is attaking Itachi")
ninja1.atk(ninja2)
ninja2.print()