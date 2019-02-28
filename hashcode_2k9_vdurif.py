# Import
import sys
import math
import re
import random
from collections import OrderedDict

# CLASS

class Photo:

    # type: H (horizontal) or V (vertical)
    # tags: list()
    def __init__(self, type, tags, id):
        self.type = type
        self.tags = tags
        self.id = id

    def __str__(self):
        return "type: %s, tags: %s, id: %s" % (self.type, str(self.tags), self.id)

    def __repr__(self):
        return "type: %s, tags: %s, id: %s" % (self.type, str(self.tags), self.id)


class Slide:

    # type: H (horizontal) or V (vertical)
    # tags: set()
    # photos: [] (1 or 2 photos)
    def __init__(self, tags, photos, type):
        self.tags = tags
        self.photos = photos
        self.type = type

    def __str__(self):
        return " ".join([str(p.id) for p in self.photos])

    def __repr__(self):
        return " ".join([str(p.id) for p in self.photos])

	
# FUNCTIONS
def score(slide_1, slide_2):
    common = len(slide_1.tags.intersection(slide_2.tags))
    diff1 = len(slide_2.tags.difference(slide_1.tags))
    diff2 = len(slide_1.tags.difference(slide_2.tags))

    return min(common, diff1, diff2)

# LOAD DATA
#path = "a_example"
# path = "b_lovely_landscapes"
# path = "c_memorable_moments"
#path = "d_pet_pictures"
#path = "e_shiny_selfies"

mode = "r"
photos_vertical_list = []
photos_horizontal_list = []
with open (path + ".txt", mode) as reader:
    all_input = reader.readlines()
    N = int(all_input[0])
    for idx, line in enumerate(all_input[1:]):
        line_splitted = line.strip().split(' ')
        if line_splitted[0] == 'V':
            photos_vertical_list.append(Photo(line_splitted[0], line_splitted[2:], idx))
        else:
            photos_horizontal_list.append(Photo(line_splitted[0], line_splitted[2:], idx))


#configuration = all_input[0].split(' ')  # save the first line of the file containing the configuration as a list of words
#print (configuration)

# print([repr(photo) for photo in photos_vertical_list])
# print([repr(photo) for photo in photos_horizontal_list])


print('Lecture input')

# CODE
unordered_slide = []
for photo in photos_horizontal_list:
    unordered_slide.append(Slide(set(photo.tags), [photo], photo.type))

for i in range(len(photos_vertical_list)):
    for j in range(i+1, len(photos_vertical_list)):
        photo1 = photos_vertical_list[i]
        photo2 = photos_vertical_list[j]
        unordered_slide.append(Slide(set(photo1.tags + photo2.tags), [photo1, photo2], 'V'))

print('Nb slides : ' + str(len(unordered_slide)))
"""
print('unordered_slide init')
score_map = {}
max_score = -1
max_id = -1
for i in range(len(unordered_slide)):
    print(i)
    for j in range(i+1, len(unordered_slide)):
        slide1 = unordered_slide[i]
        slide2 = unordered_slide[j]
        current_score = score(slide1, slide2)
        if current_score > max_score:
            max_score = current_score
            max_id = i
        if i in score_map:
            score_map[i].append((j, current_score))
        else:
            score_map[i] = [(j, current_score)]
        if j in score_map:
            score_map[j].append((i, current_score))
        else:
            score_map[j] = [(i, current_score)]

print('calcul score')
for key, value in score_map.items():
    score_map[key] = sorted(score_map[key], key=lambda t: t[1])
print('tri score')
"""
# print([value for value in score_map.values()])
print('score_map initialisation')
initial = 0
max_iter = 100
max_limit = 7
slides_result = [unordered_slide[initial]]
last_slide = unordered_slide[initial]
already_in = set([photo.id for photo in unordered_slide[initial].photos])
del [unordered_slide[initial]]

while unordered_slide:
    max_value = -1
    max_id = -1
    next_slide = None
    next_slide_position = -1
    for i in range(max_iter):
        if i < len(unordered_slide):
            if set([photo.id for photo in unordered_slide[i].photos]).intersection(already_in):
                del unordered_slide[i]
            else:
                current_score = score(last_slide, unordered_slide[i])
                if current_score > max_limit:
                    next_slide = unordered_slide[i]
                    next_slide_position = i
                    break

                if current_score > max_value:
                    max_value = current_score
                    max_id = i
    else:
        if max_id > -1:
            next_slide = unordered_slide[max_id]
            next_slide_position = max_id
    if next_slide:
        print(len(unordered_slide))
        slides_result.append(next_slide)
        [already_in.add(photo.id) for photo in next_slide.photos]
        del unordered_slide[next_slide_position]
        last_slide = next_slide


# SAVE OUTPUT
outfile = open(path + ".out", "w+")

outfile.write(str(len(slides_result)) + "\n")
for slide in slides_result:
    outfile.write(str(slide) + "\n")

outfile.close()