# a = "Vinod void"
# print(len(a))

# print(str(len(a) - 1))

# # find a lenth of the string 
# b = len(a)
# # find a index of the last charac d 
# c = b - 1
# # print the character
# print(a[c])

# a = "Hello, World!"
# b = a.replace("l", "j")
# b = a.upper()
# print(b)

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# price = 59
# txt = "The price is " + str(price) + " dollars"
# print(txt)

# s = "ab123"
# print(s.isalnum())
# import textwrap
# string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# max_width = 4
# wrap_text=textwrap.wrap(string, width=max_width)
# for i in wrap_text:
#     print(i)

# import textwrap

# def wrap(string, max_width):
#     wrap_text=textwrap.wrap(string, width=max_width)
#     for i in wrap_text:
#         output = i
#         return 

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

# def print_formatted(number):
#     max_width = len(str(number))
#     for i in range(1,number+1):
#         decimal = i
#         octal = oct(decimal)
#         hexadecimal = hex(decimal)
#         binary = bin(decimal)
#         print(f"{decimal} {octal[2:]} {hexadecimal[2:].upper()} {binary[2:]}") 

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)
