def load_products(file_name):
    #open and read
    file = open(file_name)
    lines = file.read()
    file.close()

    #empty dict
    productsDict={}

    #split the lines
    lines=lines.split('\n')

    #iterate over lines
    for line in lines:

        #split lines at spaces
        line=line.split(' ')

        #get product and price
        product=line[0]
        price=float(line[1])

        #empty dict for price and discount
        innerdict={}

        #if theres a discount
        if len(line)==3:
            #get discount
            discount=float(line[2])
            #set price and discount
            innerdict['price']=price
            innerdict['discount']=discount
        else: # if theres no discount
            innerdict['price']=price
        
        productsDict[product]=innerdict

    return productsDict

print(load_products('file.txt'))
"""

Implement the function:
def load_products(file_name):
...
return ...
which reads the file with the given name and returns a data structure
similar to the one shown in Question 1, e.g. the one with product names,
prices and discounts. The structure of the file should be as follows:
- Each line describes a single product.
- The first word in the line is the product name. For simplicity, we
assume that all products have one-word names.
- The second word is a real number and represents the price.
- If there is a third word, then it is also a real number and represents
the discount. If there is no third word, then you should not put any
discount key in the dictionary.
Note that the file format is defined in such a way that it is enough to use
the split() method to split each line into words. You don’t need to do any
complicated tokenizations.
The following is an example file content which represents exactly the
data structure from Question 1.
äpple 27.90
vispgrädde 21.50 2
jordgubbar 57.90 3

"""