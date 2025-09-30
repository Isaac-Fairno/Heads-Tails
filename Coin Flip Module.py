import coinflipdef
Heads = 0
Tails = 0

for x in range(0,100):
    coinflipdef.coinFlip()
    CompAnswer = coinflipdef.coinFlip()
    if CompAnswer == "Heads":
        Heads +=1
    else:
        Tails +=1
print(f"number of Heads: {Heads}\nNumber of Tails: {Tails}")
    
