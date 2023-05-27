import os
import time

def search_files_and_folders(folder, search_string):
    num_processed_files = 0
    start_time = time.time()

    # Create a list to store the matching results
    matching_results = []

    # Traverse the folder and its subdirectories
    for root, dirs, files in os.walk(folder):
        for name in files + dirs:
            path = os.path.join(root, name)
            if search_string in path.lower():
                matching_results.append(path[4:])
            num_processed_files += 1

    # Calculate the execution time
    execution_time = time.time() - start_time

    # Log the number of processed files and execution time
    print("Number of processed files:", num_processed_files)
    print(f"Found {len(matching_results)} matches.")
    print("Execution time:", execution_time, "seconds")

    # Save the search results to a txt file
    with open("search_results.txt", "w", encoding='utf-8') as file:
        file.write("\n".join(matching_results))

folder = r'\\?\E:\Dropbox (ArtsZuyd)\mamdt - onderwijsinhoud - CMD onderwijs 2015-2016'
search_string = 'marcel'

search_files_and_folders(folder, search_string)
