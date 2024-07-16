import os
import shutil

def take_paths():
    source = input("Please Enter Source Path: ").strip()
    destination = input("Please Enter Destination Path: ").strip()
    return source, destination

def copy_files(source, destination):
    try:
        if not os.path.exists(source):
            print(f"Error: Source path '{source}' does not exist.")
            return False
        if not os.path.exists(destination):
            os.makedirs(destination)
            print(f"Destination folder '{destination}' created.")
        
        for filename in os.listdir(source):
            source_file = os.path.join(source, filename)
            destination_file = os.path.join(destination, filename)
            shutil.copy2(source_file, destination_file)
        
        print("Files transferred successfully!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    while True:
        source, destination = take_paths()
        if copy_files(source, destination):
            break

if __name__ == "__main__":
    main()
