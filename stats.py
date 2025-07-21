from pathlib import Path
from collections import defaultdict


def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:

    char_dict : dict[str, int] = defaultdict(int)  # This will auto-init each new character with 0
    
    for character in text.lower():
        char_dict[character] += 1

    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))  # Optional: convert back to a regular dict


def dict_to_sorted_list(unsorted_dict: dict[str,int]) -> list[dict[str, str | int]]:

     return [{"char" : k, "num" : v} 
             for k,v in sorted(unsorted_dict.items(), key=lambda item:item[1], reverse=True) 
             if k.isalpha()
             ]

    

def count_unique_words(text: str, number_most_commen_words: int = None) -> dict[str, int]:

    word_dict : dict[str, int] = defaultdict(int)

    for word in text.lower().split():
        word_dict[word] += 1

    return dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True)[:number_most_commen_words])
