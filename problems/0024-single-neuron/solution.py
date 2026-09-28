import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	f = np.array([np.array(i) for i in features])
	w = np.array([np.array(i) for i in weights])
	labels = np.array(labels)

	
	probabilities = [0]
	mse = 1
	x  = f @ w + bias
	probabilities = (1/(1+np.exp(-x))).tolist()
	probabilities = [round (i,4) for i in probabilities]
	mse = round(np.mean((probabilities - labels)**2),4)
	

	return probabilities, mse