from itertools import permutations


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
