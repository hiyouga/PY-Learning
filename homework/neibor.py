def main():
    t = int(input())
    nums = list(map(int, input().split()))
    if t != len(nums):
        return
    nums.sort()
    ans = []
    for i in range(len(nums)-1):
        ans.append((nums[i+1] - nums[i], nums[i], nums[i+1]))
    ans.sort()
    for d, p, q in ans:
        if d == ans[-1][0]:
            print(str(p) + " " + str(q))
main()