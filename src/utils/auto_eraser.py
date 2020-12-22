import os
from operator import itemgetter

DATA_PATH = 'src/static/data/'
IMAGE_PATH = 'src/static/image/'
MAX_COUNT = 10


def erase_data():
    data_list = []
    for datafile in os.listdir(DATA_PATH):
        data_list.append([datafile, os.path.getctime(DATA_PATH + datafile)])
    data_list.sort(key=itemgetter(1), reverse=True)
    for i, datafile in enumerate(data_list):
        if i > MAX_COUNT - 1:
            os.remove(DATA_PATH + datafile[0])


def erase_image():
    image_list = []
    for imagefile in os.listdir(IMAGE_PATH):
        image_list.append(
            [imagefile, os.path.getctime(IMAGE_PATH + imagefile)])
    image_list.sort(key=itemgetter(1), reverse=True)
    for i, imagefile in enumerate(image_list):
        if i > MAX_COUNT - 1:
            os.remove(IMAGE_PATH + imagefile[0])


def main():
    erase_data()
    erase_image()


if __name__ == '__main__':
    main()
