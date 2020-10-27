# Post-Mortem

This was my 2nd time working with Python. My 1st time to work with Python was about 6 months ago when I needed
to create a support script that could parse data from an XML document and create a JSON document with a
different structure.  I chose to learn Python at that time due to a recommendation from another team member
and found that it was well-suited for manipulating XML and JSON data structures.

This exercise provided a fun challenge to dust off my initial learnings and tackle the language again.


## Design Choices

What design choices did you make, and why? Include approaches that did and did not work.

* I created a sub-folder (mbstats) to organize files and classes.  As I started coding, I ended up creating
several additional classes that started to make the primary file (**stats.py**) unwieldy so I created a
folder and moved each of the classes into a separate file.

* I created a separate class for each of the levels (Topics, Threads, Messages) with a singleton pattern
to handle loading the data from the REST API and storing it in a cached object to be shared and re-used.
I feel like there is quite a bit of overlap between these that could probably be reduced using inheritance
concepts and sub-classes, but I did not explore that any further once I got the initial classes working.

* I also created helper classes for the business logic to calculate statistics.  My thought process here
was to traverse the data structures once and try to pull out multiple statistics at the same time to
make it more efficient in terms of memory and processing time.  For example:

    * Most common word
    * Avg number of words per sentence

* As I was creating the nested dictionary structure, I added the keys (Topic ID, Thread ID, Message ID) to
each level to assist with building out the structure.  The final JSON output was not specified, so this
met the requirements but is certainly not the most elegant solution.  If I spent some more time on this,
I probably would have 1st created an internal data structure that contained a graph of all of the relationships.
From there, I could have created a 2nd "pretty" data structure that mimicked the desired JSON output by
iterating through the graph using a DFS (Depth First Search) algorithm.

* I did add some error handling to my code, mostly as an excuse to learn and practice.

* I did not add any automated unit testing due to time constraints and my lack of experience with Python.


## Challenges

What did you find challenging?

* I initially had some challenges with setting up all the necessary packages on my Windows PC, but with
some help from Google I managed to work through all the issues that I encountered.

    * Poetry initially failed due to a misleading path variable for Python that the Windows store had configured.
        The path included **python.exe** but was apparently a shortcut to the Windows store instead of the
        correct reference to the Python executable.

    * make initially failed due to a dependency on Visual C++ 14.0, which I had to go download

* Creating the nested dictionary presented a challenge due to not having the Topic ID for a Message, but I
was able to resolve that by creating a lookup dictionary using the data from the Threads.


## Decisions

What interesting decisions did you make along the way?

* I attempted to follow some of the Python conventions that I found from examples or from the PEP8 site.
Most likely, the end result still looks like a Java programmer who is fairly new to Python.

* In the interest of time, I stopped before tackling the Edit and Delete challenges.


## Feedback

Any other feedback you want to include

* Overall, this was a good excuse for me to spend some more time learning the Python language.

* A suggested JSON message structure for the output file could be included with the exercise.