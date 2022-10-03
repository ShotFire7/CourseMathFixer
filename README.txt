# Online Course fix by https://github.com/ShotFire7
# This program is for Canvas! And it works on things other than math!


Q: What does this do?
A: This program takes the previous questions you answered on a quiz, and when you retake that quiz,
it will return the order of multiple choice answers as numbers (like this: [3, 2, 4, 1...]) so you can
quickly re input your previous answers without wasting time. Currently, this program only works with
multiple choice questions.

Q; Why did you make this?
A: So, most online college courses are really annoying in the fact that if you get a single question wrong on a quiz, you'll
have to redo the whole thing to get 100%. It doesn't seem that annoying until you realize that they also randomize the order
of all the questions and answers for absolutely no reason, causing you to take more time re answering questions that you already
solved.


DISCLAIMER:
This program does NOT provide answers. It just helps you re input the answers you had before when retaking a quiz
to save time.


To use:
1.) Go to the quiz session that you missed questions on
2.) Right click anywhere on the page and click inspect element
3.) The second line in inspect element should begin with <html .... Click the line and do ctrl C
4.) ctrl V that line into data.txt
5.) Start a new quiz session
6.) Repeat steps 2-3
7.) ctrl V that line into data2.txt
8.) run STARTAPP.bat
9.) The console will print a list of numbers. That list is the order of multiple choice you're supposed to choose
    For example, if the first number in the list is 4, then for the first question, I choose choice #4.

Troubleshooting:
If you're on Mac or Linux, or if startapp.bat doesn't work, just open cmd or the equivalent for your os, type in cd and then the directory the file
is downloaded to, and then type in "main" and press enter. 

If the app bugs out, then the site you're using it on is likely not supported.
