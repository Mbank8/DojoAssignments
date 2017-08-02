mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]


def list_type(lst):
    new_string = ''
    total = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The list you entered is a mixed type:"
        print "String:", new_string
        print "Sume:", total

    elif new_string:
        print "The list you entered is of string type"
        print "String:", new_string

    elif total:
        print "The list you entered is of integer type"
        print "Sum:", total

    
print list_type(mixed_list)
print list_type(string_list)
print list_type(integer_list)