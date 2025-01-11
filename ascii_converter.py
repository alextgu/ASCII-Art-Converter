from PIL import Image
from colorama import Fore, Style
import os

ASCII_order = "`^\",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255

def get_pixel_matrix(height, im):
    im.thumbnail((height, 200))
    pixels = list(im.getdata())
    return [pixels[i:i+im.width] for i in range(0, len(pixels), im.width)]

def get_intensity_matrix(matrix, algo='avg'):
    intensity_matrix = []
    for row in matrix:
        temp_row = []
        for i in row:
            if algo == "avg":
                temp_row.append(round((i[0]+i[1]+i[2])/3,2))
            elif algo == "max min":
                temp_row.append(round(((i[0]+i[2])/2),2))
        
            elif algo == "luminosity":
                temp_row.append(round(0.21*i[0] + 0.72*i[1] + 0.07*i[2],2))
            else:
                raise Exception('Undefined algorithm. Please try "avg", "max min" or "luminosity"')
        intensity_matrix.append(temp_row)
    return intensity_matrix

def get_char_matrix(intensity_matrix):
    char_matrix = []
    max_pixel = max(map(max, intensity_matrix)) # Darkest pixel
    min_pixel = min(map(min, intensity_matrix)) # Lightest pixel
    for row in intensity_matrix:
        temp_row = []
        for i in row:
            rescaled_pixel = max_pixel*(i-min_pixel)/float(max_pixel - min_pixel)
            temp_row.append(rescaled_pixel)
        char_matrix.append(temp_row)
    return char_matrix


def get_ASCII(intensity_matrix, ascii_chars):
    ascii_matrix = []
    for row in intensity_matrix:
        temp_row = []
        for i in row:
            temp_row.append(ascii_chars[int(i/MAX_PIXEL_VALUE * len(ascii_chars)) - 1])
        ascii_matrix.append(temp_row)
    return ascii_matrix

def save_ascii_image(input_path, output_path, text_colour):
    im = Image.open(input_path)
    pixels = get_pixel_matrix(1000, im)

    intensity_matrix = get_intensity_matrix(pixels, "avg")
    intensity_matrix = get_char_matrix(intensity_matrix)

    ascii_matrix = get_ASCII(intensity_matrix, ASCII_order)

    with open(output_path, 'w') as f:
        for row in ascii_matrix:
            line = "".join(row)
            f.write(text_colour + line + "\n")  
        f.write(Style.RESET_ALL) 

    return output_path 


"""
def print_ascii_matrix(ascii_matrix, text_color):
    for row in ascii_matrix:
        line = "".join(row)
        print(text_color + line)
    print(Style.RESET_ALL)


path = "/Users/agu/Desktop/ASCII_Art/static/files/download.jpeg"

im = Image.open(path)
pixels = get_pixel_matrix(1000,im)


intensity_matrix = get_intensity_matrix(pixels, "avg")
intensity_matrix = get_char_matrix(intensity_matrix)

ascii_matrix = get_ASCII(intensity_matrix, ASCII_order)
print_ascii_matrix(ascii_matrix, Fore.BLACK)


"""