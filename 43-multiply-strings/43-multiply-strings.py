class Solution :
    def multiply(self, num1: str, num2: str) -> str:
            ans = 0
            for i1, v1 in enumerate(reversed(num1)):
                for i2, v2 in enumerate(reversed(num2)):
                    ans += (10**i1)*int(v1)*(10**i2)*int(v2)
            return str(ans)