
# Create input.txt and write content into it
def create_input_file():
   
    try:
        with open("input.txt", "w") as file:
            file.write("This is the first line.\n")
            file.write("Here is another line of text.\n")
            file.write("A third line, with more words.\n")
            file.write("And yet another line.\n")
            file.write("The last line in the file.\n")
        print("input.txt file created successfully.")
    except Exception as e:
        print(f"Error creating input.txt: {e}")

# Function to process the text and write to output.txt
def process_text_and_write():
    
    try:
        # Read the content of input.txt
        with open("input.txt", "r") as infile:
            text = infile.read()

        # Count the number of words
        word_count = len(text.split())

        # Convert the text to uppercase
        uppercase_text = text.upper()

        # Write the processed text and word count to output.txt
        with open("output.txt", "w") as outfile:
            outfile.write(uppercase_text)
            outfile.write(f"\nWord Count: {word_count}\n")

        print("Text processed and written to output.txt successfully.")

    except FileNotFoundError:
        print("Error: input.txt not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_input_file()  # Create the input file
    process_text_and_write() # Process the text and write to the output file
