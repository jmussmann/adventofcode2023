
mutable struct Game
    Id::Int # the game id
    max_red::Int
    max_green::Int
    max_blue::Int
end


function is_game_possible(game, game_init)
    if game.max_red > game_init.max_red
        return false
    end
    if game.max_green > game_init.max_green
        return false
    end
    if game.max_blue > game_init.max_blue
        return false
    end

    return true
end

game_strings = readlines(ARGS[1])

games = Vector{Game}()

for game_str in game_strings
    m = match(r"^Game (?<gameid>\d+):", game_str)
    Id = parse(Int, m["gameid"]);
    game = Game(Id, 0, 0, 0)
    for m in eachmatch(r"(?<red>\d+) red", game_str)
        count = parse(Int, m["red"])
        game.max_red = maximum([game.max_red, count])
    end
    for m in eachmatch(r"(?<green>\d+) green", game_str)
        count = parse(Int, m["green"])
        game.max_green = maximum([game.max_green, count])
    end
    for m in eachmatch(r"(?<blue>\d+) blue", game_str)
        count = parse(Int, m["blue"])
        game.max_blue = maximum([game.max_blue, count])
    end
    push!(games, game)
end

initial_game = Game(0, parse(Int, ARGS[2]), parse(Int, ARGS[3]), parse(Int, ARGS[4]))

print(initial_game)

global sum_possible_ids = 0
global sum_min_set = 0
for game in games
    if is_game_possible(game, initial_game)
        println(game)
        global sum_possible_ids = sum_possible_ids + game.Id
    end
    global sum_min_set = sum_min_set + game.max_blue * game.max_green * game.max_red
end

println("SUM: ", sum_possible_ids)
println("SUM min set: ", sum_min_set)


