# coco-box-extraction (and augmentation)

## Goal
We are working to extract annotations made available in JSON files and plot them on the COCO 2014 dataset images. We will also demonstrate different types of augmentations we can apply on these images.

## Sources

 2014 COCO dataset and annotations are available [here](https://cocodataset.org/#download).

[Download COCO 2014 val set (6 GB)](http://images.cocodataset.org/zips/val2014.zip)

[Download COCO train-val 2014 annotations (241 MB)](http://images.cocodataset.org/annotations/annotations_trainval2014.zip)

Since I am demostrating this extraction of annotated boxes and application of augmentation to the images in the validation set, I have randomly sampled 500 JPG files out of the available 40504 images in the zip files. The script `0_deleteJpgFiles.py` does this for us.

I have also deleted the files **instances_train2014.json**,  **person_keypoints_train2014.json** and **captions_train2014.json** since we are working with only the validation set. 

