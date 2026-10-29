
class Solution(object):
    def addDigits(self, num):

        while num >= 10:
            temp = 0

            while num > 0:
                digit = num % 10
                temp = temp + digit
                num = num // 10

            num = temp

        return num
