Learning
Image classification:Create a classifier that decides the correct orientation of a given image.
The text files have one row per image, where each row is formatted like:

photo_id correct_orientation r11 g11 b11 r12 g12 b12 ...

Your  goal  is  to  implement  and  test  three  different  classifiers  on  this  problem:
k-nearestneighbors, AdaBoost, and neural networks.  
For training, your program should be run like this:

./orient.py train train_file.txt model_file.txt [model]

where[model]is one ofnearest,adaboost,nnet, orbest.  
This program uses the data in trainfile.txt toproduce a trained classifier of the specified type,

and save the parameters in modelfile.txt.  You may use any file format you’d like for modelfile.txt; the important thing is that your test code knows how to interpret it.

For testing, your program should be run like this:

./orient.py test test_file.txt model_file.txt [model]


Akshay ,Ameya and Praneta worked on this assignment.
