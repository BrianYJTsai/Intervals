#  File: Intervals.py

#  Description: Program determines the least number of unions that include all sets of numbers. User inputs a set of tuple numbers
#  and the program outputs the short number of tuples needed to encompass the whole set

#  Student Name: Brian Tsai

#  Student UT EID: byt76

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 4/25/17

#  Date Last Modified: 4/25/17

# Returns a a list of tuples that have been shortened to encompass all unions 
def set_check(interval_list):
	set_list = []
	set_list.append(interval_list[0])
	
	# Iterate over the original list of numbers
	for index in range(len(interval_list)):
		
		# interval_set1 contains a set of the first interval in the original list
		interval_set1 = set(range(min(interval_list[index]), max(interval_list[index]) + 1))
		
		# interval_set2 contains a set of the first interval in the new list
		interval_set2 = set(range(min(set_list[len(set_list) - 1]), max(set_list[len(set_list) - 1]) + 1))
		
		# interval_set3 contains an intersection of the two sets
		interval_set3 = interval_set1 & interval_set2
		
		# If the intersection is larger than 0, then add a new union set to set_list
		if (len(interval_set3) > 0):

			# new_interval is the union of interval_set1 and interval_set2
			new_interval = interval_set1 | interval_set2
			new_interval = (min(new_interval), max(new_interval))
			
			set_list[len(set_list) - 1] = new_interval
		
		# Else, add a new interval to set_list from the original list
		else:
			set_list.append(interval_list[index])

	return set_list

# Returns a dictionary sorted by keys
def sort_dict(interval_dict):

	# sorted_size contains a list of sorted values 
	sorted_size = sorted(interval_dict, key = interval_dict.__getitem__)
	
	#return sorted list of intervals based on interval length
	return sorted_size


# Output the dictionary 
def print_dict(dict, string):
	print(string)
	for key in dict:
		print(key)

# Output the list
def print_list(list, string):
	print(string)
	for interval in list:
		print(interval)		

# Return a list of tuples from the buffer 			
def init_tupleList(interval_input):
	interval_list = []
	
	# Convert each line into a tuple and add it to the list
	for interval in interval_input:
		# Split line into list of strings
		entry_interval = interval.split()
		
		# Typecast each element into an integer
		entry_interval = [int(x) for x in entry_interval]

		# Convert each interval into a tuple 
		entry_interval = tuple(entry_interval)

		# Add tuple to tuple list
		interval_list.append(entry_interval)

	# Sort the tuple list and return it
	interval_list.sort()
	return interval_list

def main():
	# Open the buffer
	interval_input = open("intervals.txt", "r")
	
	# Create new list and dictionary
	interval_list = []
	interval_dict = {}
	
	# interval_list contains a list of tuples
	interval_list = init_tupleList(interval_input)
	
	# interval_list contains a list of corrected tuples
	interval_list = set_check(interval_list)
		
	# Set the key for each dict to be the length of each interval
	for interval in interval_list:
		interval_dict[interval] = max(interval) - min(interval)
		
	# sorted_dict contains a dictionary sorted by keys
	sorted_size = sort_dict(interval_dict)
	
	# Output a list of tuples sorted by the left limit
	print_dict(interval_dict, "Non-intersecting Intervals:")
	print()

	# Output a list of tuples sorted by length
	print_list(sorted_size, "Non-intersecting Intervals in order of size:")
	interval_input.close()
			
main()	