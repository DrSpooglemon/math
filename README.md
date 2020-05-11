# math

Calculator 1.0
    This file contains a vastly improved calculator base class along with an extended class which takes 
    inputs and readies the data for the base class to process. The gui that goes with it is not ready 
    for upload yet.

Calculator
    First attempt is a very basic calculator and probably a bunch of spaghetti code. I'm going t0 work on 
    having a separate calculator class and GUI, then add other calculator functions.
    
    Second attempt at a calculator involves a separate Calculator class which is pretty lame.
    
    Third attempt, using Kivy for the GUI instead of pygame has a much improved Calculator class which can 
    handle parenthesis although the GUI does not allow for their input. The GUI is basic as hell but and I
    want to work on other things so it can wait. The Calculator class works just fine though.
    
    Fourth attempt, the gui extends the kivy gui from the thrid one and allows for inputing parentheses, 
    powers of numbers 0-9 imstead of just squaring and backspacing. The next steps will be to improve the 
    look of the gui and rethink the calculator class. I'm thinking it would make more sense to input a list 
    rather tan a string. 
    
    Fifth attempt, I'm going to leave the backspacing out just now as I want to move onto something else. In
    this version the gui creates a list of dictionary items that is then passed onto the calculator class. 
    This allows the calcualtor class to be more streamlined but it makes back and forward spacing a little 
    more complicated. I would also have to factor in the error handling if the user were to delete something
    from the input list. It's more work than I think this project deserves as a calculator isn't very exiting.
    I was only doing this to refine my OOP writing.

Fractionator.Fraction(frac,unit=0) calculator class object.
    'frac' takes a tuple argument (num,denom). 
    My debugged and upgraded version of the example class given in MIT's lecture on OOP published on youtube. 
    I added multiplication and division as well as ironing out the bugs in the other functions.
