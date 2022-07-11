#nested function calls = function calls inside other function calls
#                        innermost function calls are resolves first
#                        returned value is used as argument for the next outer function

num = input("Enter a whole positive number: ")
num=float(num)
num = abs(num)
num = round(num)
print(num)

#Ez az egy sor ugyan az mint a fenti 5 sor.
print(round(abs(float(input("Enter a whole positive number: ")))))