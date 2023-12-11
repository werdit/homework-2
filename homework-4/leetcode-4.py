#1-masala
# class Solution(object):
#     def romanToInt(self, s):
#         rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
#         i = 0
#         a = 0
#         while i < len(s):
#             if i+1<len(s) and s[i:i+2] in rom:
#                 a+=rom[s[i:i+2]]
#                 i+=2
#             else:
#                 a+=rom[s[i]]
#                 i+=1
#         return a
# obj=Solution()
# print(obj.romanToInt(input("input roman number: ")))
#
#
# #2-masala
# class Solution(object):
#     def isPalindrome(self, x):
#         if str(x)==str(x)[::-1]:
#             return True
#         else:
#             return False
# obj=Solution()
# print(obj.isPalindrome(input("input number: ")))

#3-masala
class Solution(object):
    def reverse(self, x):
        if x > -2 ** 31 and x < 2**31-1:
            if x < 0:
                a=-1
            else:
                a=1
            x *= a
            res = int(str(x)[::-1])
            return a * res

obj=Solution()
print(obj.reverse(int(input("input number: "))))