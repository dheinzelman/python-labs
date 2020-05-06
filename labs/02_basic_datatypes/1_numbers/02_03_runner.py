'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
sec_to_hr = 1/3600 # 3600 seconds in 1 hour
min_to_hr = 1/60 # 60 minutes in 1 hour
miles_to_km = 1.6 # 1 mile = 1.6 km

time_hrs = (30*min_to_hr) + (30*sec_to_hr)
dist_kilometers = 10 * miles_to_km

average_speed = dist_kilometers/time_hrs

answer = ("Average speed = " + str(average_speed) + " kilometers per hour")

print(answer)