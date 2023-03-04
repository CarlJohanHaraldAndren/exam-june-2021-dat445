def shopping():
    products = {
        "äpple":
            {"price": 27.90
             },
        "vispgrädde":
            {"price": 21.50
                , "discount": 2
             },
        "jordgubbar":
            {"price": 57.90
                , "discount": 3
             }
    }
    total_sum = 0
    while True:
        product = input("Product? ")
        if product == "":
            break
        elif product not in products:
            print("Sorry we don't have " + product)
        else:
            quantity = int(input("Quantity? "))
            price = products[product]["price"]
            discount = products[product].get("discount", 0)
            sum = price * quantity * (1 - discount / 100)
            total_sum += sum
            print("Sum: {:.2f}".format(sum))
            print("Total: {:.2f}".format(total_sum))


shopping()

"""

Question 1
The following variable:

products = {
"äpple":
{"price": 27.90
},
"vispgrädde":
{"price": 21.50
,"discount": 2
},
"jordgubbar":
{"price": 57.90
,"discount": 3
}
}

contains information about the product list in a shop. It is assigned to a
dictionary where the keys are the product names and the values are
other dictionaries which describe the pricing of the corresponding
product. The nested dictionary can only have two keys: "price" and
"discount". The price is what you normally pay for the product, but if
there is also a discount then you deduce that many percentages from
the final sum paid for the product.
Implement the function shopping() which repeatedly asks the customer
for product name and quantity. Based on the product name and the
quantity it computes the sum to be paid after deducting the potential
discount. After each interaction, the program prints the sum for the
current product and the total sum accumulated so far. The interaction
stops when the customer enters an empty string for the product name.
On the other hand, if the customer enters a product name that is not
listed in the above variable, then the program must print a reasonable
message without failing.
An example interaction follows:
>>> shopping()
Product? äpple
Quantity? 2
Sum:   55.8 # no discount applied
Total: 55.8
Product? mjölk
Sorry we don't have mjölk # error message printed
Product? vispgrädde
Quantity? 1
Sum:   21.07 # 2% discount
Total: 76.87 # total = 55.8+21.07
Product? # no product name -> exit

"""