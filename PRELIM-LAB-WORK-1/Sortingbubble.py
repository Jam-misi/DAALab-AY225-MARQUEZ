import time

def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        Tuple of (sorted list, time taken in seconds)
    """
    start_time = time.time()
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize by detecting if array is already sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps occurred, array is sorted
        if not swapped:
            break
    
    end_time = time.time()
    time_taken = end_time - start_time
    
    return arr, time_taken

def read_numbers_from_file(filename):
    """Reads integers from a text file and returns them as a list."""
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split by spaces or commas and filter out empty strings
                for value in line.replace(',', ' ').split():
                    if value.strip().lstrip('-').isdigit():  # Handles negatives
                        numbers.append(int(value))
                    else:
                        print(f"Warning: Skipping invalid value '{value}'")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return numbers

    

if __name__ == "__main__":
    program_start = time.perf_counter()
    filename = "dataset.txt"  # Change to your file name

    # Step 1: Read numbers from file
    data = read_numbers_from_file(filename)
    
    if data:
        sorted_arr, time_taken = bubble_sort(data)
        print(f"Sorted:   {sorted_arr}")
        
        program_end = time.perf_counter()
        print(f"Time:     {program_end - program_start:.6f} seconds")