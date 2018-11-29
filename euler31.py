#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

#    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

#It is possible to make £2 in the following way:

#    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

#How many different ways can £2 be made using any number of coins?



num_comb = 0 #intializing

total_pence = 200 #intializing, should work for other numbers

for one_pence in range(0,total_pence + 1):  #allows up to total_pence one pence coins

 for two_pence in range(0,(total_pence - (one_pence) ) // 2 + 1): #allows up to max number of 2 pence coins

  for five_pence in range(0,(total_pence - (one_pence + two_pence* 2) ) // 5 + 1): #allows up to max number of 5 pence coins

   for ten_pence in range(0,(total_pence - (one_pence + two_pence * 2 + five_pence * 5) ) // 10 + 1): #allows up to max number of 10 pence coins

    for twenty_pence in range(0,(total_pence - (one_pence + two_pence * 2 + five_pence * 5 + ten_pence * 10) ) // 10 + 1): #allows up to max number of 20 pence coins

     for fifty_pence in range(0,(total_pence - (one_pence + two_pence * 2 + five_pence * 5 + ten_pence * 10 + twenty_pence * 20) ) // 20 + 1): #allows up to max number of 50 pence coins

      for one_pound in range(0,(total_pence - (one_pence + two_pence * 2 + five_pence * 5 + ten_pence * 10 + twenty_pence * 20 + fifty_pence * 50) ) // 100 + 1): #allows up to max number of 1 pound coins

       for two_pound in range(0,(total_pence - (one_pence + two_pence * 2 + five_pence * 5 + ten_pence * 10 + twenty_pence * 20 + fifty_pence * 50 + one_pound * 100) ) // 200 + 1): #allows up to max number of 2 pound coins

        value = (one_pence + two_pence * 2 + five_pence * 5 + ten_pence * 10 + twenty_pence * 20 + fifty_pence * 50 + one_pound * 100 + two_pound * 200) #calculates value of coin combination

        #adds 1 to num_comb (number of combinations) if coin combination adds up to exactly the total desired value
        if value == total_pence:

         num_comb += 1

print (num_comb)

