import re

def preprocess(text: str) -> str:
    """
    clean and normalisation of text
    """
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = text.strip() # Remove whitespaces at the start and end of the word

    return text

#i/p
#I am
#The best player in the world 

#o/p
#I am the best player in the world

# i/p
# I am   the best player in the world
# o/p 
# I am the best player in the world

# i/p
#      I am the best player in the world
# o/p
# I am the best player in the world