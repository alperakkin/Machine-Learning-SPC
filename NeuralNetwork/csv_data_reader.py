import csv
import random

class CSVObject:

    def __init__(self, inputs, targets):
        self.inputs = inputs
        self.targets = targets

    def result(self):

        it = 0
        tt = 0
        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            len_satir = sum(1 for line in reader)
        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for satir, sutun in enumerate(reader):
                len_sutun = len(sutun)

        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for satir, sutun in enumerate(reader):
                if (satir == 0):
                    for arr in range(len_sutun):
                        if (sutun[arr] == "Input"):
                            it += 1
                        if(sutun[arr]=="Target"):
                            tt+=1

            with open('data.csv', 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                len_satir = sum(1 for line in reader)
            with open('data.csv', 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for satir, sutun in enumerate(reader):
                    len_sutun = len(sutun)

            inputs_array = [0 for i in range(it)]
            targets_array=[0 for i in range(tt)]
            satir_oku =random.randint(1,4)

            with open('data.csv', 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')

                for satir, sutun in enumerate(reader):
                    if (satir == satir_oku):

                        for arr in range(it):
                            inputs_array[arr] =float(sutun[arr])

                        for arr in range(tt):
                            targets_array[arr]=float(sutun[arr+it])

                return inputs_array,targets_array,it,tt



    def arr_length(self):
        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for satir, sutun in enumerate(reader):
                len_sutun = len(sutun)
        return len_sutun-1
















