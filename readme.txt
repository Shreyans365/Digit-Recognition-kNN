The aim is to develop the most efficient kNN or Modified-kNN algorithm for classifying Handwritten Digits.

The Train Data is provided in the "train.txt" file, the layout of which is intelligible.
The Test Data is provided in the "testAll.txt" file having the same layout as the train file.
An Additional "test.txt" file has been included to test a single Instance.

Note-The input data must be in the form of either a 32x32 binary matrix (IN THE FORM OF A TEXT FILE) or a 32x32(px) Image.
     The Image provided should be in grayscale.


IMPORTANT LIBRARIES USED...(Surprisingly, Numpy was not needed)
1)PIL (Python Imaging Library)



-------------------------------------------------"DigitPredictor.py"------------------------------------------------- 
(Original Attempt employing the simplest form of kNN Algorithm)

The createData() function is used to import the Train Data by using the filename "train.txt".This Data is stored in a nested list.
Each element of the main list is a list having exactly 1025 elements.The first 1024 elements are either "1" or "0" and the 1025th element 
is a number belonging to {0,1,2,3,4,5,6,7,8,9}.
The first 1024 elements are treated as 1024 attributes and the 1025th element is basically the class to which that instance belongs.

The createTestVector() function which takes a file name (txt) as argument is called when a single Instance is to be tested.
It returns a vector having 1024 elements which are all either "1" or "0".

The prepareImageToVector() function returns a vector similar to createTestVector().The only difference is that the file name provided as argument
should be that of an IMG file.
The .convert('1') statement converts the input image to grayscale. (0s and 255s)
Each "255" present in the test vector is changed to "1" for the sake of printString() function mentioned below.

The createTestData() function which takes a file name as argument is called when Multiple Instances are to be tested.It returns
a list similar to createData()...except that each sub-list has 1024 elements.(The 1025th element which identifies the class of the instance is missing)

The printString() function was added to check if the test vector was created successfully or Not.
Its output is something like this...

00000000000000000001000000000000
00000000000000011111111000000000
00000000011111111111111110000000
00000000111111111111111110000000
00000001111111111000111111000000
00000001111111100000011111000000
00000011111110000000011111000000
00000011111110000000011111000000
00000011111000000001111110000000
00000011111000000011111110000000
00000011111100011111111000000000
00000011111111111111111000000000
00000001111111111111100000000000
00000001111111111111000000000000
00000001111111111111110000000000
00000000111111111111111000000000
00000000111111100001111110000000
00000000111110000000011110000000
00000001111110000000011110000000
00000001111100000000001111000000
00000001111100000000001111000000
00000001111100000000000111000000
00000001111100000000001111000000
00000001111000000000011111000000
00000001111100000000011110000000
00000001111100000001111110000000
00000001111100000011111100000000
00000000111111111111110000000000
00000000111111111111100000000000
00000000011111111110000000000000
00000000111111111000000000000000
00000000001100000000000000000000

The mode() function was created as a support function for the classifyUsingKNN() function.(Unfortunately Numpy does not have a mode() function)

The classifyUsingKNN() consists of the code for the kNN algorithm and is self explanatory.

Results -- The program has a 93.5% Accuracy for k=5

-------------------------------------------------------------------------------------------------------------------------------





