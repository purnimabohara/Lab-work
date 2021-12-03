#convert seconds into days,minutes and seconds
seconds= int(input("enter the time in seconds"))
days=seconds/86400
hours=seconds/3600
minute=seconds/60
print(f"total day for given seconds: {days}")
print(f"total hours for given seconds: {hours}")
print(f"total minutes for given seconds: {minute}")
