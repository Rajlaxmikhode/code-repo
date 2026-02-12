#program to calculate discount
def discount_calc(price,discount):
    discount_allowed=(price*discount)/100
    print(discount_allowed)
    total=price-discount_allowed
    return total
    
print(discount_calc(900,10))
