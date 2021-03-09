'''You live 4 miles from the university. The bus drives at 25mph but spends 2 minutes at each of
the 10 stops on the way. How long will the bus journey take? Alternatively, you could run to university.
You jog the first mile at 7 mph; then run the next two at 15mph; before jogging the last at 7 mph  again.
 Will this be quicker or slower than the bus?
'''
miles_from_university=4
speed_of_bus=25
time_taken=((miles_from_university/speed_of_bus)*60)
# 2 minutes in each stop
time_spend_on_stops=20
total_time=time_spend_on_stops+time_taken
print('the total time taken ny the bus is',total_time)
jog_1=(1/7)*60
jog_2=(2/15)*60
jog_3=(1/7)*60
total_walk_time=jog_1+jog_2+jog_3
print('The time taken to run is ',total_walk_time)
if (total_time>total_walk_time):
    print("the bus is slower then running")
else:
    print("the running is slower then the bus")
