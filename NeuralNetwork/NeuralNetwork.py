from Matrix import MatrixObject as MO
import math



def Sigmoid(x):

    return 1/(1+math.exp(-x))


def DSigmoid(y):
    return y*(1-y)

def alreadySigmoided(x):
    return x*(1-x)



class NeuralNetworks:

    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes= hidden_nodes
        self.output_nodes= output_nodes


        self.weights_ih= MO(self.hidden_nodes,self.input_nodes)
        self.weights_ho= MO(self.output_nodes,self.hidden_nodes)

        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h= MO(self.hidden_nodes,1)
        self.bias_o= MO(self.output_nodes,1)

        self.bias_h.randomize()
        self.bias_o.randomize()

        self.learning_rate=0.1




    def Predict(self,input_array):


       # Generating Hidden Output!!
        inputs= MO.fromArray(input_array)
        hidden= MO.hadamart(self.weights_ih,inputs)
        hidden.add(self.bias_h)

        # activation function

        hidden= MO.map(hidden,Sigmoid)

      # Generating the outputs output

        outputs = MO.hadamart(self.weights_ho,hidden)
        outputs.add(self.bias_o)
        outputs=MO.map(outputs,Sigmoid)


       # Sending back to the caller
        print("Tahmin",outputs.toArray())
        return outputs.toArray()



    def train(self,inputs_array,targets_array):

       # Generating the hidden outputs

         inputs=  MO.fromArray(inputs_array)
         hidden = MO.hadamart(self.weights_ih,inputs)
         hidden.add(self.bias_h)





    # activation function

         hidden= MO.map(hidden,Sigmoid)

       # Generating the outputs output

         outputs= MO.hadamart(self.weights_ho,hidden)
         outputs.add(self.bias_o)
         outputs= MO.map(outputs,Sigmoid)


        # Convert arrays to matrix object

         targets = MO.fromArray(targets_array)

         #lr = 0.1

        # Calculate the error

         output_errors = MO.subtract(targets, outputs)




         gradients = MO.map(outputs,DSigmoid)


         gradients=MO.multiply(gradients,output_errors)





         gradients = MO.hadamart(gradients,self.learning_rate)



         hidden_T= MO.transpose(hidden)




         weights_ho_deltas=MO.hadamart(gradients,hidden_T)


         self.weights_ho.add(weights_ho_deltas)
         self.bias_o.add(gradients)


         who_t=MO.transpose(self.weights_ho)
         hidden_errors=MO.hadamart(who_t,output_errors)

         hidden_gradient=MO.map(hidden,DSigmoid)


         hidden_gradient=MO.multiply(hidden_gradient,hidden_errors)


         hidden_gradient=MO.hadamart(hidden_gradient,self.learning_rate)

         inputs_T=MO.transpose(inputs)

         weight_ih_deltas=MO.hadamart(hidden_gradient,inputs_T)


         self.weights_ih.add(weight_ih_deltas)
         self.bias_h.add(hidden_gradient)




















