import sys

def main(argv):
    DICT_MACHINE = initialize_dict_machine()
    sol = 0
    with open(argv[0], "r") as f:
        data = f.read()
    for line in data.splitlines():
        line = process_line(line, DICT_MACHINE)
        idx = search_digit(line)
        nex = int(line[idx])
        sol += nex*10
        while (idx := search_digit(line, idx+1)) > 0:
            nex = int(line[idx])
        sol += nex
    print("Solution", sol)


# returns the index of the next digit or -1 if there is no digit
def search_digit(arg, start=0):
    for i in range(start, len(arg)):
        if arg[i].isnumeric():
            return i
    return -1

def process_line(line, DICT_MACHINE):


    res = ""

    idx = 0
    while idx < len(line):
        i = 1
        if line[idx].isnumeric():
            s = line[idx]
            res += s
        elif len(line[idx:]) > 2:
            s, i = parse_string(line[idx:], DICT_MACHINE)
            res += s
        idx += i

    return res


def initialize_dict_machine():

    DICT = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    DICT_MACHINE = create_dict_state_machine(DICT)


    return DICT_MACHINE

def parse_string(input_str, DICT_MACHINE):
    
    if input_str[0] not in DICT_MACHINE.keys():
            return "", 1
    curr = DICT_MACHINE[input_str[0]]
    for i in range(1,len(input_str)):
        if input_str[i] in curr.keys():
            curr = curr[input_str[i]]
            if type(curr) is str:
                return curr, 1
        else:
            return "", 1

def create_dict_state_machine(input_dict):

    res = {}

    for k,v in input_dict.items():
        if k[0] not in res.keys():
            res[k[0]] = {}
        res[k[0]] = create_dict(res[k[0]], k, 1, v)

    return res


def create_dict(current_dict, input_str, idx, value):

    if idx < len(input_str)-1:
        if input_str[idx] not in current_dict.keys():
            current_dict[input_str[idx]] = {}
        current_dict[input_str[idx]] = create_dict(current_dict[input_str[idx]], input_str, idx+1, value)
    else:
        current_dict[input_str[idx]] = value

    return current_dict


if __name__ == "__main__":
    main(sys.argv[1:])

