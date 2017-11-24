import cv2
import numpy as np

def printHistAndCommHist(inputPath, outputPath):
    # init basic vars
    cameraman = cv2.imread(inputPath,0)
    cameramanHistogram = np.full((256), 0)
    cameramanCommHistogram = np.full((256), 0)

    # get histogram
    for i in range (len(cameraman)):
        for j in range (len(cameraman[i])):
            value = cameraman[i][j]
            cameramanHistogram[value] += 1

    # get comm histogram
    cameramanCommHistogram[0] = cameramanHistogram[0]
    for i in range (1, 256):
        cameramanCommHistogram[i] = cameramanHistogram[i] + cameramanCommHistogram[i - 1]

    # create new image
    cameramanNew = np.zeros((512,1024,3), np.uint8)
    maxHisHeightNorm = int(max(cameramanHistogram) / 512)
    maxCommHisHeightNorm = int(max(cameramanCommHistogram) / 512)

    for i,j in zip(range(0, 1024, 4), range(0, 256)):
        hisNormHeight = int(cameramanHistogram[j] / maxHisHeightNorm)
        comHisNormHeight = int(cameramanCommHistogram[j] / maxCommHisHeightNorm)
        cv2.line(cameramanNew, (i, 511), (i, 512 - comHisNormHeight), (140, 140, 140), 2)
        cv2.line(cameramanNew, (i, 511), (i, 512 - hisNormHeight), (80, 80, 80), 1)

    cv2.imwrite(outputPath, cameramanNew)


def mystery():
    originalImage = cv2.imread("inputs/tree.png",0)
    modifiedImage = cv2.imread("inputs/treeM.png",0)
    diffImage = np.zeros((len(originalImage),len(originalImage[0]),3), np.uint8)


    for i in range (len(originalImage)):
        for j in range (len(originalImage[i])):
            value = modifiedImage[i][j] - originalImage[i][j]
            diffImage[i][j] = value

    cv2.imwrite("outputs/treeNew.png", diffImage)

# Exec funcs
printHistAndCommHist("inputs/cameraman.png", "outputs/cameramanNew.png")
printHistAndCommHist("inputs/bat.png", "outputs/batNew.png")
printHistAndCommHist("inputs/fog.png", "outputs/fogNew.png")
printHistAndCommHist("inputs/fognoise.png", "outputs/fognoiseNew.png")
mystery()