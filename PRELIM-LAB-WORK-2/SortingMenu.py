import time
import os

def bubble_sort(arr):
    """Sorts an array using bubble sort algorithm."""
    start_time = time.time()
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] < arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        if not swapped:
            break
    
    time_taken = time.time() - start_time
    return arr_copy, time_taken

def insertion_sort(arr):
    """Sorts an array using insertion sort algorithm."""
    start_time = time.time()
    arr_copy = arr.copy()
    
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[j] < key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    
    time_taken = time.time() - start_time
    return arr_copy, time_taken

def merge_sort(arr):
    """Sorts an array using merge sort algorithm."""
    start_time = time.time()
    arr_copy = arr.copy()
    
    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    sorted_arr = merge_sort_recursive(arr_copy)
    time_taken = time.time() - start_time
    return sorted_arr, time_taken

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

    

def display_menu():
    """Display the menu options."""
    print("\n" + "="*50)
    print("         SORTING ALGORITHM MENU")
    print("-"*50)
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. Compare All Algorithms")
    print("5. Exit")
    print("*"*50)

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), "dataset.txt")

    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '5':
            print("\nExiting program. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("\nInvalid choice! Please enter 1-5.")
            continue
        
        # Read data from file
        data = read_numbers_from_file(filename)
        
        if not data:
            print("\nNo data to sort. Please check the file.")
            continue
        
        print(f"\nOriginal data: {data}")
        print(f"Data size: {len(data)} elements\n")
        
        if choice == '1':
            sorted_arr, time_taken = bubble_sort(data)
            print(f"Bubble Sort Result: {sorted_arr}")
            print(f"Time taken: {time_taken:.6f} seconds")
        
        elif choice == '2':
            sorted_arr, time_taken = insertion_sort(data)
            print(f"Insertion Sort Result: {sorted_arr}")
            print(f"Time taken: {time_taken:.6f} seconds")
        
        elif choice == '3':
            sorted_arr, time_taken = merge_sort(data)
            print(f"Merge Sort Result: {sorted_arr}")
            print(f"Time taken: {time_taken:.6f} seconds")
        
        elif choice == '4':
            print("Running all sorting algorithms...\n")
            
            sorted_arr1, time1 = bubble_sort(data)
            print(f"1. Bubble Sort:    {time1:.6f} seconds")
            
            sorted_arr2, time2 = insertion_sort(data)
            print(f"2. Insertion Sort: {time2:.6f} seconds")
            
            sorted_arr3, time3 = merge_sort(data)
            print(f"3. Merge Sort:     {time3:.6f} seconds")
            
            print(f"\nSorted result: {sorted_arr1}")
            
            # Find fastest
            times = [('Bubble Sort', time1), ('Insertion Sort', time2), ('Merge Sort', time3)]
            fastest = min(times, key=lambda x: x[1])
            print(f"\nFastest algorithm: {fastest[0]} ({fastest[1]:.6f} seconds)")