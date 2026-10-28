
class Solution(object):
    def subtractProductAndSum(self, n):

        product = 1
        sum = 0

        while n > 0:
            digit = n % 10
            sum += digit
            product *= digit
            n = n // 10

        return product - sum
