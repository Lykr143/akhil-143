# def rotate_list(l,n):
# 	return l[n-1:] + l[:n-1]
# l = [1,2,3,4,5]
# print("original list :", l)
# print("rotoate list :", rotate_list(l,3))

# l = "matam"
# def palindrome(l):
# 	for i in range(len(l)):
# 		t = l[:i] + l[i+1:] 
# 		if t == t[::-1]:
# 			return True
	
# 	return l[::-1]	
# print(palindrome(l))



# l = [1,2,0,2,0,0,2,3,4]
# def solution(nums):
# 	for i in nums:
# 		if 0 in nums:
# 			nums.remove(0)
# 			nums.append(0)
# 	return nums
# print(solution(l))


# l1 = [1,2,0,2,0,0,2,3,4]
# j = 0
# for i in range(len(l)):
# 	if l1[i] != 0:
# 		l1[j], l1[i] = l1[i],l1[j]
# 		j = j +1 
# print(l1)		


class A:
	a = 3
	b = 6
def add(self,a,b):
	return a + b
	
def __init__(self):
	print("i am constructor")
obj = A()
print(obj.add())	
		


