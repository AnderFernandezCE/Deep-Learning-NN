inputs = [1, 2, 3, 4]
weights = [[0.8, 0.5, -0.1, 0.2], [0.6, 0.7, -0.1, -0.4], [0.9, 0.2, 0.2, -0.6]]# ,[-0.8, 0.5, 0.1, 0.2] 
biases = [2, -1, 3]

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


print("---- Row vector ----")
row1 = np.array([[1,2,3]])
list1 = [4,5,6]
row2= np.array([list1])
row3 = np.expand_dims(np.array(list1), axis=0)

print("---- Column vector ----")
# Transpose of a row vector
col1 = np.array([[1],[2],[3]]).T


print("---- Batch of inputs ----")
# HERE THE DOT PRODUCT ORDER IS IMPORTANT, FIRST INPUT THEN WEIGHTS TRANSPOSED(WE WANT SAMPLE RESULTS)
batch_inputs = np.array([[1,2,3,4],
                         [5,6,7,8],
                         [9,10,11,12]])
batch_outputs = np.dot(batch_inputs, np.array(weights).T) + biases
print(batch_outputs)