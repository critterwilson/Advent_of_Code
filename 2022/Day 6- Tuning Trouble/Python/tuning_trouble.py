def is_unique_chars(s:str) -> bool:
    print(s)
    
def challenge1(input:str) -> int:
    print(input)
    for i in range(4, len(input)):
        print(i, input[i:i+4])
        if len(set(input[i:i+4])) == 4:
            print(input[i:i+4])
            return i + 4        

def challenge2(input:str):
    for i in range(14, len(input)):
        print(i, input[i:i+14])
        if len(set(input[i:i+14])) == 14:
            print(input[i:i+14])
            return i + 14        

if __name__ == "__main__":
    o = open("../Input/day6_input.txt")
    input = o.readline()
    o.close()

    print(challenge1(input))
    print(challenge2(input))