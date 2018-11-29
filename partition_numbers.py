#calculates the first n numbers in the partition function
#i.e. number of integer sums to make each integer up to n
#see: https://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function

def find_pent_nums( n ):
#finds the GENERALIZED pentagonal numbers up to n
#see https://en.wikipedia.org/wiki/Pentagonal_number
#and https://en.wikipedia.org/wiki/Pentagonal_number_theorem

	num_list = [ 0, 1 ]
	index = 1

	while abs( num_list[ -1 ] ) < n:
		index = index * ( - 1 )
		next_num = ( ( ( 3 * ( index ** 2 ) ) - index ) // 2 )
		num_list.append( next_num )

		index = index * ( - 1 )
		index += 1
		next_num = ( ( ( 3 * ( index ** 2 ) ) - index ) // 2 )
		num_list.append( next_num )

	return num_list


def find_partition_nums( n ):
#finds first n partition numbers

	pent_list = find_pent_nums( n + 1 )
	partitions_list = [ 1 , 1 ]
	#since partition function of zero is defined to be equal to one

	partitions_found = 2

	while partitions_found < ( n + 1 ):
	#want to search until partition for n has been found

		index = 0
		while pent_list[ index ] <= partitions_found:
			index += 1
		#finds max index of list of pentagonal numbers to be used
#TEST
#		print('index=',index)
#TEST

		new_num = 0
		for i in range( 1, index ):
			if ( i % 4 ) == 1 or ( i % 4 ) == 2:
				neg_pos = 1
			else:
				neg_pos = -1
			new_num += ( partitions_list[ ( ( -1 ) * pent_list[ i ] ) ] ) * ( neg_pos )
		#finds next partition number
#TEST
#		print('new_num=',new_num)
#TEST

		partitions_list.append( new_num )
		partitions_found += 1

	return partitions_list



