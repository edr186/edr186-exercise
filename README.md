# CloudBolt Take-Home Coding Exercise

Congratulations, you passed the [CloudBolt Software](http://cloudbolt.io) hiring
screen. The next step is to demonstrate your coding and design chops at your own
pace, and show us what you’re capable of!

## Instructions

This repository contains the [Django](https://docs.djangoproject.com/en/2.2/)
project for a bare-bones, anonymous message board, structured as 
*Topic > Thread > Message*. Users cannot create new Topics, but they can create
new Threads and Messages.

To get started, please [fork the
repository](https://github.com/CloudBoltSoftware/coding-exercise/fork).

### Tasks

Complete the following tasks in priority order:

1. Using the `stats.py` script, which interacts with the messageboard REST
   API (http://localhost:8080/api/), and return the following information:
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

### Post-Mortem

After you've finished with development, we ask that you write up a
**post-mortem** with the following questions as a starting point:

1. What design choices did you make, and why? Include approaches that did and
   did not work.
1. What did you find challenging?
1. What interesting decisions did you make along the way?
1. Any other feedback you want to include

### Submission

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

## Overview

The following sections detail how to run the application and start developing.

If you’re unfamiliar with the structure of a Django application, check out the
Django resources linked in the Appendix.

> Note: The message board application lives in `src/messageboard`.

### Requirements

* [Python >= 3.6](https://www.python.org/downloads/)
* [Poetry](https://github.com/python-poetry/poetry)

It's recommended that you use the `make` commands provided in the Makefile. See
the Appendix for an explanation of what these commands do.

Additional packages can be installed using `poetry add <package-name>`.

> Note: Feel free to install any additional packages or tools to support your
> efforts!

### Getting Started

If you have any of the following environment variables set, you should unset them:
* `DJANGO_SETTINGS_MODULE`

1. To initialize the application, run `make build`. This command creates a
   virtual environment using `pipenv` and installs the required Python packages.
   It also runs database migrations and seeds your database with fixtures (i.e.
   randomly-generated data).
2. To start the application, run `make run`. This command starts the Django
   server on http://localhost:8080.
3. In a separate terminal, you can run automated tests using `make tests`.
4. To run the `stats.py` script, run `make stats`.
5. For everything else, check out the table below.

## Appendix

### Make Commands

We have provided a number of helpful commands via a Makefile to assist your
development experience.

| Command       | Description                                                                                         |
|---------------|-----------------------------------------------------------------------------------------------------|
| `make build`  | Installs required packages to the virtual environment, managed by `pipenv`, and seeds your database |
| `make run`    | Runs the Django server at `http://localhost:8080`                                                   |
| `make stats`  | Runs the `stats.py` script                                                                          |
| `make shell`  | Opens an interactive terminal                                                                       |
| `make test`   | Runs unit tests                                                                                     |
| `make format` | Formats the `src` folder using `black`                                                              |
| `make wipe`   | Deletes and re-seeds the database                                                                   |

### Resources

* [Django Quick Start](https://docs.djangoproject.com/en/2.2/intro/overview/)
* [DjangoGirls Tutorial](https://tutorial.djangogirls.org/en/)

### FAQ

#### 1. I don't have time to work on this, but I still want to apply to CloudBolt. What do I do?

If you have another project that you think would better exemplify your skills,
we'd love to see that instead! Regardless of the project, we will use the
[Evaluation Criteria](#evaluation-criteria).

If this is the case, please reach out to your hiring contact.

#### 2. I have other questions!

Please reach out to your hiring contact.
