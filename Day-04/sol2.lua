INSTANCES = {}
function main()

    local cards = load_file(arg[1])

    local res = 0

    local cards_winning_counts = {}

    local winning_numebrs
    local own_numbers

    for i=1,#cards do
        winning_numbers, own_numbers = split_input(cards[i])
        cards_winning_counts[i] = get_card_winning_count(winning_numbers, own_numbers)
    end
    
    for i=1,#cards do
        res = res + count_winning_cards(i, cards_winning_counts, 0)
    end

    print("Res:", res)

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

function get_card_winning_count(winning_numbers, own_numbers)
    local res = 0
    for i=1,#winning_numbers do
        for j=1,#own_numbers do
            if winning_numbers[i] == own_numbers[j] then
                res = res + 1
            end
        end
    end
    return res
end

function count_winning_cards(card_idx, cards_winning_counts, origin)
    res = 1
    for i=card_idx+1,card_idx+cards_winning_counts[card_idx] do
        if i <= #cards_winning_counts then
            res = res + count_winning_cards(i, cards_winning_counts, card_idx)
        end
    end
    return res
end


main()
