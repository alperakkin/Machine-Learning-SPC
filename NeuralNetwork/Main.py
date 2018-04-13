from NeuralNetwork import NeuralNetworks as NN
from csv_data_reader import CSVObject as csv_o

batch=10000



data=csv_o(2,1)
inputs=[0 for i in range(data.arr_length())]
targets=[0]




nn= NN(2,20,1)


for i in range(batch):
 train_data= data.result()
 nn.train(train_data[0], train_data[1])
 #print(train_data)
 if(i%5==0):
  print("İşleniyor: ", round((i/batch)*100),"%")




nn.Predict([0,1])














