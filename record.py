import pypuzzle
import os

img_path = '/home/david/recordsearch/imgs/'
search_img = '/home/david/recordsearch/camera.jpg'
img_dict = {}
dist_dict= {}
imgs = os.listdir(img_path)
current_img = ''


puzzle = pypuzzle.Puzzle()

# Set pypuzzle variables
puzzle.set_lambdas(15)
puzzle.set_p_ratio(1.5)
puzzle.set_autocrop(1)


# Create dictionary of compressed vectors from files in images
for img in imgs:    
    current_img = img_path + img
    vec = puzzle.get_cvec_from_file(current_img)
    cmp_vec = puzzle.compress_cvec(vec)
    img_dict[img] = cmp_vec

# Get vectors for search image
search_image_vec = puzzle.get_cvec_from_file(search_img)

# Get distance between images and search file
for key in img_dict:
    rec_name = key
    cmp_vec = img_dict[rec_name]
    uncmp_vec = puzzle.uncompress_cvec(cmp_vec)
    distance = puzzle.get_distance_from_cvec(search_image_vec, uncmp_vec)
    dist_dict[rec_name] = distance

closest_match = min(dist_dict, key=dist_dict.get)

print closest_match
print dist_dict[closest_match]

