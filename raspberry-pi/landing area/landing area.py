import time

def validate_input(input_string: str): # return false on error or an array of the form [x, y] on success
    try:
        input_parts = input_string.split(",") # a comma separates the coordinate points
    except ValueError:
        return False
    if len(input_parts) != 2: # we expect an x and a y coordinate
        return False
    try:
        result = [float(part) for part in input_parts] # turn the strings in input_parts into floats
        return result
    except ValueError: # if something wasn't a float
        return False

def get_area(p1, p2, p3): 
    area = 0.5 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) # math equation for area
    return abs(area)

while True:
    vertex_1 = validate_input(input("Vertex 1: "))
    if not vertex_1:
        print("That was not the proper format. Please try again.")
        continue    # serial print to enter coordinates and if the worng format is put return an error
    vertex_2 = validate_input(input("Vertex 2: "))
    if not vertex_2:
        print("That was not the proper format. Please try again.")
        continue
    vertex_3 = validate_input(input("Vertex 3: "))
    if not vertex_3:
        print("That was not the proper format. Please try again.")
        continue
    area = get_area(vertex_1, vertex_2, vertex_3)   # call back to the math function plugging in the three points
    print(f"The area of the triangle with vertices ({vertex_1[0]},{vertex_1[1]}), ({vertex_2[0]},{vertex_2[1]}), ({vertex_3[0]},{vertex_3[1]}) is {area} square km.")