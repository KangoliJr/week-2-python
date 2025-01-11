def read_and_modify_file(input_filename, output_filename):
 
  try:
    with open(input_filename, 'r') as infile:
      data = infile.read()

    # Modify the data 
    modified_data = ' '.join(word.capitalize() for word in data.split()) 

    with open(output_filename, 'w') as outfile:
      outfile.write(modified_data)

    print(f"File '{input_filename}' read and modified successfully. "
          f"Modified content written to '{output_filename}'.")

  except FileNotFoundError:
    print(f"Error: Input file '{input_filename}' not found.")
  except IOError:
    print(f"Error: An I/O error occurred while reading or writing the file.")

if __name__ == "__main__":
  input_filename = "rw"  
  output_filename = "rw_modified.txt" 

  read_and_modify_file(input_filename, output_filename)