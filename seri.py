def max_pairwise_product(numbers):
    max1 = float('-inf')
    max2 = float('-inf')
    
    for num in numbers:
        if num >= max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    return max1 * max2

# Example usage:
# numbers = [1, 2, 3, 4, 5]
# print(max_pairwise_product(numbers))
