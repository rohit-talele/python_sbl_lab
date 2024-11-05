def update_and_find(lst, x):
    lst[0] = x
    
    middle_index = len(lst) // 2
    del lst[middle_index]
    
    max_element = max(lst)
    min_element = min(lst)
    
    return lst, max_element, min_element

n = int(input("Enter the number of elements in the list: "))
my_list = []

print("Enter the elements of the list:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    my_list.append(element)

x_value = int(input("Enter the value of x to update the first element: "))

updated_list, max_value, min_value = update_and_find(my_list, x_value)

print(f"\nUpdated List: {updated_list}")
print(f"Max Element: {max_value}")
print(f"Min Element: {min_value}")
