"""
Random filler text generator for testing purposes and generating mock data

Usage:
    python index.py <wordcount>
    
Author:
    aoyu (ngaoyu27@gmail.com)
    
Version:
    1.0
"""

#imports
import random
import sys


# read file and store as global var
WORDS = open("words.txt", "r").read().splitlines()


def generate_words(wordcount: int) -> str:
    """Generate a random paragraph of words

    Args:
        wordcount (int): _description_

    Returns:
        str: _description_
    """
    wordplist = [random.choice(WORDS) for _ in range(wordcount)]
    wordpara = " ".join(wordplist)
    return wordpara


def main():
    wordcount = int(sys.argv[1])
    print(generate_words(wordcount))


if __name__ == "__main__":
    main()
