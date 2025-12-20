#by for loop
nums = [5,1,15,46,254]
max_val = nums[0]
for n in nums:
    if n > max_val:
        max_val = n

print("max value:",max_val)

#by while loop
nums = [5,1,15,46,254]
max_value = nums[0]
i = 0
while i < len(nums):
    print("checking",nums[i],"current max",max_value)
    if nums[i] > max_value:
        max_value = nums[i]
        print("updated max value:",max_value)
    i += 1

print("final max value:",max_value)