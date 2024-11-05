def copy_file_content(source_filename, target_filename):
    try:
        with open(source_filename, 'r') as source_file:
            content = source_file.read()
        
        with open(target_filename, 'w') as target_file:
            target_file.write(content)
        
        print(f"Content of '{source_filename}' has been successfully written to '{target_filename}'")
    except FileNotFoundError:
        print(f"Error: The file '{source_filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_and_display_file(filename, data_to_append):
    try:
        with open(filename, 'a') as file:
            file.write(data_to_append + "\n")
        
        with open(filename, 'r') as file:
            content = file.read()
        
        print("\nCurrent content of the file after appending:")
        print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    source_file = 'source.txt'
    target_file = 'target.txt'
    
    copy_file_content(source_file, target_file)
    
    data_to_append = "This is the new data added to the file."
    append_and_display_file(target_file, data_to_append)


main()
