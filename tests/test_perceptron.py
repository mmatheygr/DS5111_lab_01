import sys
sys.path.append(".")

from bin.perceptron import Perceptron

def test_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict_function([1,1]) ==  1, "1-1 failed"
    assert the_perceptron.predict_function([1,0]) ==  1, "1-0 failed"
    assert the_perceptron.predict_function([0,1]) ==  1, "0-1 failed"
    assert the_perceptron.predict_function([0,0]) ==  0, "0-0 failed"
