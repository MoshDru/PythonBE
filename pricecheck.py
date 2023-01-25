# Function to check errors in prices

def priceCheck(products, productPrices, productSold, soldPrice):
    errors = 0
    products_prices = dict(zip(products, productPrices))
    for i in range(len(productSold)):
        if products_prices[productSold[i]] != soldPrice[i]:
            errors += 1
    return errors

# Test the function
products = ["apple", "banana", "orange", "pear", "peach", "plum"]
productPrices = [0.5, 0.25, 0.75, 0.3, 0.4, 0.6]
productSold = ["apple", "banana", "orange", "pear", "peach", "plum"]
soldPrice = [0.5, 0.3, 0.75, 0.6, 0.5, 0.19]
print(priceCheck(products, productPrices, productSold, soldPrice)) # output: 1
