class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(float(tokens[i-2]))
                    b = int(float(tokens[i-1]))
                    if tokens[i] == "+":
                        result = a + b
                    elif tokens[i] == "-":
                        result = a - b
                    elif tokens[i] == "*":
                        result = a * b
                    else:
                        result = a / b

                    tokens = (tokens[:i-2] + [str(result)] + tokens[i+1:])
                    break
        return int(float(tokens[0]))