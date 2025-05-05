def process_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes to a new file with error handling.
    
    Args:
        input_filename (str): Path to the input file
        output_filename (str): Path to the output file
    
    Returns:
        bool: True if operation was successful, False otherwise
    """
    try:
        # Read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            
        return True
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return False
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
        return False
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return False


def main():
    """Main function to handle user interaction"""
    print("File Processing Tool")
    print("--------------------")
    
    while True:
        input_file = input("Enter the input filename (or 'quit' to exit): ").strip()
        
        if input_file.lower() == 'quit':
            break
            
        output_file = input("Enter the output filename: ").strip()
        
        if process_file(input_file, output_file):
            print(f"File processed successfully. Output written to {output_file}")
        else:
            print("File processing failed. Please try again.")
        
        print()  # Add blank line for better readability


if __name__ == "__main__":
    main()