#https://discuss.leetcode.com/topic/78879/python-solution-with-o-n
def getNextGreaterElement(findNums, nums):
    if not findNums or not nums:
        return
    stack = []
    d = {}
    for i in nums[::-1]:
        while stack and stack[-1] <= i:
            stack.pop()
        d[i] = stack[-1] if stack else -1
        stack.append(i)
    return [d[i] for i in findNums]


def getNextGreaterElement2(findNums, nums):
    if not findNums or not nums:
        return None
    d = {}
    st = []
    for i in nums:
        while st and st[-1] < i:
            d[st.pop()] = i
        st.append(i)
    return [d.get(i, -1) for i in findNums]
print(getNextGreaterElement([4,1,2], [1,3,4,2]))
print(getNextGreaterElement2([4,1,2], [1,3,4,2]))