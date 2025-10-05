print("Usage: python3 main.py <path_to_book>")

from stats import wordcount
from stats import lettercount
import sys

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
# print(f"Analyzing book found at {filepath}...")
print("----------- Word Count ----------")
letters=wordcount(sys.argv[1])
output=lettercount(letters)

sorted_output=({keyz: value for keyz, value in sorted(output.items(), key=lambda item: item[1], reverse=True)})

sorted_list=list(sorted_output.keys())

sorted_values=list(sorted_output.values())

print("--------- Character Count -------")
for i in range(0,len(list(sorted_output.keys()))):
    print(f"{sorted_list[i]}: {sorted_values[i]}")
    

    