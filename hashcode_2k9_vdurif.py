# Import
import sys
import math
import re
import random

# CLASS

class Photo:

    # type: H (horizontal) or V (vertical)
    # tags: set()
    def __init__(self, type, tags):
        self.type = type
        self.tags = tags


class Slide:

    # type: H (horizontal) or V (vertical)
    # tags: set()
    # photos: [] (1 or 2 photos)
    def __init__(self, tags, photos, type):
        self.tags = tags
        self.photos = photos
        self.type = type

	
# FUNCTIONS
def score(slide_1, slide_2):
    common = slide_1.tags.intersection(slide_2.tags)
    diff1 = slide_2.tags.difference(slide_1.tags)
    diff2 = slide_1.tags.difference(slide_2.tags)
	
	return min(common, diff1, diff2)

# LOAD DATA
path = "a_example"
#path = "b_lovely_landscapes"
#path = "c_memorable_moments"
#path = "d_pet_pictures"
#path = "e_shiny_selfies"

mode = "r"
with open (path + ".in", mode) as reader:
	all_input = (reader.readlines())
	reader.close()

#configuration = all_input[0].split(' ')  # save the first line of the file containing the configuration as a list of words
#print (configuration)



# CODE


# SAVE OUTPUT
outFile = open(path + ".out", "w+")

result = []
for val in result:
	outFile.write(repr(val) + "\n")

outFile.close()