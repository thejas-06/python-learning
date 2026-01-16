# while loops
i = 1
while i<=10:
    x = 0
    while x<i:
        print("Thejas", end=" ")
        x += 1
    print("")     
    i += 1    


db = "1010"
trail  = 1
while trail<=3:
    pin =input(f"trail {trail} | pin-->")
    trail+=1
    if pin == db:
        print("correct")
        break
    else:
        print("incorrect")    
