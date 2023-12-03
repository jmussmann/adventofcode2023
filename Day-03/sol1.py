import sys

def main(argv):
    sol = 0
    lines = []
    with open(argv[0], "r") as f:
        data = f.read()
    for line in data.splitlines():
        lines.append(line)

    width = len(lines[0])
    height = len(lines)

    sol = []
    for y, line in enumerate(lines):
        canidate = []
        is_part = False
        for x, c in enumerate(line):
            if c.isnumeric():
                canidate.append(c)
                if check_is_part(x, y, width, height, lines):
                    is_part = True
            else:
                if is_part and len(canidate) > 0:
                    sol.append(int("".join(canidate)))
                canidate = []
                is_part = False
        if is_part and len(canidate) > 0:
            sol.append(int("".join(canidate)))
    print(sum(sol))


            

def check_is_part(pos_x, pos_y, width, height, lines):
    for i in range(-1, 2):
        for j in range(-1, 2):
            idx_x = pos_x + j
            idx_y = pos_y + i
            if idx_x >= 0 and idx_x < width and idx_y >= 0 and idx_y < height:
                el = lines[idx_y][idx_x]

                if el != "." and (not el.isnumeric() or i != 0):
                    return True

        

if __name__ == "__main__":
    main(sys.argv[1:])

