d,w,h = map(int,input().split())

x = ((d**2) /((h**2)+(w**2))) ** 0.5

print(int(x*w),int(x*h))