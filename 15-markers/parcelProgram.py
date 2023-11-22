minWeight = 1
maxWeight = 10
maxDimension = 80
sumDimensions = 200
accepted = True

def getWeight():
    global weight
    weight = int(input("Enter the weight of the parcel: "))

def getDimensions():
    global height, length, breadth
    height = int(input("Enter the height of the parcel: "))
    length = int(input("Enter the length of the parcel: "))
    breadth = int(input("Enter the breadth of the parcel: "))

def calculateParcel(w, h, l, b):
    global accepted
    if (w >= minWeight and w <= maxWeight) and (h + l + b <= sumDimensions) and (h <= maxDimension) and (l <= maxDimension) and (b <= maxDimension):
        accepted = True
    else: 
        if (w > 10):
            print("The parcel's weight exceeds " + str(maxWeight) + " kg.")
            accepted = False
        if (w < 1):
            print("The parcel's weight is less than " + str(minWeight) + " kg.")
            accepted = False
        if (h + l + b > sumDimensions):
            print("The sum of the dimensions of the parcel exceeds " + str(sumDimensions) + " cm.")
            accepted = False
        if (h > maxDimension):
            print("The height of the parcel exceeds " + str(maxDimension) + " cm.")
            accepted = False
        if (l > maxDimension):
            print("The length of the parcel exceeds " + str(maxDimension) + " cm.")
            accepted = False
        if (b > maxDimension):
            print("The breadth of the parcel exceeds " + str(maxDimension) + " cm.")
            accepted = False

def output():
    getWeight()
    getDimensions()
    calculateParcel(weight, height, length, breadth)
    if accepted == False:
        print("The parcel has not been accepted.")
    else:
        print("The parcel has been accepted.")

output()
