# Conference Track Management

This is a Bin Packing like problem, the strategy behind this algorithm is to find the best fit of to spread a set os numbers in a given amount of bin(s) and size(s). 

In this solution, because the shifts are variable in size (morning has 180mins, afternoon has 240mins), we consider the shifts as being the "bins" and the talk and their durations as being the packages, after spreading the talks in shifts, the shifts also are spread in tracks (days), following an order (morning -> afternoon -> morning..).

## Requirements:

    python 2.7+

## Instructions to run the project

###### In your unix like command line type:
    
    $: python app.py < input.txt

## Testing with python's unittest


###### All suite at once
    $: python -m unittest discover -s src 
    

###### Single modules
    
    $: python -m unittest src.entity.tests.test_shift
    $: python -m unittest src.entity.tests.test_track
    
    $: python -m unittest src.service.scheduler.tests.test_scheduler
    $: python -m unittest src.service.scheduler.tests.test_bin_packing
    
    $: python -m unittest src.service.io.tests.test_talk_reader
    $: python -m unittest src.service.io.tests.test_track_writer
    

## Design

First, I've opted to develop it in python mostly because of familiarity concerns over the other languages, being a non typed language allows to prototype ideas very fast, also, python's built in debugger and unit testing framework works like a PyCharm (ba dum tss) in my IDE.

## Architecture

In order to spreads the talks in bins with different sizes, there is an aggregation between classes, A Track(day) has multiple Shifts(morning, afternoon), and each Shift contains the best fitted number of Talks.

There are classes to handle IO operations, like reading and parsing the stdin contents into a list of Talks, and further, printing the processed schedule of Tracks.

The main logic, that spreads the talks and shifts, according to the best fit for their sizes, is contained in the service classes (Scheduler and BinPacking).


###### References

1. https://en.wikipedia.org/wiki/Bin_packing_problem
2. https://www.python.org/dev/peps/pep-0008/#naming-conventions
3. https://docs.python.org/3/library/unittest.html#organizing-tests
4. https://medium.com/@dasagrivamanu/python-naming-conventions-the-10-points-you-should-know-149a9aa9f8c7
5. https://docs.python.org/2/library/datetime.html

