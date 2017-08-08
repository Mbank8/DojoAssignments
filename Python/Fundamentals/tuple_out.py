my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

# def tuplesOut(arr):
#     print [(key,value) for key,value in my_dict.iteritems()]
   
   
# tuplesOut(my_dict)

def tuplesOut(arr):
    print zip(my_dict.keys(), my_dict.values())
    
   
tuplesOut(my_dict)