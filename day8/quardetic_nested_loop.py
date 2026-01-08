listA = [i*2 for i in range(1,10001)]
listB = [i*3 for i in range(1,10001)]

def findduplicates(listA,listB):
     duplicates = []
     for i in listA:
         for j in listB:
              if i == j:
                   duplicates.append(i)


     return duplicates

print(f"common elements{findduplicates(listA,listB)}")

        
        

             

                                            
                                