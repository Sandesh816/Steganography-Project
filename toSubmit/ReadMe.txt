This is a ReadMe document for an Steganography project, where we will be extracting hidden messages and images from an image.

Modules needed: 
1) numpy
2) imageio

Description of functions:

1) extract_lsb_from_image(image_path, bit_count):

Parameters:
image_path: path to the image where messages are hidden
bit_count: the length of your hidden message
Working:
First, we process the image from the given path. Then, going from top->bottom, left-> right, we store the least significant bit of red, green, and blue from each pixel. We do this until our array has bits >= bit_count
Then, it returns the first bit_count number of bits from our array

2) binary_to_int(binary_list):

Parameters:
binary_list: a list that contains a binary string
Working:
we just convert the given binary string in the form of a list into an integer.

3) main:

To get hidden text from image:
We know that header for text will be of 32 bits. So, we extract first 32 bits using function 1. Then, we convert it to an integer to get the size of the hidden text message. Then, we call function 1 again, and this time, we extract 32+length from earlier function call, then we extract the bits after the first 32 bits. And, they are the hidden text messages in our given image.

To get hidden image from an image:
We know that header for image will be of 64 bits. So, we extract first 64 bits using function 1 and we get the height and width of the hidden image. Then, we extract least significant bits from first 64 + (height * width * 3 * 8) number of bits from the image. Then, we remove first 64 bits as they are header bits. Then, we construct the hidden image using the height and width variables that we had computed. 
