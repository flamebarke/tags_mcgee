import sys
from sys import argv
import os

# Usage information
def error():
    if len(sys.argv) < 2:
        print(f"\nERROR [NOT ENOUGH ARGUMENTS]")
        print(f"\nUSAGE: \tpython3 ./tags_mcgee.py file_with_tags.txt\n")
        sys.exit(1)
# Runs first to check if the required number of arguments have been provided
error()
# arguments list = the script name and the text file
script,text_file = argv

# Defined colors
CRED = '\033[91m'
CREND = '\033[0m'
CYEL = '\033[33m'
CYEND = '\033[0m'
CGRE = '\33[92m'
CGEND = '\33[0m'

banner = """

▄▄▄█████▓ ▄▄▄        ▄████   ██████     ███▄ ▄███▓ ▄████▄    ▄████ ▓█████ ▓█████
▓  ██▒ ▓▒▒████▄     ██▒ ▀█▒▒██    ▒    ▓██▒▀█▀ ██▒▒██▀ ▀█   ██▒ ▀█▒▓█   ▀ ▓█   ▀
▒ ▓██░ ▒░▒██  ▀█▄  ▒██░▄▄▄░░ ▓██▄      ▓██    ▓██░▒▓█    ▄ ▒██░▄▄▄░▒███   ▒███
░ ▓██▓ ░ ░██▄▄▄▄██ ░▓█  ██▓  ▒   ██▒   ▒██    ▒██ ▒▓▓▄ ▄██▒░▓█  ██▓▒▓█  ▄ ▒▓█  ▄
  ▒██▒ ░  ▓█   ▓██▒░▒▓███▀▒▒██████▒▒   ▒██▒   ░██▒▒ ▓███▀ ░░▒▓███▀▒░▒████▒░▒████▒
  ▒ ░░    ▒▒   ▓▒█░ ░▒   ▒ ▒ ▒▓▒ ▒ ░   ░ ▒░   ░  ░░ ░▒ ▒  ░ ░▒   ▒ ░░ ▒░ ░░░ ▒░ ░
    ░      ▒   ▒▒ ░  ░   ░ ░ ░▒  ░ ░   ░  ░      ░  ░  ▒     ░   ░  ░ ░  ░ ░ ░  ░
  ░        ░   ▒   ░ ░   ░ ░  ░  ░     ░      ░   ░        ░ ░   ░    ░      ░
               ░  ░      ░       ░            ░   ░ ░            ░    ░  ░   ░  ░
                                                  ░
"""

info = """

Tags is a Unicode block containing formatting tag characters (language tag and ASCII character tags).
U+0001, U+0020–U+007F were originally intended for invisibly tagging texts by language.

This program takes the unicode character tag and decodes it into a readable format.

For further information refer:

https://unicode.org

https://en.wikipedia.org/wiki/Tags_(Unicode_block)

https://www.compart.com/en/unicode/block/U+0000

"""

# Dictionary containing the unicode tags character codes and the corresponding symbol
code = {'U0020': ' ', 'U0021': '!', 'U0022': '"', 'U0023': '#', 'U0024': '$', 'U0025': '%',
'U0026': '&', 'U0027': '\'', 'U0028': '(', 'U0029': ')', 'U002A': '*', 'U002B': '+',
'U002C': ',', 'U002D': '-', 'U002E': '.', 'U002F': '/', 'U0030': '0', 'U0031': '1',
'U0032': '2', 'U0033': '3', 'U0034': '4', 'U0035': '5', 'U0036': '6', 'U0037': '7',
'U0038': '8', 'U0039': '9', 'U003A': ':', 'U003B': ';', 'U003C': '<', 'U003D': '=',
'U003E': '>', 'U003F': '?', 'U0040': '@', 'U0041': 'A', 'U0042': 'B', 'U0043': 'B',
'U0044': 'C', 'U0045': 'D', 'U0046': 'E', 'U0047': 'F', 'U0047': 'G', 'U0048': 'H',
'U0049': 'I', 'U004A': 'J', 'U004B': 'K', 'U004C': 'L', 'U004D': 'M', 'U004E': 'N',
'U004F': 'O', 'U0050': 'P', 'U0051': 'Q', 'U0052': 'R', 'U0053': 'S', 'U0054': 'T',
'U0055': 'U', 'U0056': 'V', 'U0057': 'W', 'U0058': 'X', 'U0059': 'Y', 'U005A': 'Z',
'U005B': '[', 'U005C': '\\', 'U005D': ']', 'U005E': '^', 'U005F': '_', 'U0060': '`',
'U0061': 'a', 'U0062': 'b', 'U0063': 'c', 'U0064': 'd', 'U0065': 'e', 'U0066': 'f',
'U0067': 'g', 'U0068': 'h', 'U0069': 'i', 'U006A': 'j', 'U006B': 'k', 'U006C': 'l',
'U006D': 'm', 'U006E': 'n', 'U006F': 'o', 'U0070': 'p', 'U0071': 'q', 'U0072': 'r',
'U0073': 's', 'U0074': 't', 'U0075': 'u', 'U0076': 'v', 'U0077': 'w', 'U0078': 'x',
'U0079': 'y', 'U007A': 'z', 'U007B': '{', 'U007C': '|', 'U007D': '}', 'U007E': '~'}

# Reads the file and outputs to stdout
def read():
    with open (f"{text_file}", encoding='utf-8') as f:
        print(CYEL + "\n" + "#" * 50 + CYEND)
        print(f"\nFile contents >: \n")
        read = f.read()
        print(f"\n{read}\n")
        print(CYEL + "#" * 50 + CYEND)

# Reads the file line by line including any encoding and outputs to stdout
def readlines():
    with open (f"{text_file}", encoding='utf-8') as f:
        print(f"\n File line data >: \n")
        lines = f.readlines()
        print(f"\n{lines}\n")
        print(CYEL + "#" * 50 + CYEND + "\n")

# Stores the character codes to file in uppercase and formats using sed
def retrieve():
    tags = input(CGRE + f"\nCopy and paste your Unicode tag character codes here excluding the first \ >: \\" + CGEND)
    prefix = input(CGRE + f"\nEnter any prefix that is present on your unicode i.e U000 or U+ >: " + CGEND)
    f = open('tags.txt', 'w')
    f.write(tags.upper())
    f.close()
    clean = r"sed -e 's/\\/\n/g' -e " + f"'s/{prefix}/''/g' " + 'tags.txt' + " > " "clean_tags.txt"
    print(CGRE + f"\n\nformatting unicode tags into bytes per line and outputting to file >: ./clean_tags.txt\n" + CGEND)
    os.system(clean)

# Decodes the stored character codes and outputs to stdout
def decode():
    print(CGRE + "\nDecoded Unicode tag character codes >:  \n\n" + CGEND)
    f = open('clean_tags.txt')
    f_list = f.readlines()
    for line in f_list:
        line = line.rstrip()
        print(CRED + code.get(line) + CYEND, end="")
    print("\n\n")

# Execute the program
def tags_mcgee():
    print(CRED + f"{banner}" + CYEND)
    prompt = input(CGRE + "Would you like to see info >: y/n " + CGEND)
    if prompt == "y":
            print(f"{info}")
    read()
    readlines()
    retrieve()
    decode()

tags_mcgee()
