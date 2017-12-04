truefalse = True or False and True or not False

print truefalse  

"""
  console i/o
"""
def console_io():
  answer = raw_input("Can I haz function? ")
  if answer == 'yes' and not 'no' or not 'n':
    print 'yes, you can haz function'
  else:
    print 'No, you can\'t haz function'

# console_io() 

"""
  higher order function
"""
def HOF(func, arg): func(arg)

def func(arg): 'This is the arg: %s' % (arg)

# print HOF(func, 'Some arg.')

"""
  currying 
"""
def curry(arg1): return lambda arg2: arg1 + arg2

five = curry(5)
seven = five(2)

print seven

"""
  Lists
"""
def list_slicer(list): return lambda start, end: list[start:end]

list_to_slice = list_slicer([1,2,3,4,5])

list_section = list_to_slice(0, 3)

print list_section

