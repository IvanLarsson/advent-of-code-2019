import math 
#inputFile = r"C:\Users\ivan_\Documents\repos\AdventOfCode2019\dec1\test_input"
inputFile = r"C:\Users\ivan_\Documents\repos\AdventOfCode2019\dec1\real_input"
sum = 0

with open(inputFile) as f:
    for mass in f:
        mod = math.floor(float(mass)/3) - 2
        totModFuel = 0

        fuel = math.floor(mod/3) - 2
        if fuel <= 0 :
            continue
        else :
            totModFuel += fuel
            while True:
                fuelsFuel = math.floor(fuel/3) - 2
                if fuelsFuel <= 0 :
                    break
                else :
                    totModFuel += fuelsFuel
                    fuel = fuelsFuel

        sum += mod
        sum += totModFuel
     
print(sum)