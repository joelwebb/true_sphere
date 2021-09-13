from numpy import asarray
from numpy import arange
from numpy.random import rand
import math
import numpy as np
import argparse


def vector_arc_distance(v_1, v_2):
    """using two vectors with a length of 3, get the arc distances
    based on https://stackoverflow.com/questions/52210911/great-circle-distance-between-two-p-x-y-z-points-on-a-unit-sphere
    alternative https://github.com/spacetelescope/spherical_geometry

    """
    delta = math.sqrt(
        (v_2[0] - v_1[0]) ** 2 + (v_2[1] - v_1[1]) ** 2 + (v_2[2] - v_1[2]) ** 2
    )
    return 2 * 1 * delta / 2 / 1  # assuming unit circle so R = 1


def midpoint(p1, p2):
    """calculates the midpoint between two points which might be the
    output without gradient descent to base off of
    """
    return np.array([(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2, (p1[2] + p2[2]) / 2])


def objective_function(x):
    """objective function to optimize for gradient descent
    Needs edited to follow how we would optimize the loss between the
    midpoint and our randomly selected point.
    """
    return x * 1  # change this to our actual function


def derivitive(x):
    """No way to calculate this without assistance to derive sum of arc distances.
    googling suggests the derivitive of a sum is the sum of a derivitive - look into this."""
    return x * 1


def mse(A, B):
    """since we can't use other extenal packages for calculations and only numpy,
    calculate the mean square error by hand - might be able to be used in loss/error
    """
    return ((A - B) ** 2).mean(axis=0)


def gradient_descent(objective_function, derivative, boundaries, iterations, step_size):
    """perform simple gradient descent with numpy manually
    Alternative packages with built in SGD, etc include
    https://pytorch.org/docs/stable/autograd.html
    """
    # create lists to track all outputs
    outputs = list()
    scores = list()
    # get a random point within the boundaries
    output = boundaries[:, 0] + rand(len(boundaries)) * (
        boundaries[:, 1] - boundaries[:, 0]
    )
    # for each iteration in the iter object
    for i in range(iterations):
        # calculate gradient
        gradient = derivitive(output)  # Code breaks here -
        # take a step
        output = output - step_size * gradient
        # evaluate candidate point
        output_eval = objective_function(output)
        # store output
        outputs.append(output)
        scores.append(output_eval)
        # report progress
        print(output, output_eval)
    return [outputs, scores]


if __name__ == "__main__":

    # get randomly chosen locations on the sphere
    input_1 = np.array([1, 1, 1])
    input_2 = np.array([0, 0, 0])
    # set the n dimensional boundary of the sphere between -1, 1 for each coordinate
    boundaries = asarray([[-1.0, 1.0], [-1, 1], [-1, 1]])
    # get a random point vector within the boundaries
    rand_starting_vector = boundaries[:, 0] + rand(len(boundaries)) * (
        boundaries[:, 1] - boundaries[:, 0]
    )
    # define the total iterations
    iterations = 30
    # define the step size
    step_size = 0.1
    # define the learning rate
    # learning_rate = None TODO - add this in manually
    # perform the gradient descent search
    outputs, scores = gradient_descent(
        objective_function, derivitive, boundaries, iterations, step_size
    )
    # compute target scores for our inputs
    results_1 = objective_function(input_1)
    results_2 = objective_function(input_2)
    # check the results vs the outputs
    print(results_1)
    print(outputs)
