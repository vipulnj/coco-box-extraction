import os
from glob import glob
from random import Random

# set data
numImages = 50
seedValue = 42

allImagesFiles = glob('val2014_copy/*.jpg')
imageFiles = Random(seedValue).choices(allImagesFiles, k=numImages)

allFilesExceptSampledFiles = list(set(allImagesFiles) - set(imageFiles))
print("len(images) =", len(imageFiles), "\n")
for file in allFilesExceptSampledFiles:
    os.remove(file)

# rename directory
os.rename('val2014', f'val2014_{numImages}')