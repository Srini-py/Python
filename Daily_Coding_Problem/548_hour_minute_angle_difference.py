'''
Given a clock time in hh:mm format, determine, to the nearest degree,
the angle between the hour and the minute hands.
'''


time = input("Enter the time in hh:mm format : ")
hrs = int(time[:2])
mins = int(time[3:])

difference = abs(mins*6 - ((hrs%12)*30 + mins/2))
print("%f degrees" %(difference))