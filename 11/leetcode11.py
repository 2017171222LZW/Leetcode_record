class Solution:
    def maxArea(self, height: list) -> int:
        cur1, cur2 = 0, len(height)-1
        max_water = 0
        step = cur2 
        while cur1 < cur2:
            if height[cur1] <= height[cur2]:
                mw = step*height[cur1]
                max_water = max(max_water, mw)
                cur1 += 1
            else:
                mw = step*height[cur2]
                max_water = max(max_water, mw)
                cur2 -= 1
            step -= 1
        return max_water
if __name__ == '__main__':
    s = Solution()
    height = [2,3,4,5,18,17,6]
    max_water=s.maxArea(height)
    print(max_water)
