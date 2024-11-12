#QUESTION ONE a)
def even_numbers(numbers):
     even_num = [i for i in numbers if i % 2 ==0]
     return even_num

# Example usage:
numbers = [1,2,3,4,5,6]
print(even_numbers(numbers))

#b)
def multiplication_table(number):
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

number = 8
multiplication_table(number)

#c)
def get_largest_number(numbers):
    if not numbers:
          return None
     
    largest = numbers[0]
    for num in numbers:
        if num >largest:
         largest = num
    return largest

numbers = [3,5,7,8,-1,4]
largest = get_largest_number(numbers)
print(largest)

#d
input_string = "hello"
comparison_string = "hello"
if input_string == comparison_string:
    print("its the same string")
else:
    print("its not the same string")    

