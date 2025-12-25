attendence = {
    "Rahim": [1,1,0,1,1],
    "karim": [1,0,0,1,0],
    "esha" : [1,1,1,1,1],
}
for name,days in attendence.items():
    present = 0
    for d in days:
        if d == 1:
            present += 1
    percentage  =(present/len(days)) * 100
    print(name,"attendence:",percentage,"%")
