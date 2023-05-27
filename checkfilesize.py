import os
import time

path_limit = 200
folder_a = r'\\?\E:\Dropbox (ArtsZuyd)\mamdt - onderwijsinhoud - CMD onderwijs 2015-2016'
num_files_processed = 0
execution_time = 0.0

def compare_folders(folder1, limit):
    global num_files_processed
    global execution_time
    start_time = time.time()
    notification_interval = 10  # Notify every 10 seconds
    last_notification_time = start_time
    print(f"\nChecking path sizes inside folder {folder_a[4:]} that exceed the limit of {path_limit} characters.")
    results = []
    for root, dirs, files in os.walk(folder1):
        for name in files + dirs:
            path = os.path.join(root, name)
            if len(path) > limit:
                results.append(path)

            num_files_processed += 1
            current_time = time.time()

             # Check if it's time for a progress notification
            if current_time - last_notification_time >= notification_interval:
                elapsed_time = current_time - start_time
                print(f"Processed {num_files_processed} files. Elapsed time: {elapsed_time:.2f} seconds.")
                last_notification_time = current_time

    sorted_paths = sorted(results, key=len, reverse=True)

    # Create the output folder if it doesn't exist
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate the text file path with the current date and time
    current_datetime = time.strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_folder, f"filesizes_{current_datetime}.txt")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"These paths inside folder {folder_a[4:]} exceed the limit of {path_limit} characters:\n\n")
        for path in sorted_paths:
            f.write(f"{len(path)}: {path[4:]}\n")

    end_time = time.time()
    execution_time = end_time - start_time

if __name__ == '__main__':
    compare_folders(folder_a, path_limit)

    print(f"Total files processed: {num_files_processed}.")
    print(f"Total execution time: {execution_time:.2f} seconds.")