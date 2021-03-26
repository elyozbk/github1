#1dan 100gacha sonlar royxatidan bitta tasodifiy son tushib qoldi.Mana shu sonni topuvchi datur yozing.

#1 dan 1000 gacha bolgan sonlar royxatidan bitta tasodifiy son tushurib beruvchi datur
import random
n = 100
numbers = list(range(1,n+1))
x = numbers.pop(random.randint(1,n+1))
print(x)

#royhat orqali tasodifiy sonni topuvchi dastur
numbers2 = list(range(1,1+n))
print(sum(numbers2)-sum(numbers))