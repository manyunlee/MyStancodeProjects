"""
File: weather_master.py
Name: Mandy Lee
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT=-1 # This constant controls when to stop


def main():
	"""
	1. If no data->print "No temperatures were entered"
	2. If one data->highest=lowest=average
	3. If more than one data, input data until the EXIT number-> find highest/lowest/average
	"""
	print('stanCode \"Weather Master 4.0\"!')
	x=int(input('Next Temperature: (or -1 to quit)? '))
	if x < 16:
		cold = 1
	else:
		cold = 0  # start from the first data, if next data is exit->not count

	if x==EXIT:
		print('No temperatures were entered')
	else:
		highest = x  # assign the first data as highest
		lowest = x  # assign the first data as lowest
		count=1  # start from the first data, if next data is exit->not count
		summation = x  # start from the first data, if next data is exit->not sum up

		while x!=EXIT:
			y=int(input('Next Temperature: (or -1 to quit)? '))  # assign new data as y (always name y as new data)

			if y==EXIT:  # if next data is EXIT->break
				break  # if there's only one data->print one data
			else:
				if y>highest:
					highest=y  # replace highest with new data, lowest not change
				elif y<lowest:
						lowest=y  # replace lowest with new data, highest not change
			count = count + 1
			summation = summation + y
			x = y  # assign x as y, new y come in and p.k. with old y
			if y < 16:
				cold = cold + 1

		print('Highest temperature= '+str(highest))  # print the result when the while function end
		print('Lowest temperature= ' + str(lowest))
		print('Average= ' + str(float(summation/count)))
		print(str(cold)+' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
