from itertools import permutations
import copy


def parse_file_to_list(file_path):
    result_list = []

    with open(file_path, 'r') as file:
        for line in file:
            # Strip newline characters and split by spaces
            name, width, height = line.strip().split(' ')

            # Convert width and height to integers
            result_list.append([int(width), int(height), name])
            
    return result_list

file_path = 'input.txt'  # Change the filepath as needed
main_rectangles = parse_file_to_list(file_path)

# Sort the list by width first, then by height
main_rectangles.sort()

def get_rectangle(rectangle, skyline, output, w):

    l = 0
    r = len(rectangle) - 1
    result = -1
    while(l <= r):
        mid = (l+r)//2
        
        if(rectangle[mid] <= w):
            l = mid + 1
            result = mid
        else:
            r = mid - 1




def skyline_placement(rectangles, W):
    # Initialize skyline with the full width and zero height
    skyline = [(0, 0, W)]
    placements = []
    max_height = 0

    for width, height, name in rectangles:
        for i, (x, y, space_width) in enumerate(skyline):
            if width <= space_width:
                # Place the rectangle at the current skyline segment
                placements.append((x, y, name))
                max_height = max(max_height, y + height)

                # Update the skyline: add a new segment or adjust existing
                if width == space_width:
                    skyline[i] = (x, y + height, width)
                else:
                    skyline[i] = (x + width, y, space_width - width)
                    skyline.insert(i, (x, y + height, width))
                break

    return placements, max_height

def find_best_placement(rectangles):

    # Set initial best area to infinity
    best_area = float('inf')
    best_placement = None
    best_width = 0
    best_height = 0

    # Explore different widths (from the widest rectangle to the sum of all widths)
    for W in range(rectangles[0][0], sum(r[0] for r in rectangles) + 1):
        placements, height = skyline_placement(rectangles, W)
        area = W * height

        if area < best_area:
            best_area = area
            best_placement = placements
            best_width = W
            best_height = height

    return best_placement, best_width, best_height



w_min = main_rectangles[0][0]
w_max = sum(main_rectangles[i][0] for i in range(len(main_rectangles)))

rectangles = copy.deepcopy(main_rectangles)
best_height = -1
best_width = -1
best_area = -1
best_cordinate = []


for w in range(w_min, w_max):
    h = 0
    area = 0
    cordinate = []
