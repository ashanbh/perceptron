import numpy as np
import copy

def predict_only(X, Y, w, b, debug_function=None, summarize=True):
    # how untrained am I?
    prediction_errors = 0
    for i, x in enumerate(X):
        a = np.dot(x, w) + b
        y = Y[i]
        # Count errors
        if (a * y) <= 0:
            prediction_errors += 1
        if debug_function:
            debug_function(x,y,a)
    if summarize:
        print(f"Prediction Errors:{prediction_errors}")
    return prediction_errors

#basic perceptron algorithm
def perceptron(X, Y, w, b, epochs=20, predict=False, debug_function=None):
    # how untrained am I?
    if predict:
        predict_only(X, Y, w, b, debug_function)

    # start Training
    for t in range(epochs):
        w_old = copy.deepcopy(w)

        for i, x in enumerate(X):
            a = np.dot(X[i], w) + b

            y = Y[i]
            if (a * y) <= 0:
                w = w + X[i] * y
                # print(f"Weights updated -> (x={x}, y={y}, a={a}) => w:{w_old}->{w}, b:{b}->{b+y}")
                b = b + y
            else:
                # print(f"Prediction correct  -> (x={x}, y={y}, a={a})")
                pass

        if (np.array_equal(w_old, w)):
            #converged in the `t+1`st epoch
            return (w, b, t+1)
            break

    return (w, b, 0)