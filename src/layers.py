inputs = [1, 2, 3, 4]
weights = [[0.8, 0.5, -0.1, 0.2], [0.6, 0.7, -0.1, -0.4], [0.9, 0.2, 0.2, -0.6]]# ,[-0.8, 0.5, 0.1, 0.2] 
biases = [2, -1, 3, 0]

# Output of current layer
layer_outputs = []
# For each neuron
for neuron_weights, neuron_bias in zip (weights, biases):
  # Zeroed output of given neuron
  neuron_output = 0
  # For each input and weight to the neuron
  for n_input, weight in zip (inputs, neuron_weights):
    # Multiply this input by associated weight
    # and add to the neuron’s output variable
    neuron_output += n_input * weight
    # Add bias
  neuron_output += neuron_bias
  # Put neuron’s result to the layer’s output list
  layer_outputs.append(neuron_output)
print (layer_outputs)

# DOT PRODUCT
# in vectors(SAME LENGTH - 1D ARRAYS) returns a single number, the sum of products of consecutive vector elements

# vector addition
# returs a vector where each element is the sum of the elements at the same position in the input vectors(SAME LENGTH - 1D ARRAYS)

import numpy as np
# order of arguments is important!
layer_outputs = np.dot(weights, inputs) + biases
print(layer_outputs)

print("--- IGNORE ---")
a = np.dot(weights, inputs) # (3,4) . (4,) = (3,)
b = np.dot(inputs, weights) # (4,) . (3,4) = ERROR
print(a, b)

# a = [
#     [3, 4, 5],
#     [6, 7, 8]
# ]
# b = [1,2,3]

# print(np.dot(a,b),np.dot(b,a)) RETURNS ERROR


A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]
print(np.dot(A, B))