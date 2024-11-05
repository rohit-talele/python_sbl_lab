import os

def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_characters = sum(len(line) for line in lines)
            
        print(f"\nFile: {filename}")
        print(f"Number of Lines: {num_lines}")
        print(f"Number of Words: {num_words}")
        print(f"Number of Characters: {num_characters}")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

def list_files_in_current_directory():
    files_and_dirs = os.listdir('.')
    
    print("\nFiles and directories in the current directory:")
    for item in files_and_dirs:
        print(item)

def main():
    list_files_in_current_directory()

    filename = input("\nEnter the name of the file to count lines, words, and characters: ")
    
    count_file_stats(filename)


main()
