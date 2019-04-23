"""
Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""
def rotate(image: list):
    for layer in range(len(image)//2):
        first = layer
        last = len(image) - 1 - layer

        for i in range(first, last):
            offset = i - first  
            top = image[first][i]

            # left -> top
            image[first][i] = image[last-offset][first]

            # bottom -> left
            image[last-offset][first] = image[last][last-offset]

            # right -> bottom
            image[last][last-offset] = image[i][last]

            # top -> right
            image[i][last] = top