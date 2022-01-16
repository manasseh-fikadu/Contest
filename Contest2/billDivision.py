def bonAppetit(bill, k, b):
    # Write your code here
    billed = b - (sum(bill) - bill[k]) // 2
    if billed:
        print(billed)
    else:
        print("Bon Appetit")
