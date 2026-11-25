#!/usr/bin/env python3
"""Write the dog's excuse to /output/entry.txt.

The entry is one line, under 200 characters, in the dog's own voice:
a dog caught eating the homework, explaining itself with total
confidence that it did nothing wrong.
"""

import os

EXCUSE = "The homework started it. It looked at me like that for three hours straight. I had to eat it before it ate me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
