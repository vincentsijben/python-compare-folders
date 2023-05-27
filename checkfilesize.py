import os

path_limit = 250
folder_a = r'\\?\E:\Dropbox (ArtsZuyd)\mamdt - onderwijsinhoud - CMD onderwijs 2015-2016'

def check_path_length(path, limit):
    if len(path) > limit:
        
        print(f"{len(path)}: {path[4:]}")

def compare_folders(folder1, limit):
    print(f"\n\nThese paths exceed the limit of {path_limit} characters:\n")
    for root, dirs, files in os.walk(folder1):
        for name in files + dirs:
            path = os.path.join(root, name)
            check_path_length(path, limit)

if __name__ == '__main__':
    compare_folders(folder_a, path_limit)
