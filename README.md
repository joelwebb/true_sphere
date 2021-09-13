# True Sphere Challenge
 Sphere based batch gradient descent for the true challenge

# Task
 1) Write a batch gradient descent routine to find the point on the unit sphere (size 1) (in any number of dimensions) which minimizes the sum of arc length distances to each of a set of given points also on the sphere.


## Setup

Requires at least Python 3, tested with 3.6.9

Relies on numpy - so make sure this is up to date. 

After cloing the repository, open a terminal inside the repository directory.

Create a virtual environment if necessary with venv:

```shell
python3 -m pip install virtualenv
python3 -m venv env
source env/bin/activate
```

Then to install the necessary packages install the requirements.txt file:

```shell
$ pip install -r requirements.txt
```

## Running the gradient descent 

To run one locally, try:
```shell
$ python3 gradient_testing.py 
```
There are print statements in the __main__ section to compare functionality. 

## Linting & Code Formatting
Code is formatted using black and can be linted with pylint. Unit tests can be completed with pytest. Due to the short nature of this, no tests are provided.

## Running in Docker

A dockerfile is included to create a containerised application of the python code - build and run from the repository directory with:

```
$ git clone https://github.com/joelwebb/true_sphere.git
$ cd true_sphere
$ sudo docker build -t true_sphere:latest .
$ sudo docker run true_sphere
```

**Note** 
On my windows machine building the image put the image in a different location: docker.io/library/true_sphere:latest

So make sure you call the run command on the right image location or it wont work.



## Limitations

- For the gradient descent, this is using numpy instead of torch autograd. Should be upgraded to torch for production testing. 

#TODO
 - add in learning rate
 - finalize how you can calculate the derivitive of the optimization function for the gradient --- need to work with someone who has more calc 3 experience than I do
 - compare to pytorch

