def calculate_cube():
    try:
        number_str = input("enter a number:")
        number = float(number_str)
        cube = number ** 3
        print(f"The cube of {number} is {cube}")
        breakpoint()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    calculate_cube()