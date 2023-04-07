### Day one - Advent of code 2015 ###
### By Calamity Jane ###

def change_tuple_value(t : tuple, idx: int, val: int) -> tuple :
    lst = list(t)
    lst[idx] = lst[idx] + val
    return tuple(lst)

def main() : 
  
    with open("puzzle_inputs/day_three.txt", "r") as inputs:
        directions = list(inputs.read())

    coordinates = (0,0)
    coordinates_set = {coordinates}
    
    for direction in directions : 
        match direction:
            case '>':
                coordinates = change_tuple_value(coordinates, 0, 1)
            case '<':
                coordinates = change_tuple_value(coordinates, 0, -1)
            case '^':
                coordinates = change_tuple_value(coordinates, 1, 1)
            case 'v':
                coordinates = change_tuple_value(coordinates, 1, -1)
        
        coordinates_set.add(coordinates)
    
    print(len(coordinates_set))
   

if __name__ == "__main__":
    main()