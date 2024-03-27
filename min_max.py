
def get_stats(numbers):
    
    minimum=min(numbers)
    maximum=max(numbers)
    return minimum, maximum

myNumbers=[12, 43, 20, 38, 28]

minimum, maximum=get_stats(myNumbers)

print(f'Min: {minimum}, Max: {maximum}')
