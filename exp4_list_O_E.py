def separate_even_odd(input_list):
    even_list = []
    odd_list = []
    
    for num in input_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    
    return even_list, odd_list

def merge_and_sort(even_list, odd_list):
    merged_list = even_list + odd_list
    merged_list.sort()  
    return merged_list

def main():
    user_input = input("Enter a list of numbers (separated by spaces): ")
    
    input_list = list(map(int, user_input.split()))
    
    even_list, odd_list = separate_even_odd(input_list)
    
    sorted_list = merge_and_sort(even_list, odd_list)
    
    print("Original list:", input_list)
    print("Even numbers:", even_list)
    print("Odd numbers:", odd_list)
    print("Merged and sorted list:", sorted_list)

main()
