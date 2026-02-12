#program to calculate discount


def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    if price <= 0:
        return "The price should be greater than 0"
    
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    discount_allowed = (price * discount) / 100
    total = price - discount_allowed
    
    return total


print(apply_discount(100, 80))
print(apply_discount(200, 50))
print(apply_discount(74.5, 20.0))


