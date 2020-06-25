# Instructions

This repository contains the [Django](https://docs.djangoproject.com/en/2.2/)
project for a bare-bones, anonymous message board, structured as *Topic > Thread > Message*.
Users cannot create new Topics, but they can create new Threads and
Messages.

To get started, please [fork the
repository](https://github.com/CloudBoltSoftware/coding-exercise/fork).

## Tasks

Complete the following tasks in priority order:

1. Using the `stats.py` script, which interacts with the messageboard REST API
   (http://localhost:8080/api/), and return the following information:
    1. Total number of messages
    1. Most frequently used word in messages.
    1. Average number of words per sentence.
    1. Average number of messages per thread, per topic.
    1. Finally, compile the entire message board into a single JSON object, and
       write it to `messageboard.json`.
1. Add the ability to edit and/or delete a message.

After you've completed the above tasks, implement one or more features of your
choosing. Here are some ideas:

1. Add a pagination method to the Thread model.
1. Reimplement the message board as a non-web application. For example, a
   command-line application.
1. Add a new type of message that communicates with an external API.
1. Write a web front-end using the REST API.
1. Add users and authentication.
1. Implement a natural language processing (NLP) feature.
1. Add the ability to vote on topics.
1. Anything else you can think of!

## Post-Mortem

After you've finished with development, we ask that you write up a
**post-mortem** with the following questions as a starting point:

1. What design choices did you make, and why? Include approaches that did and
   did not work.
1. What did you find challenging?
1. What interesting decisions did you make along the way?
1. Any other feedback you want to include

## Submission

When you're finished, please send a link to your forked version of this
repository to your hiring contact.

## Expectations

If you don’t complete all the tasks, that’s absolutely fine. We’re asking that
you spend a maximum of 3 hours of total development time working on this
assignment, distributed however you see fit. Some candidates will be able to
complete all requested tasks in the allotted time, but people work at different
rates, and folks have different expertise. We’re more interested to see what you
can get done in 3 hours and how you approach problems like these.

We may ask you about this in a future interview, so we encourage you to take
notes!

### Evaluation Criteria

Here's what we're looking for:

* Code quality
* Communication
* Python chops
* Feature design
* Test quality
* Django dj-chops