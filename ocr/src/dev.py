from processor.utility.ocr import *
import cv2
# from processor.sheethandler.fullpage import recognizeSheet
from processor import recognizeJPG
# pdf2jpg('../data/QR_2B_Answersheet.pdf')
for i in range(0,1):
    # print ('loading ' + 'data/QR_2B_Answersheet-{}.jpg'.format(i))
    grayscale_image = cv2.imread('/Users/Norman//git/Answer-Sheet-OCR/ocr/data/ycb/2017-02-25-09-55-11-01_1-0.jpg'.format(i), cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(grayscale_image, 128, 255,
                                    cv2.THRESH_BINARY_INV)
    print _, binary_image
    kernel = np.ones((3,3),np.uint8)
    binary_image = cv2.dilate(binary_image, kernel, iterations=1)

    cv2.imshow('gray', cv2.resize(binary_image, (binary_image.shape[1]//3, binary_image.shape[0]//3)))
    # cv2.imwrite('tmp/handwritten.jpg', binary_image)
    cv2.waitKey(0)
    binary_image, contours, centers = adjustOrientation(binary_image, 'tmp/detect_{}.jpg'.format(i))
    # grayscale_image = cv2.imread('data/multiple_choice.jpg'.format(i), cv2.IMREAD_GRAYSCALE)
    # grayscale_image, contours, centers = adjustOrientation(grayscale_image, 'tmp/multiple_choice.jpg'.format(i))    
    # grayscale_image = cv2.imread('data/halfpage-0.jpg'.format(i), cv2.IMREAD_GRAYSCALE)
    # grayscale_image, contours, centers = adjustOrientation(grayscale_image, 'tmp/halfpage.jpg'.format(i))
    # grayscale_image = cv2.imread('data/handwritten.jpg'.format(i), cv2.IMREAD_GRAYSCALE)
    # grayscale_image, contours, centers = adjustOrientation(grayscale_image, 'tmp/handwritten.jpg'.format(i))
    # print ('loading done.')

    cv2.imshow('gray', cv2.resize(binary_image, (binary_image.shape[1]//3, binary_image.shape[0]//3)))
    cv2.imwrite('tmp/handwritten.jpg', binary_image)
    cv2.waitKey(0)

    h, w = binary_image.shape
    cv2.imwrite('/var/tmp/binary_image.jpg', binary_image)

    horizontal_pos, vertical_pos = getGridlinePositions(binary_image, contours, centers)
    # name = extractGrids(binary_image, horizontal_pos, vertical_pos, 0, 0, 2, 5)
    # g1 = extractGrids(binary_image, horizontal_pos, vertical_pos, 0, 7, 1, 1)
    # g2 = extractGrids(binary_image, horizontal_pos, vertical_pos, 0, 8, 1, 1)
    recognizeJPG("/Users/Norman/git/Answer-Sheet-OCR/ocr/data/half_answers-3.jpg", "halfpage")
    # recognizeSheet(binary_image, horizontal_pos, vertical_pos)
    # print ("g1:{}, g2:{}".format(getBlackRatio(g1), getBlackRatio(g2)))
    color_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(color_image, contours, -1, (0, 255, 0), thickness=10)

    for c in vertical_pos:
        cv2.line(color_image, (c, 0), (c, h-1), (0, 255, 0), thickness=10)
    for r in horizontal_pos:
        cv2.line(color_image, (0, r), (w-1, r), (0, 255, 0), thickness=10)

    color_image = cv2.resize(color_image, (w//3, h//3))
    cv2.imshow('color_image', color_image)
    # cv2.imshow('name', name)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
