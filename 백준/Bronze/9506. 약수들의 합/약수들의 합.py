while True:
    n = int(input())
    
    if n == -1:
        break
    nums = {1}
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            nums.add(i)
            nums.add(n//i)
      
    if sum(nums) == n:
        nums = list(nums)
        nums.sort()
        nums = [str(i) for i in nums]
        print(f'{n} =', ' + '.join(nums))
    else:
        print(f'{n} is NOT perfect.')