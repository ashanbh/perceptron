#basic perceptron algorithm
def perceptron(X, Y, w, b, epochs=20, predict=False):
    # how untrained am I?
    if predict:
        prediction_errors = 0
        for i, x in enumerate(X):
            a = np.dot(x, w) + b
            y = Y[i]
            print(
                f"Prediction: {'Horizontal' if a > 0 else 'Vertical'} ({a}) GT:{'Horizontal' if y > 0 else 'Vertical'}({y})")

            # Count errors
            if (a * y) <= 0:
                print("Mismatch")
                prediction_errors += 1

            # show card
            draw_card(x)
        print(f"Prediction Errors:{prediction_errors}")

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
            print(f"CONVERGENCE (epoch:{t})")
            break

    return (w, b)