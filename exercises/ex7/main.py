import cv2 as cv
from HodaDatasetReader.HodaDatasetReader import read_hoda_cdb, read_hoda_dataset


if __name__ == "__main__":
    print('Reading Train 60000.cdb ...')
    train_images, train_labels = read_hoda_cdb('./DigitDB/Train 60000.cdb')
    print('Reading Test 20000.cdb ...')
    test_images, test_labels = read_hoda_cdb('./DigitDB/Test 20000.cdb')
