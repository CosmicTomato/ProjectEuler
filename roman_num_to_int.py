#takes in a roman numeral and outputs its corresponding integer

def main( numeral ):
#numeral should be entered as string

	ans = 0

	num_list = list( numeral )
	#creates list with entries that are the letters of the numeral

	while num_list[ 0 ] == 'M':
		ans += 1000
		num_list = num_list[ 1 : ]
	#each loop peels off a leading M and adds 1000 to sum

		if len( num_list ) == 0:
			return ans
		#returns answer if number has been fully analyzed

	if len( num_list ) >= 2:
		if num_list[ 0 : 2 ] == ['C', 'M']:
			ans += 900
			num_list = num_list[ 2 : ]

			if len( num_list ) == 0:
				return ans
			#returns answer if number has been fully analyzed

	while num_list[ 0 ] == 'D':
		ans += 500
		num_list = num_list[ 1 : ]

		if len( num_list ) == 0:
			return ans
		#returns answer if number has been fully analyzed

	if len( num_list ) >= 2:
		if num_list[ 0 : 2 ] == ['C', 'D']:
			ans += 400
			num_list = num_list[ 2 : ]

			if len( num_list ) == 0:
				return ans
			#returns answer if number has been fully analyzed

	while num_list[ 0 ] == 'C':
		ans += 100
		num_list = num_list[ 1 : ]

		if len( num_list ) == 0:
			return ans
		#returns answer if number has been fully analyzed

	if len( num_list ) >= 2:
		if num_list[ 0 : 2 ] == ['X', 'C']:
			ans += 90
			num_list = num_list[ 2 : ]

			if len( num_list ) == 0:
				return ans
			#returns answer if number has been fully analyzed

	while num_list[ 0 ] == 'L':
		ans += 50
		num_list = num_list[ 1 : ]

		if len( num_list ) == 0:
			return ans
		#returns answer if number has been fully analyzed

	if len( num_list ) >= 2:
		if num_list[ 0 : 2 ] == ['X', 'L']:
			ans += 40
			num_list = num_list[ 2 : ]

			if len( num_list ) == 0:
				return ans
			#returns answer if number has been fully analyzed

	while num_list[ 0 ] == 'X':
		ans += 10
		num_list = num_list[ 1 : ]

		if len( num_list ) == 0:
			return ans
		#returns answer if number has been fully analyzed

	if len( num_list ) >= 2:
		if num_list[ 0 : 2 ] == ['I', 'X']:
			ans += 9
			num_list = num_list[ 2 : ]

			if len( num_list ) == 0:
				return ans
			#returns answer if number has been fully analyzed

	while num_list[ 0 ] == 'V':
		ans += 5
		num_list = num_list[ 1 : ]

		if len( num_list ) == 0:
			return ans
		#returns answer if number has been fully analyzed

	if len( num_list ) >= 2:
		if num_list[ 0 : 2 ] == ['I', 'V']:
			ans += 4
			num_list = num_list[ 2 : ]

			if len( num_list ) == 0:
				return ans
			#returns answer if number has been fully analyzed

	while num_list[ 0 ] == 'I':
		ans += 1
		num_list = num_list[ 1 : ]

		if len( num_list ) == 0:
			return ans
		#returns answer if number has been fully analyzed

	return ans


