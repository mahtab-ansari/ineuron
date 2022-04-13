'''str = input("Please Enter a String : ")
rev_str = str[::-1]
print("Reverse of the Input String : ",rev_str)'''


def str_rev(inp_str):
    inp_str = inp_str[::-1]
    return inp_str
str = input("Please Enter a String : ")
rev_str = str_rev(str)
print("Reverse of the Input String : ",rev_str)