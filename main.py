from pathlib import Path
from stats import count_words, count_characters, count_unique_words, dict_to_sorted_list

# Assume you're working in this directory:
current_dir = Path.cwd()  # Get the current working directory

# And you have a full path to a file
full_path_frankenstein = Path("/home/abe/workspace/boot_dev_projects/bookbot//books/frankenstein.txt")

# Get the relative path to the current directory
relative_path_frankenstein = full_path_frankenstein.relative_to(current_dir)

def main() -> int:

    text_path = relative_path_frankenstein

    text = get_book_text(text_path)

    report = [
    "============ BOOKBOT ============",
    "Analyzing book found at books/frankenstein.txt...",
    "----------- Word Count ----------",
    f"Found {count_words(text)} total words",
    "--------- Character Count -------",
    ]
    
    for element in dict_to_sorted_list(count_characters(text)):
        report.append(f"{element['char']}: {element['num']}")

    report.append("============= END ===============")

    print(*report, sep = "\n")
   

def get_book_text(filepath: Path) -> str:
    with open(filepath) as f:
        return(f.read())
    

main()