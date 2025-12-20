#by for loop
nums = [5,1,15,46,254]
min_value = nums[0]
for n in nums:
    if n < min_value:
        min_value = n
print("min value:",min_value)

#by while loop
nums = [5,1,15,46,254]
min_value = nums[0]
i = 0
while i < len(nums):
    if nums[i] < min_value:
        min_value = nums[i]
    i += 1
print("min value:",min_value)
