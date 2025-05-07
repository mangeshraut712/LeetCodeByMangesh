class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = list(s)
        st = []
        for i, c in enumerate(arr):
            if c == '(':
                st.append(i)
            elif c == ')':
                if st:
                    st.pop()
                else:
                    arr[i] = ''
        for i in st:
            arr[i] = ''
        return ''.join(arr)
