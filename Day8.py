# Day 8: File I/O
# - Topics:
# - Learn how to read and write files in Python using open(), read(), write().
# - Working with text and CSV files.
# - Project:
# - Write a script that reads a text file and counts how many lines and words are in the file.
def count_lines_words(file_path):
    # Using error handling with try
    try:
        # Opening the file
        with open(file_path, "r") as file:
            # Reading each line in the file
            lines = file.readlines()
            # Getting the number of lines
            line_count = len(lines)
            # Getting the number of words in the file
            word_count = sum(len(line.split()) for line in lines)

            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")

    except FileNotFoundError:
        print("File not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = "Day 8 Project"

count_lines_words(file_path)