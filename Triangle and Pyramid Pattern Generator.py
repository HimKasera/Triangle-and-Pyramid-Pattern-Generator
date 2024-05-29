def lower_triangular(rows):
    # Print a lower triangular pattern
    for r in range(1, rows + 1):
        print("* " * r)

def upper_triangular(rows):
    # Print an upper triangular pattern
    for r in range(rows, 0, -1):
        print("* " * r)

def pyramid(rows):
    # Print a pyramid pattern
    for r in range(1, rows + 1):
        print(" " * (rows - r) + "* " * r)

def main():
    while True:
        # Display the menu options to the user
        print("Choose a shape to generate:")
        print("1. Lower Triangular")
        print("2. Upper Triangular")
        print("3. Pyramid")
        print("4. Exit")
        
        # Get the user's choice
        user_choice = input("Enter your choice (1/2/3/4): ")

        # Exit the loop if the user chooses to exit
        if user_choice == '4':
            break

        # Get the number of rows for the shape
        row_count = int(input("Enter the number of rows: "))

        # Generate the selected shape
        if user_choice == '1':
            lower_triangular(row_count)
        elif user_choice == '2':
            upper_triangular(row_count)
        elif user_choice == '3':
            pyramid(row_count)
        else:
            # Inform the user if they made an invalid choice
            print("Invalid choice. Please try again.")

        print()  # Print a blank line for better readability

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
