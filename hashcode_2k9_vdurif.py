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
    score = 0

    common_tags = slide_1.tags
    tags_slide1_not_slide2 = set(slide_1.tags)
    tags_slide2_not_slide1 =

    return min()

# LOAD DATA
path = "a_example"
#path = "b_lovely_landscapes"
#path = "c_memorable_moments"
#path = "d_pet_pictures"
#path = "e_shiny_selfies"

mode = "r"
photos_vertical_list = []
photos_horizontal_list = []
with open (path + ".txt", mode) as reader:
    all_input = reader.readlines()
    N = int(all_input[0])
    for line in all_input[1:]:
        line_splitted =  line.split(' ')
        if Photo(line_splitted[0] == 'V':
            photos_vertical_list.append(Photo(line_splitted[0], line_splitted[2:]))
        else:
            photos_horizontal_list.append(Photo(line_splitted[0], line_splitted[2:]))


#configuration = all_input[0].split(' ')  # save the first line of the file containing the configuration as a list of words
#print (configuration)



# CODE


# SAVE OUTPUT
outFile = open(path + ".out", "w+")

result = []
for val in result:
    outFile.write(repr(val) + "\n")

outFile.close()