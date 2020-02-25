from time import * #I'm just playing around with different python libaries; this technically isn't really needed
"""This is the class where all the mathematical calculations are happening and takes in a mode input where a user can select the
matrix calculation mode they desire(addition, subtraction, multiplication). It also contains all the framework for the calculations
to happen
"""
class matrixcalculator:
    def __init__(self,modeselect,matrixinput):
        inputcheck = False
        while inputcheck == False:
            self.modeselect = input("Please input the calculator mode you wish for; \"A\" for addition, \"B\" for subtraction and \"C\" for multiplication")
            if self.modeselect == "A" or self.modeselect == "B" or self.modeselect == "C":
                inputcheck = True
            else:
                print("Please make sure you entered the correct input!")
                
    def addition(self,matrix1,matrix2): #this contains the basis for matrix addition. It functions by taking the two matrices and adding the matrix entries at their respective positions to a final list
                
        returnlist = []
        for s in range(len(matrix1[0])):
            var = []
            for p in range(len(matrix1[0])):
                var.append(int(matrix1[s][p])+int(matrix2[s][p]))
            returnlist.append(var)
        return returnlist
    
    def subtraction(self, matrix1,matrix2): #This also follows a similar process to the addition
        returnlist = []
        for inputs in range(len(matrix1[0])):
            somelist=[]
            for o in range(len(matrix1[0])):
                somelist.append(int(matrix[inputs][o])-int(matrix2[inputs][o]))
            returnlist.append(somelist)
        return returnlist
    
    def multiplication(self, matrix1,matrix2): #For this multiplication method, I first created a modified list for matrix 2 since the columns are the ones that are being multiplied and for it to fit comfortably into the for loop especially when matrices of different sizes are being multiplied
        returnlist = []
        augmentedmatrix = []
        for i in range(len(matrix2[-1])):
            stick = []
            for s in range(len(matrix1[-1])):
                stick.append(matrix2[s][i])
            augmentedmatrix.append(stick)
            
        for r in range(len(matrix1)):
            returnthing = []
            for i in range(len(matrix1)):
                sum = 0
                for j in range(len(matrix1[0])):
                    sum += (int(matrix1[r][j])* int(augmentedmatrix[i][j]))
                    if ij == len(augmentedmatrix[0])-1:
                        returnthing.append(sum)
            returnlist.append(returnthing)
        return returnlist

s = matrixcalculator("placeholder","placeholder") #this is just creating an object of the class with two placeholders so that it can be called with ease
#The main function is where the processing and printing magic happens
def main():
    dimensions = input("What are the dimensions of your two matrices? Format as \"x,y:x,y\"(x is row dimension and y is column dimension)MAKE SURE THAT THE TWO MATRICES ARE IN ORDER OF OPERATION!")
    #This is where the user will input the dimensions needed
    try: #The data here is being formatted properly into a list so that it can be accessed with ease when needed
        determine= dimensions.split(":")
        bigsplit = []
        for kl in determine:
            bigsplit.append(kl.split(","))
    except:
        return "That is not the correct format, please check!"
    
    if (bigsplit[0][0] != bigsplit[1][0] or bigsplit[0][-1] != bigsplit[1][-1]) and (s.modeselect == "A" or s.modeselect == "B"):
        return "that operation is not possible!"
    elif bigsplit[0][-1] != bigsplit[1][0] and s.modeselect == "C":
        return "that operation is not possible!"
    #This checks the conditions to make sure the sizes of the matrices are successful; for addition and subtraction, they must be the same sized matrix and for multiplication, they must be compatible so that [n x m] x [m x w] (let n, m, w be any arbitrary natural number)
    matrix1 = []
    matrix2 = []
    for r in range(1,int(bigsplit[0][0])+1):
        insertion = []
        for c in range(1,int(bigsplit[0][-1])+1):
            insertion.append(input("type in the value for the " + str(r) + " , "+ str(c) +" dimension(first matrix)"))
        matrix1.append(insertion)
    #This loop takes in the first matrix values with the user friendly interface that specifies the position that it requires
    for op in range(1,int(bigsplit[1][0])+1):
        insertion2 = []
        for thing in range(1,int(bigsplit[1][-1])+1):
            insertion2.append(input("type in the value for the " + str(op) + ","+ str(thing) +" dimension(second matrix)"))
        matrix2.append(insertion2)
    #This loop also does the identical process for matrix 2
    twomatrices = [matrix1,matrix2]
    #With the info, it looks at the user input and sends the data to the class to be processed and returns some final matrix that has its values calculated
    if s.modeselect == "A":
        finalcombo = s.addition(matrix1, matrix2)
    elif s.modeselect == "B":
        finalcombo = s.subtraction(matrix1,matrix2)
    elif s.modeselect == "C":
        finalcombo = s.multiplication(matrix1,matrix2)
    #This simply prints the final matrix in a format that is visually understandable to the user
    for n in finalcombo:
        if n == finalcombo[0]:
            print("Your final matrix is: " + "\n")
            print(str(n) + "\n")
        else:
            print(str(n) + "\n")
    #I just felt like it why not :)
    print("The current date and time is: " + strftime("%A %d %b %Y %H:%M:%S",localtime()))
main()