Learning
Image classification:Create a classifier that decides the correct orientation of a given image.
The text files have one row per image, where each row is formatted like:

photo_id correct_orientation r11 g11 b11 r12 g12 b12 ...

k-nearestneighbors, AdaBoost, and neural network are implemented to classify the images  

For training, program run like this:

./orient.py train train_file.txt model_file.txt [model]

where[model]is one ofnearest,adaboost,nnet, orbest.  
This program uses the data in trainfile.txt to produce a trained classifier of the specified type,
and save the parameters in modelfile.txt.  

For testing, your program run like this:

./orient.py test test_file.txt model_file.txt [model]


Akshay ,Ameya and Praneta worked on this assignment.
