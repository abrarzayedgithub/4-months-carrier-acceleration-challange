#use collections.counter
#anagrams are those words whose letters are same but order is different

from collections import Counter
x = 'silent'
y = 'listen'
def  checkanagram(x,y):
    sorted(x)
    sorted(y)
    return Counter(x) == Counter(y)
print(checkanagram(x,y))