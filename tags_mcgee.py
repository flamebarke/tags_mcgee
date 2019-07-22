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
U+E0001, U+E0020–U+E007F were originally intended for invisibly tagging texts by language.

This program takes the unicode character tag and decodes it into a readable format. 

For further information refer:

https://unicode.org

https://en.wikipedia.org/wiki/Tags_(Unicode_block)

https://www.compart.com/en/unicode/block/U+E0000

"""

# Dictionary containing the unicode tags character codes and the corresponding symbol
code = {'E0020': ' ', 'E0021': '!', 'E0022': '"', 'E0023': '#', 'E0024': '$', 'E0025': '%',
'E0026': '&', 'E0027': '\'', 'E0028': '(', 'E0029': ')', 'E002A': '*', 'E002B': '+',
'E002C': ',', 'E002D': '-', 'E002E': '.', 'E002F': '/', 'E0030': '0', 'E0031': '1', 
'E0032': '2', 'E0033': '3', 'E0034': '4', 'E0035': '5', 'E0036': '6', 'E0037': '7', 
'E0038': '8', 'E0039': '9', 'E003A': ':', 'E003B': ';', 'E003C': '<', 'E003D': '=', 
'E003E': '>', 'E003F': '?', 'E0040': '@', 'E0041': 'A', 'E0042': 'B', 'E0043': 'B', 
'E0044': 'C', 'E0045': 'D', 'E0046': 'E', 'E0047': 'F', 'E0047': 'G', 'E0048': 'H', 
'E0049': 'I', 'E004A': 'J', 'E004B': 'K', 'E004C': 'L', 'E004D': 'M', 'E004E': 'N', 
'E004F': 'O', 'E0050': 'P', 'E0051': 'Q', 'E0052': 'R', 'E0053': 'S', 'E0054': 'T', 
'E0055': 'U', 'E0056': 'V', 'E0057': 'W', 'E0058': 'X', 'E0059': 'Y', 'E005A': 'Z', 
'E005B': '[', 'E005C': '\\', 'E005D': ']', 'E005E': '^', 'E005F': '_', 'E0060': '`', 
'E0061': 'a', 'E0062': 'b', 'E0063': 'c', 'E0064': 'd', 'E0065': 'e', 'E0066': 'f', 
'E0067': 'g', 'E0068': 'h', 'E0069': 'i', 'E006A': 'j', 'E006B': 'k', 'E006C': 'l', 
'E006D': 'm', 'E006E': 'n', 'E006F': 'o', 'E0070': 'p', 'E0071': 'q', 'E0072': 'r', 
'E0073': 's', 'E0074': 't', 'E0075': 'u', 'E0076': 'v', 'E0077': 'w', 'E0078': 'x', 
'E0079': 'y', 'E007A': 'z', 'E007B': '{', 'E007C': '|', 'E007D': '}', 'E007E': '~'}

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


