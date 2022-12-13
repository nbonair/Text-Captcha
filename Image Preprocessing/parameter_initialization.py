char_list = string.ascii_letters+string.digits
characters = set(char for char in char_list)
characters = sorted(list(characters))
img_height = 50
img_width = 200
# Map text to numeric labels 
char_to_num = {char:idx for idx, char in enumerate(characters)}

# Map numeric labels to text
num_to_char = {val:key for key, val in char_to_num.items()}
