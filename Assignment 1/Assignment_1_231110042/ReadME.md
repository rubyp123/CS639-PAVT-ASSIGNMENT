RUBY PRAJAPATI 231110042
Here are some instructions for running file

fuzzSubmission.py file is in submission folder.
5 test cases are in test cases folder inside kachuaCore folder.
Test_Cases folder is in side KachuaCore.
Inside Tescases folder there is outputs folder with screenshort of outputs.

for running fuzzSubmission.py file ,
 1. open cammand promt in kachuaCore folder.
 2. Write cammand - " python kachua.py -t 30 --fuzz Test_Cases/example2.tl -d{':w':2,':x':3,':y':5,':z':6} "
 3. If you want to run other test cases just change name of file (<filie_name.tl>) and number of inputs in -d parameter.
 4. -t is duration of program to be run in seconds , can change value for changing duration of running program.

Exmaple files are in example folder
 1. example1.tl file takes one input (:m)
 2. example2.tl file takes four inputs (:x,:y,:z,:w)
 3. example3.tl file takes four input (:x,:y,:z,:w)
 4. example4.tl file takes tree inputs (:x,:y,:z)
 5. example5.tl file takes four inputs(:x,:y,:z,:w)

