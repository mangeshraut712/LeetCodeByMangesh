class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        ap = res.append
        bal = 0

        # First pass: drop invalid ')'
        for c in s:
            if c == '(':
                bal += 1
                ap(c)
            elif c == ')':
                if bal:
                    bal -= 1
                    ap(c)
            else:
                ap(c)

        # Second pass: drop excess '(' from the end
        if bal:
            out = []
            ap2 = out.append
            for c in reversed(res):
                if c == '(' and bal:
                    bal -= 1
                else:
                    ap2(c)
            return "".join(reversed(out))

        return "".join(res)
