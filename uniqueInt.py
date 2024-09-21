MAX_INT = 2**31 - 1
MIN_INT = -2**31
unique_integers = set()

# Custom bubble sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Corrected file paths
input_file_path = r"C:\Users\LENOVO\OneDrive\Desktop\uniqueintegers\dsa\hw01\input_01.txt"
output_file_path = r"C:\Users\LENOVO\OneDrive\Desktop\uniqueintegers\dsa\hw01\output_01.txt"

try:
    with open(input_file_path, "r") as file:
        print(f"Reading from {input_file_path}...")  # Debugging line
        for line in file:
            line = line.strip()
            print(f"Read line: '{line}'")  # Debugging line to see raw line content

            try:
                my_int = int(line)
                print(f"Parsed integer: {my_int}")  # Debugging line to see parsed integers
                if MIN_INT <= my_int <= MAX_INT:
                    unique_integers.add(my_int)
                    print(f"Added {my_int} to unique_integers")  # Debugging line
            except ValueError:
                print(f"Skipping line: '{line}' (not an integer)")  # Debugging line
                continue
except FileNotFoundError:
    print(f"File {input_file_path} not found. Please check the file path.")
    exit()

# If no integers were found, notify the user
if not unique_integers:
    print("No valid integers were found in the input file.")

# Convert the set to a list and sort it using the custom bubble sort
sorted_integers = bubble_sort(list(unique_integers))

# Write the sorted unique integers to the output file
try:
    with open(output_file_path, 'w') as output_file:
        print(f"Writing sorted integers to {output_file_path}...")  # Debugging line
        for integer in sorted_integers:
            output_file.write(f"{integer}\n")
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")
    exit()

# Ensure the file is closed before reading
print(f"Processing complete! The results are stored in {output_file_path}")

# Read and print the output file's content to the console
try:
    with open(output_file_path, 'r') as output_file:
        print("Content of the output_01.txt file:")
        content = output_file.read().strip()  # Read the entire file content
        if content:
            print(content)  # Print the file content
        else:
            print("The output file is empty.")  # In case there's nothing in the file
except FileNotFoundError:
    print(f"File {output_file_path} not found. Please check the file path.")
