## Daniel Turnquist
## turnq070
import copy

# Part A: Red Blue Swap
#==========================================
# Purpose:
#   Swaps the red and blue components in an image
# Input Parameter(s):
#   A 3D matrix (list of lists of lists) representing an .bmp image
#   Each element of the matrix represents one row of pixels in the image
#   Each element of a row represents a single pixel in the image
#   Each pixel is represented by a list of three numbers between 0 and 255
#   in the order [red, green, blue]
# Return Value:
#   A 3D matrix of the same dimensions, with all colors inverted
#   (that is, for every pixel list, the first and last values have been
#   swapped.
#==========================================
def red_blue_swap(img_matrix):
    for row in img_matrix:
        for pix in row:
            pix[0], pix[2] = pix[2], pix[0]
    return img_matrix

# Part B helper: weighted average
#==========================================
# Purpose:
#   Takes in the RGB value of a pixel and uses the formula avg = 0.3*red + 0.59*green + 0.11*blue to calculate the greyscale value
# Input Parameter(s):
#   A single pixel object
# Return Value:
#   An integer representing the truncated greyscaled RGB value of the pixel.
#==========================================
def weighted_ave(pix):
    return int(0.3 * pix[0] + 0.59 * pix[1] + 0.11 * pix[2])

# Part B: Grayscale
#==========================================
# Purpose:
#   Converts an image to grayscale
# Input Parameter(s):
#   A 3D image matrix (see part 1)
# Return Value:
#   A 3D matrix of the same dimensions, where each pixel has all components
#   (red, green, blue) set to a value determined by the formula:
#       0.3*red + 0.59*green + 0.11*blue
#   and then truncated down to the nearest integer.
#==========================================
def grayscale(img_matrix):
    for row in img_matrix:
        for pix in row:
            gray_val = weighted_ave(pix)
            pix[0], pix[1], pix[2] = gray_val, gray_val, gray_val
    return img_matrix

# Part C helper: pixel compressor
#==========================================
# Purpose:
# averages the RGB values of a square of four pixels to create a single pixel out of four initial ones.
# Input Parameter(s):
# four pixel objects in a square
# Return Value:
#   A single RBG pixel object
#==========================================
def compress_pixels(pix1, pix2, pix3, pix4):
    R = int((pix1[0] + pix2[0] + pix3[0] + pix4[0]) / 4)
    G = int((pix1[1] + pix2[1] + pix3[1] + pix4[1]) / 4)
    B = int((pix1[2] + pix2[2] + pix3[2] + pix4[2]) / 4)
    return [R, G, B]

# Part C: Split
#==========================================
# Purpose:
#   Splits an image into four copies of itself, each with half the dimensions
#   of the original.  Computes each component of the output image's pixels by
#   taking the corresponding 2x2 square of pixels in the original and averaging
#   that component among those four pixels (truncating this average down to the
#   nearest integer).  See instructions for more details.
# Input Parameter(s):
#   A 3D image matrix (see part 1).  You may assume that the width and height
#   of the image are both even, so that each 1 pixel in the output image
#   corresponds to one 2x2 square of pixels in the input.
# Return Value:
#   A 3D matrix of the same dimensions, with the transformation described above.
#==========================================
def split(img_matrix):
    height = len(img_matrix)
    width = len(img_matrix[0])
    output = copy.deepcopy(img_matrix)
    for y in range(height)[::2]:
        for x in range(width)[::2]:
            output[y // 2][x // 2] = compress_pixels(img_matrix[y][x], img_matrix[y][x + 1], img_matrix[y + 1][x], img_matrix[y + 1][x + 1])
            output[int(y // 2 + height / 2)][x // 2] = compress_pixels(img_matrix[y][x], img_matrix[y][x + 1], img_matrix[y + 1][x], img_matrix[y + 1][x + 1])
            output[y // 2][int(x // 2 + width / 2)] = compress_pixels(img_matrix[y][x], img_matrix[y][x + 1], img_matrix[y + 1][x], img_matrix[y + 1][x + 1])
            output[int(y // 2 + height / 2)][int(x // 2 + width / 2)] = compress_pixels(img_matrix[y][x], img_matrix[y][x + 1], img_matrix[y + 1][x], img_matrix[y + 1][x + 1])
    return output





# DO NOT EDIT ANYTHING BELOW THIS LINE

# Helper function (you don't have to understand what this does)
#==========================================
# Purpose:
#   Compute the integer represented by a sequence of bytes
# Input Parameter(s):
#   A list of bytes (integers between 0 and 255), in big-endian order
# Return Value:
#   Integer value that the bytes represent
#==========================================
def big_end_to_int(ls):
    total = 0
    for ele in ls[::-1]:
        total *= 256
        total += ele
    return total

# .bmp conversion function (you don't have to understand what this does)
#==========================================
# Purpose:
#   Turns a .bmp file into a matrix of pixel values, performs an operation
#   on it, and then converts it back into a new .bmp file
# Input Parameter(s):
#   fname, a string representing a file name in the current directory
#   operation, a string representing the operation to be performed on the
#   image.  This can be one of 3 options: 'invert', 'grayscale',
#   or 'split'.
# Return Value:
#   None
#==========================================
def transform_image(fname,operation):
    #Open file in read bytes mode, get bytes specifying width/height
    fp = open(fname,'rb')
    data = list(fp.read())
    old_data = list(data)
    width = big_end_to_int(data[18:22])
    height = big_end_to_int(data[22:26])

    #Data starts at byte 54.  Create matrix of pixels, where each
    #pixel is a 3 element list [red,green,blue].
    #Starts in lower left corner of image.
    i = 54
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = [data[i+2],data[i+1],data[i]]
            i += 3
            row.append(pixel)
        matrix.append(row)
        #Row size must be divisible by 4, otherwise padding occurs
        i += (2-i)%4
    fp.close()

    #Perform operation on the pixel matrix
    if operation == 'red_blue_swap':
        new_matrix = red_blue_swap(matrix[::-1])
    elif operation == 'grayscale':
        new_matrix = grayscale(matrix[::-1])
    elif operation == 'split':
        new_matrix = split(matrix[::-1])
    else:
        return
    new_matrix = new_matrix[::-1]
    #Write back to new .bmp file.
    #New file name is operation+fname
    i = 54
    for y in range(height):
        for x in range(width):
            pixel = tuple(new_matrix[y][x])
            data[i+2],data[i+1],data[i] = pixel
            i += 3
        i += (2-i)%4
    fp = open(operation+"_"+fname,'wb')
    fp.write(bytearray(data))
    fp.close()

