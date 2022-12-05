import bisect

def challenge1():
    l = []
    with open("../Input/day1_input.txt", 'r') as o:
        total_calories = 0
        for line in o:
            if line.strip() == "":
                bisect.insort(l, total_calories)
                total_calories = 0
            else:
                total_calories += int(line.strip())

    print(f"Highest Calorie Value: {l[-1]}")

def challenge2():
    l = []
    with open("../Input/day1_input.txt", 'r') as o:
        total_calories = 0
        for line in o:
            if line.strip() == "":
                bisect.insort(l, total_calories)
                total_calories = 0
            else:
                total_calories += int(line.strip())

    print(f"Top 3 Calorie Value: {sum(l[-3:])}") 

challenge1()
challenge2()