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
        for x, c in enumerate(line):
            if c == "*":
                sol.append(get_adj_numbers_prod(x, y, width, height, lines))
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

def get_adj_numbers_prod(pos_x, pos_y, width, height, lines):
    
    nums=[]
    for i in range(-1, 2):
        idx_first_num = None
        for j in range(-1, 2):
            idx_x = pos_x + j
            idx_y = pos_y + i
            if idx_x >= 0 and idx_x < width and idx_y >= 0 and idx_y < height:
                el = lines[idx_y][idx_x]
                if el.isnumeric():
                    num, idx_start = get_comp_number(idx_x, idx_y, lines)
                    if idx_first_num is None or idx_first_num != idx_start:
                        nums.append(num)
                        idx_first_num = idx_start
    if len(nums) == 2:
        return nums[0] * nums[1]
    return 0

def get_comp_number(pos_x, pos_y, lines):

    idx = pos_x

    while idx > 0:
        if lines[pos_y][idx-1].isnumeric():
            idx -= 1
        else:
            break
    idx_start = idx
    
    canidate = []
    while idx < len(lines[pos_y]):
        if lines[pos_y][idx].isnumeric():
            canidate.append(lines[pos_y][idx])
            idx +=1
        else:
            break
    return int("".join(canidate)), idx_start


if __name__ == "__main__":
    main(sys.argv[1:])

