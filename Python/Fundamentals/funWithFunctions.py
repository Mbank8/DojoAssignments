
# def odd_even (a):
#     while a < 2001:
#         if a % 2 != 0:
#             print "Number is %d. This is an odd number." % (a)
#             a += 1
#         else:
#             print "Number is %d. This is an even number." % (a)
#             a+= 1
#     return(a)
# odd_even(1)

# def multiply(arr,num):
#     for x in range(len(arr)):
#         arr[x] *= num
#     return arr
# a = [2,4,10,16]
# b = multiply(a,5)
# print b

def layered_multiples(arr):
    print arr
    for x in range(len(arr)):
        arr[x] *= num
        arr[x] = 1
    return arr
x = layered_multiples(([2,4,5],3))
print x