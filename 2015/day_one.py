
### Day one - Advent of code 2015 ###
### By Calamity Jane ###

# -------- Part one -----------
# Loop throught direction in order to calculate the floor 
def get_floor(starting_floor: int, directions: list) -> int : 
    for direction in directions : 
        match direction: 
            case '(' : 
                starting_floor += 1
            case ')' : 
                starting_floor -= 1
    return starting_floor

def main() : 
    # Get each directions form the input file into a list
    with open("puzzle_inputs/day_one.txt", "r") as inputs:
        directions = list(inputs.read())
    print(get_floor(0, directions))

if __name__ == "__main__":
    main()

# -------- Part two -----------
# Loop throught direction in order to calculate the floor 
def get_position_basement(starting_floor: int, directions: list) -> int : 
    for i, direction in enumerate(directions) : 
        match direction: 
                case '(' : 
                    starting_floor += 1
                case ')' : 
                    starting_floor -= 1
        if starting_floor == -1:
            return i+1

def main() : 
    # Get each directions form the input file into a list
    with open("puzzle_inputs/day_one.txt", "r") as inputs:
        directions = list(inputs.read())
    print(get_position_basement(0, directions))

if __name__ == "__main__":
    main()