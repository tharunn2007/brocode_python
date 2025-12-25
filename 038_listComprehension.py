# an compact way to create a list

doubles=[x**2 for x in range(1,11)]
print(doubles)
#OUTPUT:  [1,4,9,...100]

nums=[1,2,3,4,5,-12,-3,-4]
posi_nums= [num for num in nums if num>0] #appends the postive