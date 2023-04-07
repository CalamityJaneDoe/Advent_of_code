### Day one - Advent of code 2015 ###
### By Calamity Jane ###

def create_itineraries(itinerary: list) -> tuple : 
    idx = 0 
    santa_it = []
    robot_santa_it = []
    for i in itinerary : 
        if idx %2 == 0 :
            santa_it.append(i)
        else :
            robot_santa_it.append(i)
        idx += 1

    return (santa_it, robot_santa_it)

def save_coordinates(itinerary: list, coordinates_set: set) -> set :
    coordinates = (0,0)
    for direction in itinerary: 
        match direction:
            case '>':
                coordinates = (coordinates[0]+1, coordinates[1]) 
            case '<':
                coordinates = (coordinates[0]-1, coordinates[1])
            case '^':
                coordinates = (coordinates[0], coordinates[1]+1) 
            case 'v':
                coordinates = (coordinates[0], coordinates[1]-1)

        coordinates_set.add(coordinates)

    return coordinates_set

def main() : 
  
    with open("puzzle_inputs/day_three.txt", "r") as inputs:
        directions = list(inputs.read())

    itineraries = create_itineraries(directions)

    # Adds better lisibility for the code
    santa_itinerary = itineraries[0]
    robot_itinerary = itineraries[1]

    houses_visited_by_santa = save_coordinates(santa_itinerary, {(0,0)})
    houses_visited_by_robot = save_coordinates(robot_itinerary, houses_visited_by_santa)
    
    print(len(houses_visited_by_robot) )


if __name__ == "__main__":
    main()