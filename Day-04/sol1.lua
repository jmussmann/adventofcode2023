function main()

    local cards = load_file(arg[1])

    local res = 0

    local winning_numebrs
    local own_numbers

    for i=1,#cards do
        winning_numbers, own_numbers = split_input(cards[i])
        res = res + get_card_points(winning_numbers, own_numbers)
    end


    print(res)

end

function load_file(path)
    local lines = {}
    for line in io.lines(path) do
        lines[#lines+1] = line
    end
    return lines
end

function split_input(line)

    local winning_numebrs
    local own_numbers


    for winning_numbers_str, own_numbers_str in line:gmatch("Card%s+%d+: (.*) | (.*)") do
        print(winning_numbers_str)
        winning_numbers = get_numbers_from_string(winning_numbers_str)
        own_numbers = get_numbers_from_string(own_numbers_str)
    end
    return winning_numbers, own_numbers
end

function get_numbers_from_string(input_str)

    local res = {}

    for str in string.gmatch(input_str, "%w+") do
        res[#res+1] = tonumber(str)
    end

    return res
end

function get_card_points(winning_numbers, own_numbers)
    local res = 1
    for i=1,#winning_numbers do
        for j=1,#own_numbers do
            if winning_numbers[i] == own_numbers[j] then
                res = res * 2
            end
        end
    end
    if res == 1 then
        return 0
    end
    return res/2
end


main()
