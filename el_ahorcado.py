"""
1)Write a program that consists of asking the user for different letters, if the user fails to 
	start drawing the hangman, if the user is right to show the correct letter.
2)Hide the letters with a low dash.
3)The game ends when the user fond all the letters.
4)You can create a list of words and pick a random word from this list.
"""

fail0 = """
Bienvenidos a Michoacan !
	____________________

    |         |

    |         

    |        

    |        

    |

    | 
"""

fail1 = """
Bienvenidos a Michoacan !
	____________________

    |         |

    |         O

    |        

    |        

    |

    | 
"""

fail2 = """
Bienvenidos a Michoacan !
	____________________

    |         |

    |         O

    |         |
              |
    |         |

    |

    | 
"""

fail3 = """
Bienvenidos a Michoacan !
	____________________

    |         |

    |         O

    |       / |
              |
    |         |

    |

    | 
"""

fail4 = """
Bienvenidos a Michoacan !
	____________________

    |         |

    |         O

    |       / | \\
              |
    |         |

    |

    | 
"""

fail5 = """
Bienvenidos a Michoacan !
	____________________

    |         |

    |         O

    |       / | \\
              |
    |         |

    |       /

    | 
"""

fail6 = """
Bienvenidos a Michoacan !
	____________________

    |         |

    |         O

    |       / | \\
              |
    |         |

    |       /   \\

    | 
"""


import os
import re
import random
from random import choice

word = random.choice(["MARILI", "LINUX", "FIRMWARE", "PYTHON", "AUTOMATION", "GUANATOS", "RAMANUJAN"])
screen = ["*"]*len(word)
print("".join(screen))

mistake = 0

while mistake < 7:

	if mistake == 0:
		print(fail0)
	elif mistake == 1:
		print(fail1)
	elif mistake == 2:
		print(fail2)
	elif mistake == 3:
		print(fail3)
	elif mistake == 4:
		print(fail4)
	elif mistake == 5:
		print(fail5)

	char1 = input("Type a char: ").upper()
	try:
		if len(char1)>0 and ord(char1) >= 65 and ord(char1) <= 90:
			if char1 in word:
				for i in re.finditer(char1, word, re.IGNORECASE):
					screen[i.start():i.end()] = list(i.group())
				print("".join(screen))
				screen2 = ("".join(screen))
				print("Errores: "+str(mistake))
			else:
				mistake +=1
				print("".join(screen))
				print("Errores: "+str(mistake))
		else:
			print("Character is not allowed")
		if screen2 == word:
			print("Winner !")
			break
		if mistake == 6:
			print(fail6)
			print("Hangman ... !")
			break
	except:
		print("Expected a character")
		print("".join(screen))
		print("Errores: "+str(mistake))