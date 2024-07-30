# Simple Perceptron implementation in Python

## Getting started

* Dependencies
    * Python 3.10 or higher
    * poetry

* Usage
    * Clone the repository
    * Run `poetry install` to install the dependencies
    * Run `poetry run jupyter notebook` to run the jupyter notebooks

##### About the files

* `perceptron.py` : Simple small implementation of the algorithm.
* `notebooks/perceptron_2d.ipynb` : A simple perceptron with 2 inputs trained on an 8x8 card - learns a linear boundary
  in each card.
* `notebooks/perceptron_64.ipynb` : A simple perceptron with 64 inputs trained on an 8x8 card. Learns to predict whether
  the cards have vertical or horizontal boundaries.

## Overview

This is a Python implementation of the [Perceptron Algorithm](https://en.wikipedia.org/wiki/Perceptron).
A perceptron is a single neuron model that is used to classify input data into two classes.
It is the simplest form of an artificial neural network, originally proposed
by [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt) in
his seminal
paper ["The perceptron: a probabilistic model for information storage and organization in the brain." Rosenblatt F.(1958)](https://www.ling.upenn.edu/courses/cogs501/Rosenblatt1958.pdf)

## Pereceptron Algorithm

![Basic Percepton](./static/perceptron.svg "Basic function of a perceptron")
Fig: 01

Apply a set of weights to the input features and sum them up. If the sum is greater than a threshold, the perceptron
fires and outputs a 1, otherwise it outputs a -1.

## Pereceptron Algorithm Learning

Update the weights based on the error in the prediction. The weights are updated by adding the product of the error and
the input to the current weight.

$$
\text{if } y*a \leq 0 \text{ then }
\bigg|\begin{multline}
\begin{aligned}
w_i &= w_i + y x_i \text{ for i = 1,2,3,..,n} \\
b &= b + y
\end{aligned}
\end{multline}
$$

The key is that if there are no errors, the weights are not updated.
If there are errors, the weights are updated in the direction that reduces the error.

## Perceptron Convergence

However, as long as the data is linearly separable, the perceptron algorithm
is [guaranteed to converge to a solution.](https://www.cs.cornell.edu/courses/cs4780/2018fa/lectures/lecturenote03.html#:~:text=The%20Perceptron%20was%20arguably%20the,%2C%20it%20will%20loop%20forever.)
But, a major limitation of the perceptron is that it can <mark>only learn linearly separable functions.</mark>,
and non-linear functions are common and trivial to find.

e.g. [Minsky and Papert](https://books.google.com/books/about/Perceptrons_Reissue_of_the_1988_Expanded.html?id=PLQ5DwAAQBAJ)
showed that perceptrons could not learn simple functions like the XOR function

<img src="static/nonseparable.png" title="Non Linlearly seprable functions" width=200>

Furthermore, if the perceptron has N inputs, the decision boundary is an N-1 dimensional hyperplane. E.g. in a
2D space, the decision boundary is a line, in a 3D space, the decision boundary is a plane, and so on.

## History of the Perceptron

There are
many [inventions that have shaped the field of artificial intelligence](https://www.mckinsey.com/featured-insights/artificial-intelligence/deep-learnings-origins-and-pioneers),
but one of the most important is the perceptron. The perceptron was invented in 1957 by Frank Rosenblatt, a psychologist
at the Cornell Aeronautical
Laboratory. The perceptron was the first neural network, and it was the first time that a computer could learn from its
own mistakes.

![An image of the perceptron](./static/perceptron_diagram.png "An image of the perceptron from Rosenblatt's “The Design of an Intelligent Automaton,” Summer 1958.")

An image of the perceptron from Rosenblatt's “The Design of an Intelligent Automaton,” Summer 1958."

## Critcisms and Limitations

For most of the 1960s, the perceptron was seen as a major breakthrough in
artificial intelligence. However, in 1969, [Marvin Minsky](https://en.wikipedia.org/wiki/Marvin_Minsky)
(who was one year his junior at
[Bronx Science](https://en.wikipedia.org/wiki/Bronx_High_School_of_Science)
)
and [Seymour Papert](https://en.wikipedia.org/wiki/Seymour_Papert)
published a book called ["Perceptrons"](https://en.wikipedia.org/wiki/Perceptrons_(book))
, which showed that the perceptron had
severe limitations. They showed that the perceptron could not learn simple
functions like the XOR function, which is a basic logical operation. This
result led to a decline in interest in neural networks, and the perceptron
was largely abandoned.

## Perceptron Evolution

However, in the 1980s, researchers discovered that by stacking multiple
perceptrons together, they could create a more powerful neural network
called a [multilayer perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron), a precursor
to the more complex neural networks that are used today.

Although Rosenblatt was not able to see the full potential of the perceptron, and
died in a boating accident in 1971, his belief in the potential of neural networks has been vindicated.

## References

1. Hal Daumé III, "A Course in Machine Learning" [PDF](http://ciml.info/dl/v0_99/ciml-v0_99-ch04.pdf)
2. Deep Learning's Origins and Pioneers,
   McKinsey [Link](https://www.mckinsey.com/featured-insights/artificial-intelligence/deep-learnings-origins-and-pioneers)
3. Professors: Perceptron paved the way for AI, 60 years too soon, Cornell
   University [Link](https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon)
4. The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain, Frank
   Rosenblatt [PDF](https://www.ling.upenn.edu/courses/cogs501/Rosenblatt1958.pdf)
5. Perceptrons Minsky, Marvin; Papert,
   Seymour [Link](https://books.google.com/books/about/Perceptrons_Reissue_of_the_1988_Expanded.html?id=PLQ5DwAAQBAJ)

## Resources

#### Training results for 2 input perceptron

```mermaid
xychart-beta
    title "Perceptron Error Rate"
    x-axis "Number of cards" [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    y-axis "Prediction Error" 0 --> 1    
    bar [1, 0.234375, 0.0625, 0.0, 0.25, 0.328125, 0.625, 0.0, 0.125, 0.25, 0.5, 0.25, 0.625, 0.0, 0.375, 0.25, 0.125, 0.125, 0.0, 0.625, 0.75, 0.625, 0.25, 0.125, 0.375, 0.125, 0.625, 0.125, 0.25, 0.0, 0.375, 0.0, 0.125, 0.25, 0.25, 0.25, 0.0, 0.125, 0.125, 0.5, 0.25, 0.125, 0.125, 0.625, 0.625, 0.5, 0.5, 0.0, 0.0, 0.375, 0.125, 0.0, 0.375, 0.0, 0.75, 0.75, 0.625, 0.125, 0.5, 0.25, 0.375, 0.625, 0.0, 0.5, 0.125, 0.125, 0.5, 0.0, 0.375, 0.125, 0.625, 0.5, 0.25, 0.125, 0.375, 0.125, 0.125, 0.125, 0.125, 0.125, 0.0, 0.125, 0.25, 0.25, 0.375, 0.25, 0.0, 0.25, 0.0, 0.0, 0.125, 0.375, 0.125, 0.125, 0.5, 0.625, 0.5, 0.125, 0.375, 0.125]
    line "Prediction Error running avereg" [1, 0.6171875, 0.4322916666666667, 0.32421875, 0.309375, 0.3125, 0.35714285714285715, 0.3125, 0.2916666666666667, 0.2875, 0.3068181818181818, 0.3020833333333333, 0.3269230769230769, 0.30357142857142855, 0.30833333333333335, 0.3046875, 0.29411764705882354, 0.2847222222222222, 0.26973684210526316, 0.2875, 0.30952380952380953, 0.32386363636363635, 0.32065217391304346, 0.3125, 0.315, 0.3076923076923077, 0.3194444444444444, 0.3125, 0.3103448275862069, 0.3, 0.3024193548387097, 0.29296875, 0.2878787878787879, 0.2867647058823529, 0.2857142857142857, 0.2847222222222222, 0.27702702702702703, 0.2730263157894737, 0.2692307692307692, 0.275, 0.27439024390243905, 0.2708333333333333, 0.26744186046511625, 0.27556818181818177, 0.28333333333333327, 0.2880434782608695, 0.29255319148936165, 0.2864583333333333, 0.28061224489795916, 0.2825, 0.2794117647058823, 0.2740384615384615, 0.27594339622641506, 0.2708333333333333, 0.2795454545454545, 0.2879464285714285, 0.29385964912280693, 0.2909482758620689, 0.29449152542372875, 0.29374999999999996, 0.2950819672131147, 0.30040322580645157, 0.2956349206349206, 0.29882812499999994, 0.2961538461538461, 0.293560606060606, 0.29664179104477606, 0.29227941176470584, 0.2934782608695652, 0.29107142857142854, 0.2957746478873239, 0.29861111111111105, 0.297945205479452, 0.29560810810810806, 0.29666666666666663, 0.29440789473684204, 0.29220779220779214, 0.2900641025641025, 0.2879746835443037, 0.2859374999999999, 0.28240740740740733, 0.2804878048780487, 0.2801204819277108, 0.27976190476190466, 0.28088235294117636, 0.2805232558139534, 0.27729885057471254, 0.27698863636363624, 0.2738764044943819, 0.2708333333333332, 0.2692307692307691, 0.2703804347826086, 0.26881720430107514, 0.26728723404255306, 0.269736842105263, 0.27343749999999983, 0.2757731958762885, 0.2742346938775509, 0.27525252525252514, 0.2737499999999999]
```

#### Training results for 64 input perceptron

```mermaid
xychart-beta
    title "Perceptron Error Rate"
    x-axis "Number of Decks" [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    y-axis "Prediction Error" 0 --> 1    
    bar [1, 0.3333333333333333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3333333333333333, 0.3333333333333333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    line "Prediction Error running avereg" [1, 0.6666666666666666, 0.4444444444444444, 0.3333333333333333, 0.26666666666666666, 0.2222222222222222, 0.19047619047619047, 0.16666666666666666, 0.18518518518518517, 0.19999999999999998, 0.1818181818181818, 0.16666666666666666, 0.15384615384615385, 0.14285714285714285, 0.13333333333333333, 0.125, 0.11764705882352941, 0.1111111111111111, 0.10526315789473684, 0.1]
   
```
#### Mermaid flowchart for Fig 01

``` 
   flowchart LR
    subgraph Inputs["Inputs"]
        A1["$$ x_1$$"]
        A2["$$ x_2$$"]
        ADOT[".."]
        AN["$$ x_n$$"]
    end
    subgraph subGraph1["Weights"]
        w1(("$$ w_1 $$"))
        w2(("$$ w_2 $$"))
        wDOT[".."]
        wN(("$$ w_n $$"))
    end
    C{"$$ z = \sum_{i=1}^n x_i w_i + b $$"}
    step["$$ output = \begin{cases}1 & \text{if }\ z > T \text{,\ where T is some threshold},\\-1 & \text{otherwise}\end{cases} $$"]
    output["$$y$$"]
    %% Comments after double percent signs

    A1 --> w1 
    w1--> C
    A2 --> w2
    w2 --> C
    ADOT --> wDOT
    wDOT --> C
    AN --> wN
    wN --> C
    C --> step
    step --> output
    style C stroke-width:2px
```
