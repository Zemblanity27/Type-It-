# Type It!
## Video Demo: https://youtu.be/xxqS7uKVtCc
### Description:

Type It! is a simple typing test program where it gives the user a random paragraph to type out. It times the user and allows them to measure how long it will take to type out a random paragraph and gives a percentage accuracy depending on how many correct words they made.

### How it works:

Modules/Libraries Used:
time
pyfiglet
colored
random
csv

I used different modules or libraries to make this program which I will explain in the parts or functions where I used them. The first one would be the Main funciton.

### MAIN:
This is where I call all the other function I made that makes the test work. I also used a module called Pyfiglet for some ascii art to spice up the welcome screen.

### get_test
This function use the random and csv module/library to choose a paragraph from a csv file called test.csv. Currently the there's only 5 different paragraphs to choose randomly.

### countdown_test
This function tells the user to get ready and starts a countdown from 5 to 1 using the time library. This also reminds the user to press enter after finishing typing to submit what you have managed to finish.

### start_test
This one starts the typing test. After the countdown from 5 to 1, this prints the chosen paragraph from the get_test function for the user to copy and type. I used the time library to record the time the user started and then prompts the user to begin typing. After pressing enter or submiting what they have typed, the time is then again recorded which will be then subtracted to the starting time to get the total time the user have taken to finish. This also returns the total time and the user input of what they have managed to type.

### results
This one manage the results for the time and the input the user typed. I also used the pyfiglet module here to add some ascii arts for the results. I also used the module called colored to add some font color so the result may be easier to differentiate from the normal texts.

### percent_accuracy
The purpose of this last function is for checking the accuracy of the user. I set up a counter that adds up by matching the user input to the original paragraph that the program chose randomly for the test. Total correct characters divided by the length of the original paragraph multiplied by 100 to get the percentage accuracy. It prints the result after that.


