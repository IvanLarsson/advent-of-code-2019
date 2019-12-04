inputFile = r"C:\Users\ivan_\Documents\repos\AdventOfCode2019\dec2\real_input"
#inputFile = r"C:\Users\ivan_\Documents\repos\AdventOfCode2019\dec2\test_input"

with open(inputFile) as f:
    data = f.read()
    result = [x.strip() for x in data.split(',')]
    result = list(map(int, result))

    for i in range(0, len(result), 4 ):
        cmd = result[i]
        if cmd == 99  :
            break

        value1 = result[i+1]
        value2 = result[i+2]
        newPos = result[i+3]   

        if (100 * (value1 + value2)) == 19690720 : 
            print("found shit")


        if cmd == 1 :
            result[newPos] = result[value1] + result[value2]
        elif cmd == 2 :
            result[newPos] = result[value1] * result[value2] 


    print(result[0])