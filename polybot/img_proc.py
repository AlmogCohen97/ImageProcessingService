from pathlib import Path
from matplotlib.image import imread, imsave
import random


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


class Img:
    def __init__(self, path):
        """
        Do not change the constructor implementation
        """
        self.path = Path(path)
        self.data = rgb2gray(imread(path)).tolist()

    def save_img(self):
        """
        Do not change the below implementation
        """
        new_path = self.path.with_name(self.path.stem + '_filtered' + self.path.suffix)
        imsave(new_path, self.data, cmap='gray')
        return new_path

    def get_dimensions(self):
        return len(self.data), len(self.data[0])

    def blur(self, blur_level=16):

        height = len(self.data)
        width = len(self.data[0])
        filter_sum = blur_level ** 2

        result = []
        for i in range(height - blur_level + 1):
            row_result = []
            for j in range(width - blur_level + 1):
                sub_matrix = [row[j:j + blur_level] for row in self.data[i:i + blur_level]]
                average = sum(sum(sub_row) for sub_row in sub_matrix) // filter_sum
                row_result.append(average)
            result.append(row_result)

        self.data = result

    def contour(self):
        for i, row in enumerate(self.data):
            res = []
            for j in range(1, len(row)):
                res.append(abs(row[j-1] - row[j]))

            self.data[i] = res

    def rotate(self):
        # Variables of image's dimensions
        height = len(self.data)
        width = len(self.data[0])

        # Create a new empty image with swapped dimensions
        rotated_img = [[0] * width for _ in range(height)]
        # Copy pixel value to => rotate_img
        for row in range(width):
            for col in range(height):
                rotated_img[col][width - 1 - row] = self.data[row][col]

        return rotated_img

        raise NotImplementedError()


    def salt_n_pepper(self):
        # TODO remove the `raise` below, and write your implementation
        # Variables of image's dimensions
        height = len(self.data)
        width = len(self.data[0])

        # Randomly pick some pixels in the image
        num_of_pixels = random.randint(30000, 100000)
        for i in range(num_of_pixels):
            # Randomly pickups coordination
            y_cort = random.randint(0, (height-1))
            x_cort = random.randint(0, (width - 1))
            self.data[y_cort][x_cort] = 255   # Color White!

        # Randomly pick some pixels in the image
        num_of_pixel = random.randint(30000, 100000)
        for i in range(num_of_pixel):
            # Randomly pickups coordination
            y_cort = random.randint(0, height-1)
            x_cort = random.randint(0, width - 1)
            self.data[y_cort][x_cort] = 0   # Color Black!

        return self.data

        raise NotImplementedError()

    def concat(self, other_img, direction='horizontal'):

        # if Path(other_img.path[0]).exists() == False:
        #   print("Your other img path wrong..")
        #   raise NotImplementedError("Wrong path")

        if direction == 'horizontal':
            if self.get_dimensions()[0] != other_img.get_dimensions()[0]:
                raise RuntimeError("Image heights are not compatible for horizontal concatenation.")
            new_data = [row + other_img.data[i] for i, row in enumerate(self.data)]
        elif direction == 'vertical':
            if self.get_dimensions()[1] != other_img.get_dimensions()[1]:
                raise RuntimeError("Image widths are not compatible for vertical concatenation.")
            new_data = self.data + other_img.data
        else:
            raise ValueError("Invalid direction. Use 'horizontal' or 'vertical'.")

        # Store the concatenated image
        self.data = new_data
        return self

        raise NotImplementedError()

    def segment(self):
        # TODO remove the `raise` below, and write your implementation
        image = self.data

        for x in range(len(image)):
            for y in range(len(image[x])):
                #
                if image[x][y] > 100:
                    image[x][y] = 255
                else:
                    image[x][y] = 0

        return image




my_img = Img('/home/almog/PycharmProjects/ImageProcessingService/polybot/test/beatles.jpeg')
# another_img = Img('/home/almog/PycharmProjects/ImageProcessingService/polybot/test/beatles2.jpeg')
my_img.rotate()
my_img.save_img()
# concatenated image was saved in 'path/to/image_filtered.jpg'
