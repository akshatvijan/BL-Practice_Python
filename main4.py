#program 5 Time Conversion
second=int(input("Enter second"))
hour=second//3600
min=(second//3600) %60
sec=second%60

print(f"time is {hour:02d}:{min:02d}:{sec:02d}")