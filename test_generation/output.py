from input import *
import unittest
import itertools
import re
# sorts list a and changes order of list b in the way done with a  
def sort(a, b):
    if len(a) == 1:
        return
    for i in range(0,len(a) - 1):
        for j in range(0, len(a) - 1):
            if (a[j] >= a[j+1]):
                temp = a[j];
                a[j] = a[j+1]
                a[j+1] = temp
                temp = b[j]
                b[j] = b[j+1]       
                b[j+1] = temp;
# check ranges            
def check_range(a, b):
    for i in range(1, len(a)):
        if a[i] <= b[i-1]:
            print a[i], b[i-1]
            raise Exception("Invalid ranges")
        
doc = main.__doc__
l = doc.split('\n');
l.remove(l[0])
l.remove(l[len(l) - 1])
for i in range(0, len(l) - 1):
    l[i] = " ".join(l[i].split())
#spec = inspect.getargspec(main);
#args = spec[0];
for i in range(0, len(l)):
    l[i] = re.findall(r'[-0-9]+', l[i])
l1 = []
l2 = []    
# casts strings to ints
for k in range (0, len(l)):
    for p in range(0, len(l[k])):
        l[k][p] = int(l[k][p])
# divides ranges in to two lists 
for i in range(0, len(l)):
    temp = []
    temp1 = []
    for j in range(0, len(l[i])):
        if (j % 2 == 0):
            temp.append(l[i][j])
        else:
            temp1.append(l[i][j])
    l1.append(temp)
    l2.append(temp1)
# sorting ranges    

for i in range(0, len(l1)):
    sort(l1[i], l2[i])
# check ranges    
for i in range(0, len(l1)):
    check_range(l1[i], l2[i])
# generate testcases - combinations from n ranges
testcases = list(itertools.product(*l1))
# Unittest
class DynamicTest(unittest.TestCase):
    pass
## generate test cases dynamically
def test_generator(a):
    def test(self):
        self.assertEqual('pass' , main(*a))
    return test

if __name__ == '__main__':
    i = 0
    for t in testcases:
        test_name = 'test_' + str(i)
        i = i+1
        test = test_generator(t)
        setattr(DynamicTest, test_name, test)
    unittest.main()
    