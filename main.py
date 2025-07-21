from pathlib import Path
from stats import count_words, count_characters, count_unique_words

# Assume you're working in this directory:
current_dir = Path.cwd()  # Get the current working directory

# And you have a full path to a file
full_path_frankenstein = Path("/home/abe/workspace/boot_dev_projects/bookbot//books/frankenstein.txt")

# Get the relative path to the current directory
relative_path_frankenstein = full_path_frankenstein.relative_to(current_dir)

def main() -> int:

    text_path = relative_path_frankenstein

    text = get_book_text(text_path)

    number_most_commen_words = 10

    print(f"{count_words(text)} words found in the document")
    

def get_book_text(filepath: Path) -> str:
    with open(filepath) as f:
        return(f.read())
    

main()