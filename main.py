import random
class Animal():
    def __init__(self,name):
      self.name = name
class chick(Animal):
    def __init__(self,name):
        super().__init__(self,name)
name=input("請輸入名字")
if name=='':
    name='雞肉飯'
n=Animal(name)
print(n.name,'誕生了')
class chicklife():
    def __init__(self,life):
        self.life=life
    def chicklifesad(self,life):
        self.life-=2
        print('HP-2',n.name,'覺得心痛')
        print('PH=',self.life)
    def chicklifepoison(self,life):
        self.life-=2
        print('HP-2',n.name,'中毒了')
        print('PH=',self.life)
    def chicklifenightmare(self,life):
        self.life-=2
        print('HP-2',n.name,'做惡夢了')
        print('PH=',self.life)
    def chicklifehurt(self,life):
        self.life-=2
        print('HP-2',n.name,'覺得不爽')
        print('PH=',self.life)    
    def chicklifeincrease(self,life):
        self.life+=1
        print('HP+1',n.name,'覺得開心')
        print('PH=',self.life)
life = 10
c=chicklife(life)
while True:
    a=input('1餵食,2睡覺,3玩耍,4打掃,5不理牠,6宰了牠')
    if a=='':
        print(n.name,'被抹殺了')
        break
    elif int(a)==1:
        x=random.randrange(2)
        if x==0:
            c.chicklifeincrease(life)
        else:
            c.chicklifepoison(life)
    elif int(a)==2:
        x=random.randrange(2)
        if x==0:
            c.chicklifeincrease(life)
        else:
            c.chicklifenightmare(life)
    elif int(a)==3:
        x=random.randrange(2)
        if x==0:
            c.chicklifeincrease(life)
        else:
            c.chicklifehurt(life)
    elif int(a)==4:
        c.chicklifeincrease(life)
    elif int(a)==5:
        c.chicklifesad(life)           
    elif int(a)==6:
        print(n.name,'die')
        break
    if c.life<=0:
        print(n.name,'die')
        break
