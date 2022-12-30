def bubbleSort(a):

  # to get all elements in the array
  for i in range(1, len(a)):
    print("\n")
    print(i," iteration")
 
    # to compare each element in the array
    for j in range(0, len(a)-i):

      # to compare each adjacent element
      if a[j]>a[j+1]:

        # swapping the element if it's not in intended order
        temp = a[j]
        a[j] = a[j+1]
        a[j+1]=temp
        print(a)
array = [6,3,2,1,0]
bubbleSort(array)