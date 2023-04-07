### Day two - Advent of code 2015 ###
### By Calamity Jane ###

def get_paper_for_gift(dimensions: list) -> int:
    #dim_dict= {"l" : dimensions[0], "w" : dimensions[1], "h" : dimensions[2]}
    #return 2*dim_dict["l"]*dim_dict["w"] + 2*dim_dict["w"]*dim_dict["h"] + 2*dim_dict["h"]*dim_dict["l"]
    l,h,w = dimensions
    return 2*l*w + 2*w*h + 2*h*l
    
def get_slack(dimensions: list) -> int:
    dimensions.sort()
    a, b, *_ = dimensions
    return a*b

def get_ribbon(dimensions: list) -> int:
    dimensions.sort()
    a,b, *_= dimensions
    return a+a+b+b

def get_bow(dimensions: list) -> int:
    a,b,c = dimensions
    return a*b*c


def main() : 
  
    with open("puzzle_inputs/day_two.txt", "r") as inputs:
        gifts_dimensions = inputs.read().splitlines()

    paper_to_order = 0
    ribon_to_order = 0

    for gift in gifts_dimensions :
        dimension = gift.split("x")
        int_dim = [int(numeric_string) for numeric_string in dimension]

        paper_for_gift = get_paper_for_gift(int_dim)
        slack = get_slack(int_dim)
        paper_to_order += paper_for_gift
        paper_to_order += slack

        ribon_for_gift = get_ribbon(int_dim)
        bow_for_gift = get_bow(int_dim)
        ribon_to_order += ribon_for_gift
        ribon_to_order += bow_for_gift

    print("---- paper to order ----")
    print(paper_to_order)
    print("---- ribbon to order ----")
    print(ribon_to_order)

if __name__ == "__main__":
    main()