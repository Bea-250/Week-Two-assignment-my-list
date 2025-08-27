def modify_file():
    #step 1: Ask the user for filename
    filename = input("Enter the name of the file: ")
    try: 
        #step 2: Try opening the file for reading
        with open(filename, "r") as infile:
            content = infile.read()
            # Modify the content: convert to uppercase
        modified_content = content.upper()
        # Generate output filename
        new_filename = "modified_" + filename
        
        # Write the modified content to the new file
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)
            print(f"Modified content has been written to {new_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}' .")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Call the function
modify_file()