def decorator(func):
    def wrapper():
        print(f"before function")
        func()
        print(f"after function")
    return wrapper
def hello():
    print("data science")

new_func = decorator(hello)
new_func()


#Wrapper function হলো এমন একটি ফাংশন, 
# যা আরেকটি ফাংশনকে ঘিরে (wrap করে) রাখে এবং তাকে কল করার আগে/পরে অতিরিক্ত কিছু কাজ করে।