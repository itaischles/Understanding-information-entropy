# Understanding-information-entropy
This code introduces us to the concept of information entropy. We take a discrete random process (a series of random variables) with a uniform distribution function giving values between 0 and N-1. At each point in time, we calculate the histogram of values up to this point which is an approximation of the probability distribution function of the random process. The entropy is calculated at each time point by entropy = -sum(p*log2(p)). Since the early time distribution has very few occurences the entropy starts low, and with time increases to its maximal value.
