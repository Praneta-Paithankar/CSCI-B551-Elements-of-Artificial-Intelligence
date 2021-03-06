Let’s say we’ve already divided a text string image up into little subimages corresponding to individual letters;
a real OCR system has to do this letter segmentation automatically,  but here we’ll assume a fixed-width font so that we know exactly where each letter begins and ends ahead of time.  In particular, we’ll assume each letter fits in a box that’s 16 pixels wide and 25 pixels tall.  

We’ll also assume that our documents only have the 26 uppercase latin characters, the 26 lowercase characters, the 10 digits, spaces, and 7 punctuationsymbols,(),.-!?’". 

Suppose we’re trying to recognize a text string with n characters, so we have n observed variables (the subimage corresponding to each letter)O1, ..., On and n hidden variables,l1..., ln, which are the letters we want to recognize.  We’re thus interested in P(l1, ..., ln|O1, ..., On). 

As in part 1, we can rewrite this using Bayes’ Law, estimateP(Oi|li) and P(li|li−1) from training data, then use probabilistic inference to estimate the posterior, in order to recognize letters.What to do?

Write a program called ocr.py that is called like this:
./ocr.py train-image-file.png train-text.txt test-image-file.png

The  program  should  load  in  the  image  file,  which  contains  images  of  letters  to  use  for  training It should also load in the text training file, which is simply some text document that is representative of the language (English, in this case) that will be recognized.  (The training file from Part1 could be a good choice).  Then, it should use the classifier it has learned to detect the text in test-image-file.png, using (1) the simple Bayes net of Figure 1b, (2) the HMM of Fig 1a with variable elimination, and(3) the HMM of Fig 1a with MAP inference (Viterbi).  The last three lines of output from your programshould be these three results,
