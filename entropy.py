import numpy as np
import matplotlib.pyplot as plt

# This code introduces us to the concept of entropy. We take a discrete random process
# (a series of random variables) with a uniform distribution function giving
# values between 0 and N-1. At each point in time, we calculate the histogram of
# values up to this point which is an approximation of the probability distribution
# function of the random process. The entropy is calculated at each time point by
# entropy = -sum(p*log2(p)). Since the early time distribution has very few occurences
# the entropy starts low, and with time increases to its maximal value.

T = 10000 # number of random samples (also length of "time" vector)
N = 64 # outcome space (what values the random variable can take)
samples = np.random.randint(low=0, high=N, size=T) # vector of uniform distributed samples

occurences = np.zeros((T,N)) # the number of occurences of an integer up to a certain time
probability = np.zeros((T,N))
entropy = np.zeros(T)
for t in range(T):
    occurences[t,:] = np.bincount(samples[:t+1], minlength=N)
    probability[t,:] = occurences[t,:]/np.sum(occurences[t,:])
    entropy[t] = np.sum([-p*(np.log2(p)) for p in probability[t,:] if p!=0])

fig = plt.figure(figsize=(10,8))

# plot the evolving histogram
plt.subplot(221)
plt.pcolor(np.log(probability))
plt.gca().set_xlabel('Occurences (histogram)')
plt.gca().set_ylabel('Time')

# plot the samples vector vs. time
plt.subplot(222)
plt.scatter(np.arange(T), samples, s=1, alpha=0.5)
plt.gca().set_xlabel('Time')
plt.gca().set_ylabel('Random process output')

# plot the entropy vs. time
plt.subplot(223)
plt.plot(np.arange(T), entropy)
plt.gca().set_xlabel('Time')
plt.gca().set_ylabel('Entropy')
plt.gca().set_xscale('log')

plt.tight_layout()