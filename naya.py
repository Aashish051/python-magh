range 
start=int(input("Enter the start number: "))
stop=int(input("Enter the stop number :"))
step=int(input("Enter the step value  :"))
def my_range(start, stop, step):
    while  start < stop:
        print(start)
        if step!=0:
            start+=step
        else:
            start +=1
my_range(start, stop, step)