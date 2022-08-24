import os
from PIL import Image
print("between the following suggetions choose what hurts u")
print("a:headache  b:stomach ache  c:Back Pain  d:Neck Pain  e:Muscle Pain")
d={"a":"headache","b":"stomach ache","c":"Back Pain","d":"Neck Pain","e":"Muscle Pain"}
a=input("a or b or c or d or e :")
if a not in d:
    print("please choose a valid option")
    exit()
print("here is some medicines that may help your "+(d.get(a))+":")
for file in os.listdir('.'):
    if ( file.endswith('.jpeg') or file.endswith('.jpg')\
    or file.endswith('.png')) :
        f=Image.open(file)
        f=f.resize((300,300))
        f.save(file)
bg=Image.new('RGBA',(600,900),(255,255,255,250))
i=0
for file in os.listdir('.') :
    if ( file.endswith('.jpeg') or file.endswith('.jpg')\
    or file.endswith('.png')) and file.startswith(d.get(a)):
        globals()['s%s'%i]=Image.open(file)
        i+=1
i=0
for left in range (0,600,300):
    for top in range (0,900,300):
        x=(globals()['s%s'%i])
        bg.paste(x,(left,top))
        i+=1
bg.show()
