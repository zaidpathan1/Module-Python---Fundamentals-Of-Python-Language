# Program: Demonstrating PEP 8 Guidelines, Indentation, Comments, and Variables

# This function calculates the area of a rectangle
def calculate_area(length, width):
    """Return the area of a rectangle."""
    area = length * width  # Multiplying length and width
    return area


# Main part of the program
def main():
    """Main function to execute the program."""
    
    # Variables (use descriptive names, lowercase with underscores)
    rectangle_length = 10
    rectangle_width = 5

    # Calculate area using the function
    rectangle_area = calculate_area(rectangle_length, rectangle_width)

    # Display result
    print("Length:", rectangle_length)
    print("Width:", rectangle_width)
    print("Area of Rectangle:", rectangle_area)


# Entry point of the program
if __name__ == "__main__":
    main()