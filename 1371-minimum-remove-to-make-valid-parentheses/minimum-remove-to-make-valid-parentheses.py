from typing import List

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        a = list(s)
        st = []
        ap, pop = st.append, st.pop
        for i, c in enumerate(a):
            if c == '(':
                ap(i)
            elif c == ')':
                if st:
                    pop()
                else:
                    a[i] = ''
        for i in st:
            a[i] = ''
        return ''.join(a)
