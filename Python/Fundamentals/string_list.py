'''words = "It's thanksgiving day. It's my birthday , too!"
print words.find("day")
new_words = words.replace("day", "month")
print new_words

x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0]
print x[0::len(x)-1]
new_list = x[0::len(x)-1]
print new_list'''

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x_new = sorted(x)
x_new
y = x_new[:len(x)/2]
z = x_new[-5:]
z
answer = [y] + z
print answer

