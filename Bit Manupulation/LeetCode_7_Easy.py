class Solution:
    def reverse(self, x: int) -> int:
        output = 0

        # Check for sign
        if x < 0:
            sign = -1
        else:
            sign = 1

        # update the output
        x = x * sign

        while x != 0:
            output = output * 10 + (x % 10)
            x = x // 10


        return 0 if output < -2 ** 31 or output > 2 ** 31 -1 else output * sign
