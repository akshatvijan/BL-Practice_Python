import statistics
# Function	Use
# mean()	Average
# median()	Middle value
# mode()	Most repeated value
# multimode()	Multiple repeated values
# stdev()	Sample standard deviation
# variance()	Sample variance
daily_max_temperatures = [31.2, 31.5, 30.9, 31.3, 31.7, 31.9, 32.2]
print(f"Mean is {statistics.mean(daily_max_temperatures):.2f}")
print(f"standard deviation is {statistics.stdev(daily_max_temperatures):.2f}")