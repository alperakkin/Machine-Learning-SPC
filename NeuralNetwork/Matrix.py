import random

class MatrixObject:
    data = []

    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.data=[[0 for x in range(self.cols)] for y in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j]=0


    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] =random.random()


    def add(self,n):
        if  isinstance(n,MatrixObject):


            if(self.rows!=n.rows and self.cols!=n.cols):
                print("Hata:İki matrisin boyutları eş değil!")


            else:
                for i in range(self.rows):
                    for j in range(self.cols):
                        self.data[i][j] += n.data[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n


    @staticmethod
    def transpose(mtrx):

            result = MatrixObject(mtrx.cols,mtrx.rows)
            for i in range(mtrx.rows):
                  for j in range(mtrx.cols):
                    result.data[j][i] += mtrx.data[i][j]
            return result





    @staticmethod
    def map(matrix,func):
        result=MatrixObject(matrix.rows,matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                val=matrix.data[i][j]
                result.data[i][j]=func(val)
        return result


    @staticmethod
    def fromArray(arr):
        m= MatrixObject(len(arr),1)
        for i in range(len(arr)):
            m.data[i][0]=arr[i]
        return m


    def toArray(self):
        arr=[]
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.data[i][j])
        return arr

    @staticmethod
    def subtract(a,b):
        result=MatrixObject(a.rows,a.cols)

        for i in range(result.rows):
            for j in range(result.cols):
                result.data[i][j]=a.data[i][j]-b.data[i][j]
        return result






    @staticmethod
    def hadamart(a,b):

        if not isinstance(b, MatrixObject):
           result=MatrixObject(a.rows,a.cols)
           for i in range(a.rows):
                for j in range(a.cols):
                    result.data[i][j] =a.data[i][j]* b
           return result
        else:

            if(a.cols!=b.rows): print("A sütunları ile B satırları uyumsuz!")
            else:
                result=MatrixObject(a.rows,b.cols)
            for i in range(result.rows):
                for j in range(result.cols):
                    sum=0
                    for k in range(a.cols):
                        sum+=a.data[i][k]*b.data[k][j]
                        result.data[i][j]=sum

        return result


    def multiply(a,b):
        result = MatrixObject(a.rows, a.cols)
        if isinstance(b,MatrixObject):
           if isinstance(a,MatrixObject):
              for i in range(a.rows):
                  for j in range(a.cols):
                       result.data[i][j]= a.data[i][j] * b.data[i][j]
        return result








    def print_matrix(self):

      for x in range(self.cols): print("_________________________", end="")
      print()
      for x in range(self.cols): print("              ", x, end="       ")
      print()

      for i in range(self.rows):
          print()
          print("________________________________________________")
          print(i, "|",end="")




          for j in range(self.cols):

             print("  ",self.data[i][j]," ", end="")
             if(len(str(self.data[i][j]))==15): print(" ", end="")


      print()
      for x in range(self.cols): print("_________________________", end="")
      print()


