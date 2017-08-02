list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

def compareArrays(lst1, lst2):
    
    if sorted(list_one) == sorted(list_two):
        print "The lists are the same"
    
    else:
        print "The lists are not the same"

compareArrays(list_one, list_two)
