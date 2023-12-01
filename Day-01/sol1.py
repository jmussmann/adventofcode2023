import sys

def main(argv):
    sol = 0
    with open(argv[0], "r") as f:
        data = f.read()
    for line in data.splitlines():
        idx = search_digit(line)
        nex = int(line[idx])
        sol += nex*10
        while (idx := search_digit(line, idx+1)) > 0:
            nex = int(line[idx])
        sol += nex
    print(sol)
                

# returns the index of the next digit or -1 if there is no digit
def search_digit(arg, start=0):
    for i in range(start, len(arg)):
        if arg[i].isnumeric():
            return i
    return -1


if __name__ == "__main__":
    main(sys.argv[1:])

