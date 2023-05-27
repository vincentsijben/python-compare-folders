import os
import filecmp
import time
from datetime import datetime

num_files_processed = 0
execution_time = 0.0

# Provide the paths of Folder A and Folder B
# folder_a = r'\\?\E:\Dropbox (ArtsZuyd)\mamdt - onderwijsinhoud - CMD onderwijs 2015-2016\1.4 - SLB POP en portfolio'
folder_a = r'\\?\E:\Dropbox (ArtsZuyd)\mamdt - onderwijsinhoud - CMD onderwijs 2015-2016'
# folder_a = r'\\?\E:\Dropbox (ArtsZuyd)\mamdt - onderwijsinhoud - CMD onderwijs 2014-2015'
# folder_b = r'\\?\E:\Zuyd Hogeschool\CMD - Z_Archief onderwijs\2015-2016\1.4 - SLB POP en portfolio'
folder_b = r'\\?\E:\Zuyd Hogeschool\CMD - Z_Archief onderwijs\2015-2016'
# folder_b = r'\\?\E:\Zuyd Hogeschool\CMD - Z_Archief onderwijs\2014-2015'

# Specify whether to check for file size or not
check_for_filesize = False

def compare_folders(folder_a, folder_b, check_for_filesize=False):
    global num_files_processed
    global execution_time

    missing_files = []
    start_time = time.time()
    notification_interval = 10  # Notify every 10 seconds
    last_notification_time = start_time

    for dirpath, dirnames, filenames in os.walk(folder_a):
        relative_dirpath = os.path.relpath(dirpath, folder_a)
        destination_dir = os.path.join(folder_b, relative_dirpath)

        for file in filenames:
            source_file = os.path.join(dirpath, file)
            destination_file = os.path.join(destination_dir, file)

            if not os.path.exists(destination_file):
                missing_files.append(source_file)
            elif check_for_filesize and os.path.getsize(source_file) != os.path.getsize(destination_file):
                missing_files.append(source_file)

            num_files_processed += 1
            current_time = time.time()

            # Check if it's time for a progress notification
            if current_time - last_notification_time >= notification_interval:
                elapsed_time = current_time - start_time
                print(f"Processed {num_files_processed} files. Elapsed time: {elapsed_time:.2f} seconds.")
                last_notification_time = current_time

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total files processed: {num_files_processed}. Total execution time: {execution_time:.2f} seconds.")

    return missing_files



# Call the function to compare the folders
missing_files = compare_folders(folder_a, folder_b, check_for_filesize)

# Create the output folder if it doesn't exist
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Generate the text file path with the current date and time
current_datetime = time.strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(output_folder, f"comparison_results_{current_datetime}.txt")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("Files not copied:\n")
    if len(missing_files) > 0:
        for file in missing_files:
            display_path = file[4:]  # Exclude the first 4 characters (\\?\)
            f.write(f"Path: {display_path} (Length: {len(file)})\n")

        path_lengths = [len(file) for file in missing_files]
        min_length = min(path_lengths)
        max_length = max(path_lengths)
        f.write(f"\n\nNumber of files not copied: {len(missing_files)}")
        f.write(f"\nThe length of the paths ranged from {min_length} to {max_length} characters.\n")
    else:
        f.write("No missing files found.\n")

    f.write(f"\nTotal files processed: {num_files_processed}.\n")
    f.write(f"Total execution time: {execution_time:.2f} seconds.\n")

# Display the summary on the screen
print("\nComparison Summary:")
if len(missing_files) > 0:
    print(f"Number of files not copied: {len(missing_files)}")
    path_lengths = [len(file) for file in missing_files]
    min_length = min(path_lengths)
    max_length = max(path_lengths)
    print(f"The length of the paths ranged from {min_length} to {max_length} characters.")
else:
    print("No missing files found.")
print(f"\nTotal files processed: {num_files_processed}.")
print(f"Total execution time: {execution_time:.2f} seconds.")
