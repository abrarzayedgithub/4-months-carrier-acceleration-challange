#json keys must be string
import json
data = {
    'dept': 'EEE',
    'course': "machine learning"
}
x = json.dumps(data)
print(x)

with open('file.txt','w') as f:
    f.write(x)
