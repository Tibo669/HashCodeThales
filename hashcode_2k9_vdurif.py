# Import
import sys
import math
import re
import random

# CLASS

class Photo:

    # type: H (horizontal) or V (vertical)
    # tags: set()
    def __init__(self, type, tags, id):
        self.type = type
        self.tags = tags
        self.id = id


class Slide:

    # type: H (horizontal) or V (vertical)
    # tags: set()
    # photos: [] (1 or 2 photos)
    def __init__(self, tags, photos, type):
        self.tags = tags
        self.photos = photos
        self.type = type

    def __str__(self):
        return " ".join([p.id for p in self.photos])

    def __repr__(self):
        return " ".join([p.id for p in self.photos])

	
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
photos_vertical_list = []
photos_horizontal_list = []
with open (path + ".txt", mode) as reader:
    all_input = reader.readlines()
    N = int(all_input[0])
    for idx, line in enumerate(all_input[1:]):
        line_splitted = line.split(' ')
        if line_splitted[0] == 'V':
            photos_vertical_list.append(Photo(line_splitted[0], line_splitted[2:], idx))
        else:
            photos_horizontal_list.append(Photo(line_splitted[0], line_splitted[2:], idx))


#configuration = all_input[0].split(' ')  # save the first line of the file containing the configuration as a list of words
#print (configuration)



# CODE


slides_result = []
# SAVE OUTPUT
outfile = open(path + ".out", "w+")

outfile.write(len(slides_result + "\n"))
for slide in slides_result:
    outfile.write(slide + "\n")

outfile.close()