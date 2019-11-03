# Team8




#Backend algorithm for recommender system.
#python file "Hack_02_16_big.ipynb" and "Hack_02_16_big.py" are two python file which can be run as stand alone application also

requirment to run this file is to have two "stu_matBig.csv" and "vol_matBig.csv" files in the same folder where python file is stored.

However  two "stu_mat.csv" and "vol_mat.csv" can also be used as the small dataset.

These two files are being collected by forms and used for creating reccomendation systems.

It is dynamically scalable for selecting how many interviews should be schedules for students.

For example, If you want stiudents to take two interviews per day you can have only two mappings of studentId and it can also be increased based on requirment.

You can run this file bu runnin gcommand in terminal : "python Hack_02_16_big.py"

or can also open this file using jupyter notebook.

We are using user to user based collaborating filtering based on cosine similarity foe mapping interviewees to interviewers.

Ans the number of time slots are can be taken care by using approach that K-NN algorithm is taking.

Logic is made simple to implement however efficient at dynamix scaling level and providing quality lelvel.


