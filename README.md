# First Assignment for Research Track 1

### Introduction to the Code
There are 5 functions: *_drive_*, *_turn_*, *_find_silver_*, *_find_golden_* and *_checklist_*; each function is explained into the *_FirstAssignment.py_*.

The 'while cycle' represents the steps that the robot must take to achieve the goal: to pair each **_SILVER_** token with each **_GOLDEN_** token.
  1. The first step represents the robot that initially look the closest **_SILVER_** token and tries to take it;
  2.  Once taked, the program stores the offset of the **_SILVER_** token into the List 'tokens_taked' so that it no longer
	has to be considered among all the available SILVER tokens;
  3. After that, the robot look the closest **_GOLDEN_** token and release the **_SILVER_** token near to the **_GOLDEN_** token;
  4. At this point, the program stores the offset of the **_GOLDEN_** token into the List 'tokens_taked' so that it no longer
	has to be considered among all the available **_GOLDEN_** tokens;
  5. Now, the List has the first Pair and the program will continue to repeat each step until the last **_GOLDEN_** token
	because after the last, the program will warn us with a message that tells *_'List Full, impossible to continue!'_*

If you want to run the code, just follow steps below:
1. **_open the terminal shell;_**
2. **_move into this path:_** `FirstAssignmentRT1/python_simulator_rt1/robot-sim`**_;_**
3. **_write this line of code:_** `$python2 run.py FirstAssignment.py`**_;_**

### PseudoCode
In the while loop:

If the list is full, all tokens paired

    print: 'is not possible to continue because the list of tokens paired is full..'

    the program exits the loop and ends

If state is equals to True

    the robot look the closest Silver token

else
    
    the robot look the closest Golden token

If is not found a token

    the robot turn
    
else if the current distance from the robot to the token is less than 0.4 and the token found is Silver

    print: 'found the Silver'
    
    the robot grab the token
    
    the token is stored into the list
    
    the robot takes a few steps back
    
    the variable 'state' changes value
    
else if the current distance from the robot to the token is less than 0.6 and the token found is Golden

    print: 'found the Golden'
    
    the robot release the Silver token near to the Golden token
    
    the token is stored into the list
    
    print: 'paired!'
    
    the robot takes a few steps back
    
    the variable 'state' changes value
    
else if the robot is well aligned with the token

    print: 'ah, here we are'
    
    the robot go forward

else if the robot is not well aligned with the token

    print: 'left, a bit..' or print: 'right, a bit..'
    
    the robot turn left or turn right
    
### Future Improvements ###
*_Allow the robot to always find the closest token to it by performing, for example, a 360 degree turn on itself to store the distances of all the tokens present in the environment into a list and improve execution time_*
