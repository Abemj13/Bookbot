import sys
from pathlib import Path
from stats import count_words, count_characters, count_unique_words, dict_to_sorted_list

# Assume you're working in this directory:
# current_dir = Path.cwd()  # Get the current working directory

# And you have a full path to a file
# full_path_frankenstein = Path("/home/abe/workspace/boot_dev_projects/bookbot//books/frankenstein.txt")

# Get the relative path to the current directory
# relative_path_frankenstein = full_path_frankenstein.relative_to(current_dir)


def main() -> int:

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text_path = sys.argv[1]

    print(f"You passed the path to book: {text_path}")


    #Het zou mooi zijn om het rapport print gedeelte tot een functie om te toveren! Want in main() wil ik eigenlijk alleen mar functies aanroepen

    report = [
    "============ BOOKBOT ============",
    "Analyzing book found at books/frankenstein.txt...",
    "----------- Word Count ----------",
    f"Found {count_words(get_book_text(text_path))} total words",
    "--------- Character Count -------",
    ]
    
    for element in dict_to_sorted_list(count_characters(get_book_text(text_path))):
        report.append(f"{element['char']}: {element['num']}")

    report.append("============= END ===============")

    print(*report, sep = "\n")
   

def get_book_text(filepath: Path) -> str:
    with open(filepath) as f:
        return(f.read())
    

if __name__ == "__main__":
    main()