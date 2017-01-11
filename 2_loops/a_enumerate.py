choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    #print the index (one-based), and the item
    print index + 1, item
