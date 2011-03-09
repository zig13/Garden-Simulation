import random
def setup(bias) :
	if bias == 1:
		for i in range(1):
			return random.choice([5, 6, 6, 7, 7, 7, 8, 8, 9])
	if bias == 2:
		return 8 #gives the option for a non-randomised start
	else:
		for i in range(1):
			random.randint(5, 9)

#Setup
x0 = [] ; # x0 as all cells in this array are 0 on the x-axis (1st collumn)
x0.insert(0, setup(1))
x0.insert(1, setup(1))
x0.insert(2, setup(1))
x0.insert(3, setup(1))
x0.insert(4, setup(1))
x0.insert(5, setup(1))
x0.insert(6, setup(1))
x0.insert(7, setup(1))

x1 = [] ; # x1 as all cells in this array are 1 on the x-axis (2nd collumn)
x1.insert(0, setup(1))
x1.insert(1, setup(1))
x1.insert(2, setup(1))
x1.insert(3, setup(1))
x1.insert(4, setup(1))
x1.insert(5, setup(1))
x1.insert(6, setup(1))
x1.insert(7, setup(1))

x2 = [] ; # x2 as all cells in this array are 2 on the x-axis (3rd collumn)
x2.insert(0, setup(1))
x2.insert(1, setup(1))
x2.insert(2, setup(1))
x2.insert(3, setup(1))
x2.insert(4, setup(1))
x2.insert(5, setup(1))
x2.insert(6, setup(1))
x2.insert(7, setup(1))

x3 = [] ; # x3 as all cells in this array are 3 on the x-axis (4th collumn)
x3.insert(0, setup(1))
x3.insert(1, setup(1))
x3.insert(2, setup(1))
x3.insert(3, setup(1))
x3.insert(4, setup(1))
x3.insert(5, setup(1))
x3.insert(6, setup(1))
x3.insert(7, setup(1))

x4 = [] ; # x4 as all cells in this array are 4 on the x-axis (5th collumn)
x4.insert(0, setup(1))
x4.insert(1, setup(1))
x4.insert(2, setup(1))
x4.insert(3, setup(1))
x4.insert(4, setup(1))
x4.insert(5, setup(1))
x4.insert(6, setup(1))
x4.insert(7, setup(1))

x5 = [] ; # x5 as all cells in this array are 5 on the x-axis (6th collumn)
x5.insert(0, setup(1))
x5.insert(1, setup(1))
x5.insert(2, setup(1))
x5.insert(3, setup(1))
x5.insert(4, setup(1))
x5.insert(5, setup(1))
x5.insert(6, setup(1))
x5.insert(7, setup(1))

x6 = [] ; # x6 as all cells in this array are 6 on the x-axis (7th collumn)
x6.insert(0, setup(1))
x6.insert(1, setup(1))
x6.insert(2, setup(1))
x6.insert(3, setup(1))
x6.insert(4, setup(1))
x6.insert(5, setup(1))
x6.insert(6, setup(1))
x6.insert(7, setup(1))

x7 = [] ; # x7 as all cells in this array are 7 on the x-axis (8th collumn)
x7.insert(0, setup(1))
x7.insert(1, setup(1))
x7.insert(2, setup(1))
x7.insert(3, setup(1))
x7.insert(4, setup(1))
x7.insert(5, setup(1))
x7.insert(6, setup(1))
x7.insert(7, setup(1))
	
#Initial Ascii
print "---------------------------------"
print "|" , (x0[7]) , "|" , (x1[7]) , "|" , (x2[7]) , "|" , (x0[7]) , "|" , (x4[7]) , "|" , (x5[7]) , "|" , (x6[7]) , "|" , (x7[7]) , "|"
print "---------------------------------"
print "|" , (x0[6]) , "|" , (x1[6]) , "|" , (x2[6]) , "|" , (x1[6]) , "|" , (x4[6]) , "|" , (x5[6]) , "|" , (x6[6]) , "|" , (x7[6]) , "|"
print "---------------------------------"
print "|" , (x0[5]) , "|" , (x1[5]) , "|" , (x2[5]) , "|" , (x2[5]) , "|" , (x4[5]) , "|" , (x5[5]) , "|" , (x6[5]) , "|" , (x7[5]) , "|"
print "---------------------------------"
print "|" , (x0[4]) , "|" , (x1[4]) , "|" , (x2[4]) , "|" , (x3[4]) , "|" , (x4[4]) , "|" , (x5[4]) , "|" , (x6[4]) , "|" , (x7[4]) , "|       Initial"
print "---------------------------------"
print "|" , (x0[3]) , "|" , (x1[3]) , "|" , (x2[3]) , "|" , (x3[3]) , "|" , (x4[3]) , "|" , (x5[3]) , "|" , (x6[3]) , "|" , (x7[3]) , "|       Garden"
print "---------------------------------"
print "|" , (x0[2]) , "|" , (x1[2]) , "|" , (x2[2]) , "|" , (x3[2]) , "|" , (x4[2]) , "|" , (x5[2]) , "|" , (x6[2]) , "|" , (x7[2]) , "|"
print "---------------------------------"
print "|" , (x0[1]) , "|" , (x1[1]) , "|" , (x2[1]) , "|" , (x3[1]) , "|" , (x4[1]) , "|" , (x5[1]) , "|" , (x6[1]) , "|" , (x7[1]) , "|"
print "---------------------------------"
print "|" , (x0[0]) , "|" , (x1[0]) , "|" , (x2[0]) , "|" , (x3[0]) , "|" , (x4[0]) , "|" , (x5[0]) , "|" , (x6[0]) , "|" , (x7[0]) , "|"
print "---------------------------------"
#everything originates from the bottom left hand corner as in a grapth

#Function to get the growth value of a specific cell based on it's x and y coordinates
def getcell(x, y) :
	if x == 0 :
		x = (x0[y])
	if x == 1 :
		x = (x1[y])  #multiple 'ifs' required as putting an x into the array retrieval (like has been done with y) would make "xx"
	if x == 2 :
		x = (x2[y])
	if x == 3 :
		x = (x3[y])
	if x == 4 :
		x = (x4[y])
	if x == 5 :
		x = (x5[y])
	if x == 6 :
		x = (x6[y])
	if x == 7 :
		x = (x7[y])
	return x
	
print "getcell(5, 5)"
print getcell(5, 5)

#functions to get the growth values of the plants surrounding the plant at the given coordinates
def retN(x, y) : # "retN" as in "retrive north"
	if y == 7 :
		return 0
	if x == 0 :
		return (x0[y+1])
	if x == 1 :
		return (x1[y+1])
	if x == 2 :
		return (x2[y+1])
	if x == 3 :
		return (x3[y+1]) #output is size value for the plant above the given plant (North)
	if x == 4 :
		return (x4[y+1])
	if x == 5 :
		return (x5[y+1])
	if x == 6 :
		return (x6[y+1])
	if x == 7 :
		return (x7[y+1])
		
print "retN(5, 5)"
print retN(5, 5)
		
def retE(x, y) :
	if x == 7 :
		return 0
	if x == 0 :
		return (x1[y])
	if x == 1 :
		return (x2[y])
	if x == 2 :
		return (x3[y])
	if x == 3 :
		return (x4[y]) #output is size value for the plant to the right of the given plant (East)
	if x == 4 :
		return (x5[y])
	if x == 5 :
		return (x6[y])
	if x == 6 :
		return (x7[y])
		
print "retE(5, 5)"
print retE(5, 5)
		
def retS(x, y) :
	if y == 0 :
		return 0
	if x == 0 :
		return (x0[y-1])
	if x == 1 :
		return (x1[y-1])
	if x == 2 :
		return (x2[y-1]) 
	if x == 3 :
		return (x3[y-1]) #output is size value for the plant below the given plant (South)
	if x == 4 :
		return (x4[y-1])
	if x == 5 :
		return (x5[y-1])
	if x == 6 :
		return (x6[y-1])
	if x == 7 :
		return (x7[y-1])
		
print "retS(5, 5)"
print retS(5, 5)
		
def retW(x, y) :
	if x == 0 :
		return 0
	if x == 1 :
		return (x0[y])
	if x == 2 :
		return (x1[y])
	if x == 3 :
		return (x2[y])
	if x == 4 :
		return (x3[y]) #output is size value for the plant to the left of the given plant (West)
	if x == 5 :
		return (x4[y])
	if x == 6 :
		return (x5[y])
	if x == 7 :
		return (x6[y])
		
print "retW(5, 5)"
print retW(5, 5)

#functions to generate the penalty for each neibouring plant		
def penN(x, y) : #"penN" as in "Penalty from North plant"
	if retN(x, y) == 0 :
		return 0 #penalty for each dead (size 0) neighbour
	if retN(x, y) > 6.72 : #the size over which a plant is considered large
		return random.choice([0.46, 0.5, 0.523, 0.528, 0.53]) #penalty for each large neighbour
	else :
		return random.choice([0.24, 0.251, 0.26, 0.28, 0.3]) #penalty for each normal neighbour
		
print "penN(5, 5)"
print penN(5, 5)
		
def penE(x, y) :
	if retE(x, y) == 0 :
		return 0 #penalty for each dead (size 0) neighbour
	if retE(x, y) > 6.72 : #the size over which a plant is considered large
		return random.choice([0.46, 0.5, 0.523, 0.528, 0.53]) #penalty for each large (size 8 or 9) neighbour
	else :
		return random.choice([0.24, 0.251, 0.26, 0.28, 0.3]) #penalty for each normal (size 1 or 7) neighbour
		
print "penE(5, 5)"
print penE(5, 5)
		
def penS(x, y) :
	if retS(x, y) == 0 :
		return 0 #penalty for each dead (size 0) neighbour
	if retS(x, y) > 6.72 : #the size over which a plant is considered large
		return random.choice([0.46, 0.5, 0.523, 0.528, 0.53]) #penalty for each large (size 8 or 9) neighbour
	else :
		return random.choice([0.24, 0.251, 0.26, 0.28, 0.3]) #penalty for each normal (size 1 or 7) neighbour	
		
print "penS(5, 5)"
print penS(5, 5)
		
def penW(x, y) :
	if retW(x, y) == 0 :
		return 0 #penalty for each dead (size 0) neighbour
	if retW(x, y) > 6.72 : #the size over which a plant is considered large
		return random.choice([0.46, 0.5, 0.523, 0.528, 0.53]) #penalty for each large (size 8 or 9) neighbour
	else :
		return random.choice([0.24, 0.251, 0.26, 0.28, 0.3]) #penalty for each normal (size 1 or 7) neighbour
		
print "penW(5, 5)"
print penW(5, 5)

print "total pens"
print penN(5, 5)+(penE(5, 5)+(penS(5, 5)+(penW(5, 5)

#function to add growth and apply penalties		
def alter(x, y) :
	if getcell(x, y) < 1 : #stops plants from coming back from the dead
		return 0
	else :
		return (getcell(x, y)+1)-(penN(x, y)+penE(x, y)+penS(x, y)+penW(x, y)) #+1 per turn growth is added and penalties are removed
print "alter(5, 5)"
print alter(5, 5)

#function to stop growth past 9	
def cap(x, y) :
	if alter(x, y) > 9 : #imposes cap of 9 on growth (so dosn't muck up ascii)
		return 9
	else :
		return alter(x, y)
		
print "cap(5, 5)"
print cap(5, 5)
		
#now what all the above functions are actually for and when they are actually run!
x0.insert(0, cap(0, 0))
x0.insert(1, cap(0, 1))
x0.insert(2, cap(0, 2))
x0.insert(3, cap(0, 3))
x0.insert(4, cap(0, 4))
x0.insert(5, cap(0, 5))       #sets array cells to new values
x0.insert(6, cap(0, 6))
x0.insert(7, cap(0, 7))

x1.insert(0, cap(0, 0))
x1.insert(1, cap(0, 1))
x1.insert(2, cap(0, 2))
x1.insert(3, cap(0, 3))
x1.insert(4, cap(0, 4))
x1.insert(5, cap(0, 5))
x1.insert(6, cap(0, 6))
x1.insert(7, cap(0, 7))

x2.insert(0, cap(0, 0))
x2.insert(1, cap(0, 1))
x2.insert(2, cap(0, 2))
x2.insert(3, cap(0, 3))
x2.insert(4, cap(0, 4))
x2.insert(5, cap(0, 5))
x2.insert(6, cap(0, 6))
x2.insert(7, cap(0, 7))

x3.insert(0, cap(0, 0))
x3.insert(1, cap(0, 1))
x3.insert(2, cap(0, 2))
x3.insert(3, cap(0, 3))
x3.insert(4, cap(0, 4))
x3.insert(5, cap(0, 5))
x3.insert(6, cap(0, 6))
x3.insert(7, cap(0, 7))

x4.insert(0, cap(0, 0))
x4.insert(1, cap(0, 1))
x4.insert(2, cap(0, 2))
x4.insert(3, cap(0, 3))
x4.insert(4, cap(0, 4))
x4.insert(5, cap(0, 5))
x4.insert(6, cap(0, 6))
x4.insert(7, cap(0, 7))

x5.insert(0, cap(0, 0))
x5.insert(1, cap(0, 1))
x5.insert(2, cap(0, 2))
x5.insert(3, cap(0, 3))
x5.insert(4, cap(0, 4))
x5.insert(5, cap(0, 5))
x5.insert(6, cap(0, 6))
x5.insert(7, cap(0, 7))

x6.insert(0, cap(0, 0))
x6.insert(1, cap(0, 1))
x6.insert(2, cap(0, 2))
x6.insert(3, cap(0, 3))
x6.insert(4, cap(0, 4))
x6.insert(5, cap(0, 5))
x6.insert(6, cap(0, 6))
x6.insert(7, cap(0, 7))

x7.insert(0, cap(0, 0))
x7.insert(1, cap(0, 1))
x7.insert(2, cap(0, 2))
x7.insert(3, cap(0, 3))
x7.insert(4, cap(0, 4))
x7.insert(5, cap(0, 5))
x7.insert(6, cap(0, 6))
x7.insert(7, cap(0, 7))

print " "
print " "
print " " #just to put a gap between each garden instance
print " "

#End Ascii
print "---------------------------------" #format is to round array values to zero decimal points on display without altering actual value
print "|" , format((x0[7]), '.0f') , "|" , format((x1[7]), '.0f') , "|" , format((x2[7]), '.0f') , "|" , format((x3[7]), '.0f') , "|" , format((x4[7]), '.0f') , "|" , format((x5[7]), '.0f') , "|" , format((x6[7]), '.0f') , "|" , format((x7[7]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[6]), '.0f') , "|" , format((x1[6]), '.0f') , "|" , format((x2[6]), '.0f') , "|" , format((x3[6]), '.0f') , "|" , format((x4[6]), '.0f') , "|" , format((x5[6]), '.0f') , "|" , format((x6[6]), '.0f') , "|" , format((x7[6]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[5]), '.0f') , "|" , format((x1[5]), '.0f') , "|" , format((x2[5]), '.0f') , "|" , format((x3[5]), '.0f') , "|" , format((x4[5]), '.0f') , "|" , format((x5[5]), '.0f') , "|" , format((x6[5]), '.0f') , "|" , format((x7[5]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[4]), '.0f') , "|" , format((x1[4]), '.0f') , "|" , format((x2[4]), '.0f') , "|" , format((x3[4]), '.0f') , "|" , format((x4[4]), '.0f') , "|" , format((x5[4]), '.0f') , "|" , format((x6[4]), '.0f') , "|" , format((x7[4]), '.0f') , "|       Garden after"
print "---------------------------------"
print "|" , format((x0[3]), '.0f') , "|" , format((x1[3]), '.0f') , "|" , format((x2[3]), '.0f') , "|" , format((x3[3]), '.0f') , "|" , format((x4[3]), '.0f') , "|" , format((x5[3]), '.0f') , "|" , format((x6[3]), '.0f') , "|" , format((x7[3]), '.0f') , "|       first turn"
print "---------------------------------"
print "|" , format((x0[2]), '.0f') , "|" , format((x1[2]), '.0f') , "|" , format((x2[2]), '.0f') , "|" , format((x3[2]), '.0f') , "|" , format((x4[2]), '.0f') , "|" , format((x5[2]), '.0f') , "|" , format((x6[2]), '.0f') , "|" , format((x7[2]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[1]), '.0f') , "|" , format((x1[1]), '.0f') , "|" , format((x2[1]), '.0f') , "|" , format((x3[1]), '.0f') , "|" , format((x4[1]), '.0f') , "|" , format((x5[1]), '.0f') , "|" , format((x6[1]), '.0f') , "|" , format((x7[1]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[0]), '.0f') , "|" , format((x1[0]), '.0f') , "|" , format((x2[0]), '.0f') , "|" , format((x3[0]), '.0f') , "|" , format((x4[0]), '.0f') , "|" , format((x5[0]), '.0f') , "|" , format((x6[0]), '.0f') , "|" , format((x7[0]), '.0f') , "|"
print "---------------------------------"

#Turn 2
x0.insert(0, cap(0, 0))
x0.insert(1, cap(0, 1))
x0.insert(2, cap(0, 2))
x0.insert(3, cap(0, 3))
x0.insert(4, cap(0, 4))
x0.insert(5, cap(0, 5))
x0.insert(6, cap(0, 6))
x0.insert(7, cap(0, 7))

x1.insert(0, cap(0, 0))
x1.insert(1, cap(0, 1))
x1.insert(2, cap(0, 2))
x1.insert(3, cap(0, 3))
x1.insert(4, cap(0, 4))
x1.insert(5, cap(0, 5))
x1.insert(6, cap(0, 6))
x1.insert(7, cap(0, 7))

x2.insert(0, cap(0, 0))
x2.insert(1, cap(0, 1))
x2.insert(2, cap(0, 2))
x2.insert(3, cap(0, 3))
x2.insert(4, cap(0, 4))
x2.insert(5, cap(0, 5))
x2.insert(6, cap(0, 6))
x2.insert(7, cap(0, 7))

x3.insert(0, cap(0, 0))
x3.insert(1, cap(0, 1))
x3.insert(2, cap(0, 2))
x3.insert(3, cap(0, 3))
x3.insert(4, cap(0, 4))
x3.insert(5, cap(0, 5))
x3.insert(6, cap(0, 6))
x3.insert(7, cap(0, 7))

x4.insert(0, cap(0, 0))
x4.insert(1, cap(0, 1))
x4.insert(2, cap(0, 2))
x4.insert(3, cap(0, 3))
x4.insert(4, cap(0, 4))
x4.insert(5, cap(0, 5))
x4.insert(6, cap(0, 6))
x4.insert(7, cap(0, 7))

x5.insert(0, cap(0, 0))
x5.insert(1, cap(0, 1))
x5.insert(2, cap(0, 2))
x5.insert(3, cap(0, 3))
x5.insert(4, cap(0, 4))
x5.insert(5, cap(0, 5))
x5.insert(6, cap(0, 6))
x5.insert(7, cap(0, 7))

x6.insert(0, cap(0, 0))
x6.insert(1, cap(0, 1))
x6.insert(2, cap(0, 2))
x6.insert(3, cap(0, 3))
x6.insert(4, cap(0, 4))
x6.insert(5, cap(0, 5))
x6.insert(6, cap(0, 6))
x6.insert(7, cap(0, 7))

x7.insert(0, cap(0, 0))
x7.insert(1, cap(0, 1))
x7.insert(2, cap(0, 2))
x7.insert(3, cap(0, 3))
x7.insert(4, cap(0, 4))
x7.insert(5, cap(0, 5))
x7.insert(6, cap(0, 6))
x7.insert(7, cap(0, 7))

print " "
print " "
print " "
print " "

#End Ascii
print "---------------------------------" #format is to round array values to zero decimal points on display without altering actual value
print "|" , format((x0[7]), '.0f') , "|" , format((x1[7]), '.0f') , "|" , format((x2[7]), '.0f') , "|" , format((x3[7]), '.0f') , "|" , format((x4[7]), '.0f') , "|" , format((x5[7]), '.0f') , "|" , format((x6[7]), '.0f') , "|" , format((x7[7]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[6]), '.0f') , "|" , format((x1[6]), '.0f') , "|" , format((x2[6]), '.0f') , "|" , format((x3[6]), '.0f') , "|" , format((x4[6]), '.0f') , "|" , format((x5[6]), '.0f') , "|" , format((x6[6]), '.0f') , "|" , format((x7[6]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[5]), '.0f') , "|" , format((x1[5]), '.0f') , "|" , format((x2[5]), '.0f') , "|" , format((x3[5]), '.0f') , "|" , format((x4[5]), '.0f') , "|" , format((x5[5]), '.0f') , "|" , format((x6[5]), '.0f') , "|" , format((x7[5]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[4]), '.0f') , "|" , format((x1[4]), '.0f') , "|" , format((x2[4]), '.0f') , "|" , format((x3[4]), '.0f') , "|" , format((x4[4]), '.0f') , "|" , format((x5[4]), '.0f') , "|" , format((x6[4]), '.0f') , "|" , format((x7[4]), '.0f') , "|       Garden after"
print "---------------------------------"
print "|" , format((x0[3]), '.0f') , "|" , format((x1[3]), '.0f') , "|" , format((x2[3]), '.0f') , "|" , format((x3[3]), '.0f') , "|" , format((x4[3]), '.0f') , "|" , format((x5[3]), '.0f') , "|" , format((x6[3]), '.0f') , "|" , format((x7[3]), '.0f') , "|       second turn"
print "---------------------------------"
print "|" , format((x0[2]), '.0f') , "|" , format((x1[2]), '.0f') , "|" , format((x2[2]), '.0f') , "|" , format((x3[2]), '.0f') , "|" , format((x4[2]), '.0f') , "|" , format((x5[2]), '.0f') , "|" , format((x6[2]), '.0f') , "|" , format((x7[2]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[1]), '.0f') , "|" , format((x1[1]), '.0f') , "|" , format((x2[1]), '.0f') , "|" , format((x3[1]), '.0f') , "|" , format((x4[1]), '.0f') , "|" , format((x5[1]), '.0f') , "|" , format((x6[1]), '.0f') , "|" , format((x7[1]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[0]), '.0f') , "|" , format((x1[0]), '.0f') , "|" , format((x2[0]), '.0f') , "|" , format((x3[0]), '.0f') , "|" , format((x4[0]), '.0f') , "|" , format((x5[0]), '.0f') , "|" , format((x6[0]), '.0f') , "|" , format((x7[0]), '.0f') , "|"
print "---------------------------------"

#Turn 3
x0.insert(0, cap(0, 0))
x0.insert(1, cap(0, 1))
x0.insert(2, cap(0, 2))
x0.insert(3, cap(0, 3))
x0.insert(4, cap(0, 4))
x0.insert(5, cap(0, 5))
x0.insert(6, cap(0, 6))
x0.insert(7, cap(0, 7))

x1.insert(0, cap(0, 0))
x1.insert(1, cap(0, 1))
x1.insert(2, cap(0, 2))
x1.insert(3, cap(0, 3))
x1.insert(4, cap(0, 4))
x1.insert(5, cap(0, 5))
x1.insert(6, cap(0, 6))
x1.insert(7, cap(0, 7))

x2.insert(0, cap(0, 0))
x2.insert(1, cap(0, 1))
x2.insert(2, cap(0, 2))
x2.insert(3, cap(0, 3))
x2.insert(4, cap(0, 4))
x2.insert(5, cap(0, 5))
x2.insert(6, cap(0, 6))
x2.insert(7, cap(0, 7))

x3.insert(0, cap(0, 0))
x3.insert(1, cap(0, 1))
x3.insert(2, cap(0, 2))
x3.insert(3, cap(0, 3))
x3.insert(4, cap(0, 4))
x3.insert(5, cap(0, 5))
x3.insert(6, cap(0, 6))
x3.insert(7, cap(0, 7))

x4.insert(0, cap(0, 0))
x4.insert(1, cap(0, 1))
x4.insert(2, cap(0, 2))
x4.insert(3, cap(0, 3))
x4.insert(4, cap(0, 4))
x4.insert(5, cap(0, 5))
x4.insert(6, cap(0, 6))
x4.insert(7, cap(0, 7))

x5.insert(0, cap(0, 0))
x5.insert(1, cap(0, 1))
x5.insert(2, cap(0, 2))
x5.insert(3, cap(0, 3))
x5.insert(4, cap(0, 4))
x5.insert(5, cap(0, 5))
x5.insert(6, cap(0, 6))
x5.insert(7, cap(0, 7))

x6.insert(0, cap(0, 0))
x6.insert(1, cap(0, 1))
x6.insert(2, cap(0, 2))
x6.insert(3, cap(0, 3))
x6.insert(4, cap(0, 4))
x6.insert(5, cap(0, 5))
x6.insert(6, cap(0, 6))
x6.insert(7, cap(0, 7))

x7.insert(0, cap(0, 0))
x7.insert(1, cap(0, 1))
x7.insert(2, cap(0, 2))
x7.insert(3, cap(0, 3))
x7.insert(4, cap(0, 4))
x7.insert(5, cap(0, 5))
x7.insert(6, cap(0, 6))
x7.insert(7, cap(0, 7))

print " "
print " "
print " "
print " "

#End Ascii
print "---------------------------------" #format is to round array values to zero decimal points on display without altering actual value
print "|" , format((x0[7]), '.0f') , "|" , format((x1[7]), '.0f') , "|" , format((x2[7]), '.0f') , "|" , format((x3[7]), '.0f') , "|" , format((x4[7]), '.0f') , "|" , format((x5[7]), '.0f') , "|" , format((x6[7]), '.0f') , "|" , format((x7[7]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[6]), '.0f') , "|" , format((x1[6]), '.0f') , "|" , format((x2[6]), '.0f') , "|" , format((x3[6]), '.0f') , "|" , format((x4[6]), '.0f') , "|" , format((x5[6]), '.0f') , "|" , format((x6[6]), '.0f') , "|" , format((x7[6]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[5]), '.0f') , "|" , format((x1[5]), '.0f') , "|" , format((x2[5]), '.0f') , "|" , format((x3[5]), '.0f') , "|" , format((x4[5]), '.0f') , "|" , format((x5[5]), '.0f') , "|" , format((x6[5]), '.0f') , "|" , format((x7[5]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[4]), '.0f') , "|" , format((x1[4]), '.0f') , "|" , format((x2[4]), '.0f') , "|" , format((x3[4]), '.0f') , "|" , format((x4[4]), '.0f') , "|" , format((x5[4]), '.0f') , "|" , format((x6[4]), '.0f') , "|" , format((x7[4]), '.0f') , "|       Garden after"
print "---------------------------------"
print "|" , format((x0[3]), '.0f') , "|" , format((x1[3]), '.0f') , "|" , format((x2[3]), '.0f') , "|" , format((x3[3]), '.0f') , "|" , format((x4[3]), '.0f') , "|" , format((x5[3]), '.0f') , "|" , format((x6[3]), '.0f') , "|" , format((x7[3]), '.0f') , "|       third turn"
print "---------------------------------"
print "|" , format((x0[2]), '.0f') , "|" , format((x1[2]), '.0f') , "|" , format((x2[2]), '.0f') , "|" , format((x3[2]), '.0f') , "|" , format((x4[2]), '.0f') , "|" , format((x5[2]), '.0f') , "|" , format((x6[2]), '.0f') , "|" , format((x7[2]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[1]), '.0f') , "|" , format((x1[1]), '.0f') , "|" , format((x2[1]), '.0f') , "|" , format((x3[1]), '.0f') , "|" , format((x4[1]), '.0f') , "|" , format((x5[1]), '.0f') , "|" , format((x6[1]), '.0f') , "|" , format((x7[1]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[0]), '.0f') , "|" , format((x1[0]), '.0f') , "|" , format((x2[0]), '.0f') , "|" , format((x3[0]), '.0f') , "|" , format((x4[0]), '.0f') , "|" , format((x5[0]), '.0f') , "|" , format((x6[0]), '.0f') , "|" , format((x7[0]), '.0f') , "|"
print "---------------------------------"

#Turn 4
x0.insert(0, cap(0, 0))
x0.insert(1, cap(0, 1))
x0.insert(2, cap(0, 2))
x0.insert(3, cap(0, 3))
x0.insert(4, cap(0, 4))
x0.insert(5, cap(0, 5))
x0.insert(6, cap(0, 6))
x0.insert(7, cap(0, 7))

x1.insert(0, cap(0, 0))
x1.insert(1, cap(0, 1))
x1.insert(2, cap(0, 2))
x1.insert(3, cap(0, 3))
x1.insert(4, cap(0, 4))
x1.insert(5, cap(0, 5))
x1.insert(6, cap(0, 6))
x1.insert(7, cap(0, 7))

x2.insert(0, cap(0, 0))
x2.insert(1, cap(0, 1))
x2.insert(2, cap(0, 2))
x2.insert(3, cap(0, 3))
x2.insert(4, cap(0, 4))
x2.insert(5, cap(0, 5))
x2.insert(6, cap(0, 6))
x2.insert(7, cap(0, 7))

x3.insert(0, cap(0, 0))
x3.insert(1, cap(0, 1))
x3.insert(2, cap(0, 2))
x3.insert(3, cap(0, 3))
x3.insert(4, cap(0, 4))
x3.insert(5, cap(0, 5))
x3.insert(6, cap(0, 6))
x3.insert(7, cap(0, 7))

x4.insert(0, cap(0, 0))
x4.insert(1, cap(0, 1))
x4.insert(2, cap(0, 2))
x4.insert(3, cap(0, 3))
x4.insert(4, cap(0, 4))
x4.insert(5, cap(0, 5))
x4.insert(6, cap(0, 6))
x4.insert(7, cap(0, 7))

x5.insert(0, cap(0, 0))
x5.insert(1, cap(0, 1))
x5.insert(2, cap(0, 2))
x5.insert(3, cap(0, 3))
x5.insert(4, cap(0, 4))
x5.insert(5, cap(0, 5))
x5.insert(6, cap(0, 6))
x5.insert(7, cap(0, 7))

x6.insert(0, cap(0, 0))
x6.insert(1, cap(0, 1))
x6.insert(2, cap(0, 2))
x6.insert(3, cap(0, 3))
x6.insert(4, cap(0, 4))
x6.insert(5, cap(0, 5))
x6.insert(6, cap(0, 6))
x6.insert(7, cap(0, 7))

x7.insert(0, cap(0, 0))
x7.insert(1, cap(0, 1))
x7.insert(2, cap(0, 2))
x7.insert(3, cap(0, 3))
x7.insert(4, cap(0, 4))
x7.insert(5, cap(0, 5))
x7.insert(6, cap(0, 6))
x7.insert(7, cap(0, 7))

print " "
print " "
print " "
print " "

#End Ascii
print "---------------------------------" #format is to round array values to zero decimal points on display without altering actual value
print "|" , format((x0[7]), '.0f') , "|" , format((x1[7]), '.0f') , "|" , format((x2[7]), '.0f') , "|" , format((x3[7]), '.0f') , "|" , format((x4[7]), '.0f') , "|" , format((x5[7]), '.0f') , "|" , format((x6[7]), '.0f') , "|" , format((x7[7]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[6]), '.0f') , "|" , format((x1[6]), '.0f') , "|" , format((x2[6]), '.0f') , "|" , format((x3[6]), '.0f') , "|" , format((x4[6]), '.0f') , "|" , format((x5[6]), '.0f') , "|" , format((x6[6]), '.0f') , "|" , format((x7[6]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[5]), '.0f') , "|" , format((x1[5]), '.0f') , "|" , format((x2[5]), '.0f') , "|" , format((x3[5]), '.0f') , "|" , format((x4[5]), '.0f') , "|" , format((x5[5]), '.0f') , "|" , format((x6[5]), '.0f') , "|" , format((x7[5]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[4]), '.0f') , "|" , format((x1[4]), '.0f') , "|" , format((x2[4]), '.0f') , "|" , format((x3[4]), '.0f') , "|" , format((x4[4]), '.0f') , "|" , format((x5[4]), '.0f') , "|" , format((x6[4]), '.0f') , "|" , format((x7[4]), '.0f') , "|       Garden after"
print "---------------------------------"
print "|" , format((x0[3]), '.0f') , "|" , format((x1[3]), '.0f') , "|" , format((x2[3]), '.0f') , "|" , format((x3[3]), '.0f') , "|" , format((x4[3]), '.0f') , "|" , format((x5[3]), '.0f') , "|" , format((x6[3]), '.0f') , "|" , format((x7[3]), '.0f') , "|       fourth turn"
print "---------------------------------"
print "|" , format((x0[2]), '.0f') , "|" , format((x1[2]), '.0f') , "|" , format((x2[2]), '.0f') , "|" , format((x3[2]), '.0f') , "|" , format((x4[2]), '.0f') , "|" , format((x5[2]), '.0f') , "|" , format((x6[2]), '.0f') , "|" , format((x7[2]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[1]), '.0f') , "|" , format((x1[1]), '.0f') , "|" , format((x2[1]), '.0f') , "|" , format((x3[1]), '.0f') , "|" , format((x4[1]), '.0f') , "|" , format((x5[1]), '.0f') , "|" , format((x6[1]), '.0f') , "|" , format((x7[1]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[0]), '.0f') , "|" , format((x1[0]), '.0f') , "|" , format((x2[0]), '.0f') , "|" , format((x3[0]), '.0f') , "|" , format((x4[0]), '.0f') , "|" , format((x5[0]), '.0f') , "|" , format((x6[0]), '.0f') , "|" , format((x7[0]), '.0f') , "|"
print "---------------------------------"

#Turn 5
x0.insert(0, cap(0, 0))
x0.insert(1, cap(0, 1))
x0.insert(2, cap(0, 2))
x0.insert(3, cap(0, 3))
x0.insert(4, cap(0, 4))
x0.insert(5, cap(0, 5))
x0.insert(6, cap(0, 6))
x0.insert(7, cap(0, 7))

x1.insert(0, cap(0, 0))
x1.insert(1, cap(0, 1))
x1.insert(2, cap(0, 2))
x1.insert(3, cap(0, 3))
x1.insert(4, cap(0, 4))
x1.insert(5, cap(0, 5))
x1.insert(6, cap(0, 6))
x1.insert(7, cap(0, 7))

x2.insert(0, cap(0, 0))
x2.insert(1, cap(0, 1))
x2.insert(2, cap(0, 2))
x2.insert(3, cap(0, 3))
x2.insert(4, cap(0, 4))
x2.insert(5, cap(0, 5))
x2.insert(6, cap(0, 6))
x2.insert(7, cap(0, 7))

x3.insert(0, cap(0, 0))
x3.insert(1, cap(0, 1))
x3.insert(2, cap(0, 2))
x3.insert(3, cap(0, 3))
x3.insert(4, cap(0, 4))
x3.insert(5, cap(0, 5))
x3.insert(6, cap(0, 6))
x3.insert(7, cap(0, 7))

x4.insert(0, cap(0, 0))
x4.insert(1, cap(0, 1))
x4.insert(2, cap(0, 2))
x4.insert(3, cap(0, 3))
x4.insert(4, cap(0, 4))
x4.insert(5, cap(0, 5))
x4.insert(6, cap(0, 6))
x4.insert(7, cap(0, 7))

x5.insert(0, cap(0, 0))
x5.insert(1, cap(0, 1))
x5.insert(2, cap(0, 2))
x5.insert(3, cap(0, 3))
x5.insert(4, cap(0, 4))
x5.insert(5, cap(0, 5))
x5.insert(6, cap(0, 6))
x5.insert(7, cap(0, 7))

x6.insert(0, cap(0, 0))
x6.insert(1, cap(0, 1))
x6.insert(2, cap(0, 2))
x6.insert(3, cap(0, 3))
x6.insert(4, cap(0, 4))
x6.insert(5, cap(0, 5))
x6.insert(6, cap(0, 6))
x6.insert(7, cap(0, 7))

x7.insert(0, cap(0, 0))
x7.insert(1, cap(0, 1))
x7.insert(2, cap(0, 2))
x7.insert(3, cap(0, 3))
x7.insert(4, cap(0, 4))
x7.insert(5, cap(0, 5))
x7.insert(6, cap(0, 6))
x7.insert(7, cap(0, 7))

print " "
print " "
print " "
print " "

#End Ascii
print "---------------------------------" #format is to round array values to zero decimal points on display without altering actual value
print "|" , format((x0[7]), '.0f') , "|" , format((x1[7]), '.0f') , "|" , format((x2[7]), '.0f') , "|" , format((x3[7]), '.0f') , "|" , format((x4[7]), '.0f') , "|" , format((x5[7]), '.0f') , "|" , format((x6[7]), '.0f') , "|" , format((x7[7]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[6]), '.0f') , "|" , format((x1[6]), '.0f') , "|" , format((x2[6]), '.0f') , "|" , format((x3[6]), '.0f') , "|" , format((x4[6]), '.0f') , "|" , format((x5[6]), '.0f') , "|" , format((x6[6]), '.0f') , "|" , format((x7[6]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[5]), '.0f') , "|" , format((x1[5]), '.0f') , "|" , format((x2[5]), '.0f') , "|" , format((x3[5]), '.0f') , "|" , format((x4[5]), '.0f') , "|" , format((x5[5]), '.0f') , "|" , format((x6[5]), '.0f') , "|" , format((x7[5]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[4]), '.0f') , "|" , format((x1[4]), '.0f') , "|" , format((x2[4]), '.0f') , "|" , format((x3[4]), '.0f') , "|" , format((x4[4]), '.0f') , "|" , format((x5[4]), '.0f') , "|" , format((x6[4]), '.0f') , "|" , format((x7[4]), '.0f') , "|       Garden after"
print "---------------------------------"
print "|" , format((x0[3]), '.0f') , "|" , format((x1[3]), '.0f') , "|" , format((x2[3]), '.0f') , "|" , format((x3[3]), '.0f') , "|" , format((x4[3]), '.0f') , "|" , format((x5[3]), '.0f') , "|" , format((x6[3]), '.0f') , "|" , format((x7[3]), '.0f') , "|       fifth turn"
print "---------------------------------"
print "|" , format((x0[2]), '.0f') , "|" , format((x1[2]), '.0f') , "|" , format((x2[2]), '.0f') , "|" , format((x3[2]), '.0f') , "|" , format((x4[2]), '.0f') , "|" , format((x5[2]), '.0f') , "|" , format((x6[2]), '.0f') , "|" , format((x7[2]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[1]), '.0f') , "|" , format((x1[1]), '.0f') , "|" , format((x2[1]), '.0f') , "|" , format((x3[1]), '.0f') , "|" , format((x4[1]), '.0f') , "|" , format((x5[1]), '.0f') , "|" , format((x6[1]), '.0f') , "|" , format((x7[1]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[0]), '.0f') , "|" , format((x1[0]), '.0f') , "|" , format((x2[0]), '.0f') , "|" , format((x3[0]), '.0f') , "|" , format((x4[0]), '.0f') , "|" , format((x5[0]), '.0f') , "|" , format((x6[0]), '.0f') , "|" , format((x7[0]), '.0f') , "|"
print "---------------------------------"

#Turn 5
x0.insert(0, cap(0, 0))
x0.insert(1, cap(0, 1))
x0.insert(2, cap(0, 2))
x0.insert(3, cap(0, 3))
x0.insert(4, cap(0, 4))
x0.insert(5, cap(0, 5))
x0.insert(6, cap(0, 6))
x0.insert(7, cap(0, 7))

x1.insert(0, cap(0, 0))
x1.insert(1, cap(0, 1))
x1.insert(2, cap(0, 2))
x1.insert(3, cap(0, 3))
x1.insert(4, cap(0, 4))
x1.insert(5, cap(0, 5))
x1.insert(6, cap(0, 6))
x1.insert(7, cap(0, 7))

x2.insert(0, cap(0, 0))
x2.insert(1, cap(0, 1))
x2.insert(2, cap(0, 2))
x2.insert(3, cap(0, 3))
x2.insert(4, cap(0, 4))
x2.insert(5, cap(0, 5))
x2.insert(6, cap(0, 6))
x2.insert(7, cap(0, 7))

x3.insert(0, cap(0, 0))
x3.insert(1, cap(0, 1))
x3.insert(2, cap(0, 2))
x3.insert(3, cap(0, 3))
x3.insert(4, cap(0, 4))
x3.insert(5, cap(0, 5))
x3.insert(6, cap(0, 6))
x3.insert(7, cap(0, 7))

x4.insert(0, cap(0, 0))
x4.insert(1, cap(0, 1))
x4.insert(2, cap(0, 2))
x4.insert(3, cap(0, 3))
x4.insert(4, cap(0, 4))
x4.insert(5, cap(0, 5))
x4.insert(6, cap(0, 6))
x4.insert(7, cap(0, 7))

x5.insert(0, cap(0, 0))
x5.insert(1, cap(0, 1))
x5.insert(2, cap(0, 2))
x5.insert(3, cap(0, 3))
x5.insert(4, cap(0, 4))
x5.insert(5, cap(0, 5))
x5.insert(6, cap(0, 6))
x5.insert(7, cap(0, 7))

x6.insert(0, cap(0, 0))
x6.insert(1, cap(0, 1))
x6.insert(2, cap(0, 2))
x6.insert(3, cap(0, 3))
x6.insert(4, cap(0, 4))
x6.insert(5, cap(0, 5))
x6.insert(6, cap(0, 6))
x6.insert(7, cap(0, 7))

x7.insert(0, cap(0, 0))
x7.insert(1, cap(0, 1))
x7.insert(2, cap(0, 2))
x7.insert(3, cap(0, 3))
x7.insert(4, cap(0, 4))
x7.insert(5, cap(0, 5))
x7.insert(6, cap(0, 6))
x7.insert(7, cap(0, 7))

print " "
print " "
print " "
print " "

#End Ascii
print "---------------------------------" #format is to round array values to zero decimal points on display without altering actual value
print "|" , format((x0[7]), '.0f') , "|" , format((x1[7]), '.0f') , "|" , format((x2[7]), '.0f') , "|" , format((x3[7]), '.0f') , "|" , format((x4[7]), '.0f') , "|" , format((x5[7]), '.0f') , "|" , format((x6[7]), '.0f') , "|" , format((x7[7]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[6]), '.0f') , "|" , format((x1[6]), '.0f') , "|" , format((x2[6]), '.0f') , "|" , format((x3[6]), '.0f') , "|" , format((x4[6]), '.0f') , "|" , format((x5[6]), '.0f') , "|" , format((x6[6]), '.0f') , "|" , format((x7[6]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[5]), '.0f') , "|" , format((x1[5]), '.0f') , "|" , format((x2[5]), '.0f') , "|" , format((x3[5]), '.0f') , "|" , format((x4[5]), '.0f') , "|" , format((x5[5]), '.0f') , "|" , format((x6[5]), '.0f') , "|" , format((x7[5]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[4]), '.0f') , "|" , format((x1[4]), '.0f') , "|" , format((x2[4]), '.0f') , "|" , format((x3[4]), '.0f') , "|" , format((x4[4]), '.0f') , "|" , format((x5[4]), '.0f') , "|" , format((x6[4]), '.0f') , "|" , format((x7[4]), '.0f') , "|       Garden after"
print "---------------------------------"
print "|" , format((x0[3]), '.0f') , "|" , format((x1[3]), '.0f') , "|" , format((x2[3]), '.0f') , "|" , format((x3[3]), '.0f') , "|" , format((x4[3]), '.0f') , "|" , format((x5[3]), '.0f') , "|" , format((x6[3]), '.0f') , "|" , format((x7[3]), '.0f') , "|       sixth turn"
print "---------------------------------"
print "|" , format((x0[2]), '.0f') , "|" , format((x1[2]), '.0f') , "|" , format((x2[2]), '.0f') , "|" , format((x3[2]), '.0f') , "|" , format((x4[2]), '.0f') , "|" , format((x5[2]), '.0f') , "|" , format((x6[2]), '.0f') , "|" , format((x7[2]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[1]), '.0f') , "|" , format((x1[1]), '.0f') , "|" , format((x2[1]), '.0f') , "|" , format((x3[1]), '.0f') , "|" , format((x4[1]), '.0f') , "|" , format((x5[1]), '.0f') , "|" , format((x6[1]), '.0f') , "|" , format((x7[1]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[0]), '.0f') , "|" , format((x1[0]), '.0f') , "|" , format((x2[0]), '.0f') , "|" , format((x3[0]), '.0f') , "|" , format((x4[0]), '.0f') , "|" , format((x5[0]), '.0f') , "|" , format((x6[0]), '.0f') , "|" , format((x7[0]), '.0f') , "|"
print "---------------------------------"

#Turn 5
x0.insert(0, cap(0, 0))
x0.insert(1, cap(0, 1))
x0.insert(2, cap(0, 2))
x0.insert(3, cap(0, 3))
x0.insert(4, cap(0, 4))
x0.insert(5, cap(0, 5))
x0.insert(6, cap(0, 6))
x0.insert(7, cap(0, 7))

x1.insert(0, cap(0, 0))
x1.insert(1, cap(0, 1))
x1.insert(2, cap(0, 2))
x1.insert(3, cap(0, 3))
x1.insert(4, cap(0, 4))
x1.insert(5, cap(0, 5))
x1.insert(6, cap(0, 6))
x1.insert(7, cap(0, 7))

x2.insert(0, cap(0, 0))
x2.insert(1, cap(0, 1))
x2.insert(2, cap(0, 2))
x2.insert(3, cap(0, 3))
x2.insert(4, cap(0, 4))
x2.insert(5, cap(0, 5))
x2.insert(6, cap(0, 6))
x2.insert(7, cap(0, 7))

x3.insert(0, cap(0, 0))
x3.insert(1, cap(0, 1))
x3.insert(2, cap(0, 2))
x3.insert(3, cap(0, 3))
x3.insert(4, cap(0, 4))
x3.insert(5, cap(0, 5))
x3.insert(6, cap(0, 6))
x3.insert(7, cap(0, 7))

x4.insert(0, cap(0, 0))
x4.insert(1, cap(0, 1))
x4.insert(2, cap(0, 2))
x4.insert(3, cap(0, 3))
x4.insert(4, cap(0, 4))
x4.insert(5, cap(0, 5))
x4.insert(6, cap(0, 6))
x4.insert(7, cap(0, 7))

x5.insert(0, cap(0, 0))
x5.insert(1, cap(0, 1))
x5.insert(2, cap(0, 2))
x5.insert(3, cap(0, 3))
x5.insert(4, cap(0, 4))
x5.insert(5, cap(0, 5))
x5.insert(6, cap(0, 6))
x5.insert(7, cap(0, 7))

x6.insert(0, cap(0, 0))
x6.insert(1, cap(0, 1))
x6.insert(2, cap(0, 2))
x6.insert(3, cap(0, 3))
x6.insert(4, cap(0, 4))
x6.insert(5, cap(0, 5))
x6.insert(6, cap(0, 6))
x6.insert(7, cap(0, 7))

x7.insert(0, cap(0, 0))
x7.insert(1, cap(0, 1))
x7.insert(2, cap(0, 2))
x7.insert(3, cap(0, 3))
x7.insert(4, cap(0, 4))
x7.insert(5, cap(0, 5))
x7.insert(6, cap(0, 6))
x7.insert(7, cap(0, 7))

print " "
print " "
print " "
print " "

#End Ascii
print "---------------------------------" #format is to round array values to zero decimal points on display without altering actual value
print "|" , format((x0[7]), '.0f') , "|" , format((x1[7]), '.0f') , "|" , format((x2[7]), '.0f') , "|" , format((x3[7]), '.0f') , "|" , format((x4[7]), '.0f') , "|" , format((x5[7]), '.0f') , "|" , format((x6[7]), '.0f') , "|" , format((x7[7]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[6]), '.0f') , "|" , format((x1[6]), '.0f') , "|" , format((x2[6]), '.0f') , "|" , format((x3[6]), '.0f') , "|" , format((x4[6]), '.0f') , "|" , format((x5[6]), '.0f') , "|" , format((x6[6]), '.0f') , "|" , format((x7[6]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[5]), '.0f') , "|" , format((x1[5]), '.0f') , "|" , format((x2[5]), '.0f') , "|" , format((x3[5]), '.0f') , "|" , format((x4[5]), '.0f') , "|" , format((x5[5]), '.0f') , "|" , format((x6[5]), '.0f') , "|" , format((x7[5]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[4]), '.0f') , "|" , format((x1[4]), '.0f') , "|" , format((x2[4]), '.0f') , "|" , format((x3[4]), '.0f') , "|" , format((x4[4]), '.0f') , "|" , format((x5[4]), '.0f') , "|" , format((x6[4]), '.0f') , "|" , format((x7[4]), '.0f') , "|       Garden after"
print "---------------------------------"
print "|" , format((x0[3]), '.0f') , "|" , format((x1[3]), '.0f') , "|" , format((x2[3]), '.0f') , "|" , format((x3[3]), '.0f') , "|" , format((x4[3]), '.0f') , "|" , format((x5[3]), '.0f') , "|" , format((x6[3]), '.0f') , "|" , format((x7[3]), '.0f') , "|       seventh turn"
print "---------------------------------"
print "|" , format((x0[2]), '.0f') , "|" , format((x1[2]), '.0f') , "|" , format((x2[2]), '.0f') , "|" , format((x3[2]), '.0f') , "|" , format((x4[2]), '.0f') , "|" , format((x5[2]), '.0f') , "|" , format((x6[2]), '.0f') , "|" , format((x7[2]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[1]), '.0f') , "|" , format((x1[1]), '.0f') , "|" , format((x2[1]), '.0f') , "|" , format((x3[1]), '.0f') , "|" , format((x4[1]), '.0f') , "|" , format((x5[1]), '.0f') , "|" , format((x6[1]), '.0f') , "|" , format((x7[1]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[0]), '.0f') , "|" , format((x1[0]), '.0f') , "|" , format((x2[0]), '.0f') , "|" , format((x3[0]), '.0f') , "|" , format((x4[0]), '.0f') , "|" , format((x5[0]), '.0f') , "|" , format((x6[0]), '.0f') , "|" , format((x7[0]), '.0f') , "|"
print "---------------------------------"

#Turn 5
x0.insert(0, cap(0, 0))
x0.insert(1, cap(0, 1))
x0.insert(2, cap(0, 2))
x0.insert(3, cap(0, 3))
x0.insert(4, cap(0, 4))
x0.insert(5, cap(0, 5))
x0.insert(6, cap(0, 6))
x0.insert(7, cap(0, 7))

x1.insert(0, cap(0, 0))
x1.insert(1, cap(0, 1))
x1.insert(2, cap(0, 2))
x1.insert(3, cap(0, 3))
x1.insert(4, cap(0, 4))
x1.insert(5, cap(0, 5))
x1.insert(6, cap(0, 6))
x1.insert(7, cap(0, 7))

x2.insert(0, cap(0, 0))
x2.insert(1, cap(0, 1))
x2.insert(2, cap(0, 2))
x2.insert(3, cap(0, 3))
x2.insert(4, cap(0, 4))
x2.insert(5, cap(0, 5))
x2.insert(6, cap(0, 6))
x2.insert(7, cap(0, 7))

x3.insert(0, cap(0, 0))
x3.insert(1, cap(0, 1))
x3.insert(2, cap(0, 2))
x3.insert(3, cap(0, 3))
x3.insert(4, cap(0, 4))
x3.insert(5, cap(0, 5))
x3.insert(6, cap(0, 6))
x3.insert(7, cap(0, 7))

x4.insert(0, cap(0, 0))
x4.insert(1, cap(0, 1))
x4.insert(2, cap(0, 2))
x4.insert(3, cap(0, 3))
x4.insert(4, cap(0, 4))
x4.insert(5, cap(0, 5))
x4.insert(6, cap(0, 6))
x4.insert(7, cap(0, 7))

x5.insert(0, cap(0, 0))
x5.insert(1, cap(0, 1))
x5.insert(2, cap(0, 2))
x5.insert(3, cap(0, 3))
x5.insert(4, cap(0, 4))
x5.insert(5, cap(0, 5))
x5.insert(6, cap(0, 6))
x5.insert(7, cap(0, 7))

x6.insert(0, cap(0, 0))
x6.insert(1, cap(0, 1))
x6.insert(2, cap(0, 2))
x6.insert(3, cap(0, 3))
x6.insert(4, cap(0, 4))
x6.insert(5, cap(0, 5))
x6.insert(6, cap(0, 6))
x6.insert(7, cap(0, 7))

x7.insert(0, cap(0, 0))
x7.insert(1, cap(0, 1))
x7.insert(2, cap(0, 2))
x7.insert(3, cap(0, 3))
x7.insert(4, cap(0, 4))
x7.insert(5, cap(0, 5))
x7.insert(6, cap(0, 6))
x7.insert(7, cap(0, 7))

print " "
print " "
print " "
print " "

#End Ascii
print "---------------------------------" #format is to round array values to zero decimal points on display without altering actual value
print "|" , format((x0[7]), '.0f') , "|" , format((x1[7]), '.0f') , "|" , format((x2[7]), '.0f') , "|" , format((x3[7]), '.0f') , "|" , format((x4[7]), '.0f') , "|" , format((x5[7]), '.0f') , "|" , format((x6[7]), '.0f') , "|" , format((x7[7]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[6]), '.0f') , "|" , format((x1[6]), '.0f') , "|" , format((x2[6]), '.0f') , "|" , format((x3[6]), '.0f') , "|" , format((x4[6]), '.0f') , "|" , format((x5[6]), '.0f') , "|" , format((x6[6]), '.0f') , "|" , format((x7[6]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[5]), '.0f') , "|" , format((x1[5]), '.0f') , "|" , format((x2[5]), '.0f') , "|" , format((x3[5]), '.0f') , "|" , format((x4[5]), '.0f') , "|" , format((x5[5]), '.0f') , "|" , format((x6[5]), '.0f') , "|" , format((x7[5]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[4]), '.0f') , "|" , format((x1[4]), '.0f') , "|" , format((x2[4]), '.0f') , "|" , format((x3[4]), '.0f') , "|" , format((x4[4]), '.0f') , "|" , format((x5[4]), '.0f') , "|" , format((x6[4]), '.0f') , "|" , format((x7[4]), '.0f') , "|       Garden after"
print "---------------------------------"
print "|" , format((x0[3]), '.0f') , "|" , format((x1[3]), '.0f') , "|" , format((x2[3]), '.0f') , "|" , format((x3[3]), '.0f') , "|" , format((x4[3]), '.0f') , "|" , format((x5[3]), '.0f') , "|" , format((x6[3]), '.0f') , "|" , format((x7[3]), '.0f') , "|       eighth turn"
print "---------------------------------"
print "|" , format((x0[2]), '.0f') , "|" , format((x1[2]), '.0f') , "|" , format((x2[2]), '.0f') , "|" , format((x3[2]), '.0f') , "|" , format((x4[2]), '.0f') , "|" , format((x5[2]), '.0f') , "|" , format((x6[2]), '.0f') , "|" , format((x7[2]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[1]), '.0f') , "|" , format((x1[1]), '.0f') , "|" , format((x2[1]), '.0f') , "|" , format((x3[1]), '.0f') , "|" , format((x4[1]), '.0f') , "|" , format((x5[1]), '.0f') , "|" , format((x6[1]), '.0f') , "|" , format((x7[1]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[0]), '.0f') , "|" , format((x1[0]), '.0f') , "|" , format((x2[0]), '.0f') , "|" , format((x3[0]), '.0f') , "|" , format((x4[0]), '.0f') , "|" , format((x5[0]), '.0f') , "|" , format((x6[0]), '.0f') , "|" , format((x7[0]), '.0f') , "|"
print "---------------------------------"

#Turn 5
x0.insert(0, cap(0, 0))
x0.insert(1, cap(0, 1))
x0.insert(2, cap(0, 2))
x0.insert(3, cap(0, 3))
x0.insert(4, cap(0, 4))
x0.insert(5, cap(0, 5))
x0.insert(6, cap(0, 6))
x0.insert(7, cap(0, 7))

x1.insert(0, cap(0, 0))
x1.insert(1, cap(0, 1))
x1.insert(2, cap(0, 2))
x1.insert(3, cap(0, 3))
x1.insert(4, cap(0, 4))
x1.insert(5, cap(0, 5))
x1.insert(6, cap(0, 6))
x1.insert(7, cap(0, 7))

x2.insert(0, cap(0, 0))
x2.insert(1, cap(0, 1))
x2.insert(2, cap(0, 2))
x2.insert(3, cap(0, 3))
x2.insert(4, cap(0, 4))
x2.insert(5, cap(0, 5))
x2.insert(6, cap(0, 6))
x2.insert(7, cap(0, 7))

x3.insert(0, cap(0, 0))
x3.insert(1, cap(0, 1))
x3.insert(2, cap(0, 2))
x3.insert(3, cap(0, 3))
x3.insert(4, cap(0, 4))
x3.insert(5, cap(0, 5))
x3.insert(6, cap(0, 6))
x3.insert(7, cap(0, 7))

x4.insert(0, cap(0, 0))
x4.insert(1, cap(0, 1))
x4.insert(2, cap(0, 2))
x4.insert(3, cap(0, 3))
x4.insert(4, cap(0, 4))
x4.insert(5, cap(0, 5))
x4.insert(6, cap(0, 6))
x4.insert(7, cap(0, 7))

x5.insert(0, cap(0, 0))
x5.insert(1, cap(0, 1))
x5.insert(2, cap(0, 2))
x5.insert(3, cap(0, 3))
x5.insert(4, cap(0, 4))
x5.insert(5, cap(0, 5))
x5.insert(6, cap(0, 6))
x5.insert(7, cap(0, 7))

x6.insert(0, cap(0, 0))
x6.insert(1, cap(0, 1))
x6.insert(2, cap(0, 2))
x6.insert(3, cap(0, 3))
x6.insert(4, cap(0, 4))
x6.insert(5, cap(0, 5))
x6.insert(6, cap(0, 6))
x6.insert(7, cap(0, 7))

x7.insert(0, cap(0, 0))
x7.insert(1, cap(0, 1))
x7.insert(2, cap(0, 2))
x7.insert(3, cap(0, 3))
x7.insert(4, cap(0, 4))
x7.insert(5, cap(0, 5))
x7.insert(6, cap(0, 6))
x7.insert(7, cap(0, 7))

print " "
print " "
print " "
print " "

#End Ascii
print "---------------------------------" #format is to round array values to zero decimal points on display without altering actual value
print "|" , format((x0[7]), '.0f') , "|" , format((x1[7]), '.0f') , "|" , format((x2[7]), '.0f') , "|" , format((x3[7]), '.0f') , "|" , format((x4[7]), '.0f') , "|" , format((x5[7]), '.0f') , "|" , format((x6[7]), '.0f') , "|" , format((x7[7]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[6]), '.0f') , "|" , format((x1[6]), '.0f') , "|" , format((x2[6]), '.0f') , "|" , format((x3[6]), '.0f') , "|" , format((x4[6]), '.0f') , "|" , format((x5[6]), '.0f') , "|" , format((x6[6]), '.0f') , "|" , format((x7[6]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[5]), '.0f') , "|" , format((x1[5]), '.0f') , "|" , format((x2[5]), '.0f') , "|" , format((x3[5]), '.0f') , "|" , format((x4[5]), '.0f') , "|" , format((x5[5]), '.0f') , "|" , format((x6[5]), '.0f') , "|" , format((x7[5]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[4]), '.0f') , "|" , format((x1[4]), '.0f') , "|" , format((x2[4]), '.0f') , "|" , format((x3[4]), '.0f') , "|" , format((x4[4]), '.0f') , "|" , format((x5[4]), '.0f') , "|" , format((x6[4]), '.0f') , "|" , format((x7[4]), '.0f') , "|       Garden after"
print "---------------------------------"
print "|" , format((x0[3]), '.0f') , "|" , format((x1[3]), '.0f') , "|" , format((x2[3]), '.0f') , "|" , format((x3[3]), '.0f') , "|" , format((x4[3]), '.0f') , "|" , format((x5[3]), '.0f') , "|" , format((x6[3]), '.0f') , "|" , format((x7[3]), '.0f') , "|       ninth turn"
print "---------------------------------"
print "|" , format((x0[2]), '.0f') , "|" , format((x1[2]), '.0f') , "|" , format((x2[2]), '.0f') , "|" , format((x3[2]), '.0f') , "|" , format((x4[2]), '.0f') , "|" , format((x5[2]), '.0f') , "|" , format((x6[2]), '.0f') , "|" , format((x7[2]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[1]), '.0f') , "|" , format((x1[1]), '.0f') , "|" , format((x2[1]), '.0f') , "|" , format((x3[1]), '.0f') , "|" , format((x4[1]), '.0f') , "|" , format((x5[1]), '.0f') , "|" , format((x6[1]), '.0f') , "|" , format((x7[1]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[0]), '.0f') , "|" , format((x1[0]), '.0f') , "|" , format((x2[0]), '.0f') , "|" , format((x3[0]), '.0f') , "|" , format((x4[0]), '.0f') , "|" , format((x5[0]), '.0f') , "|" , format((x6[0]), '.0f') , "|" , format((x7[0]), '.0f') , "|"
print "---------------------------------"

#Turn 5
x0.insert(0, cap(0, 0))
x0.insert(1, cap(0, 1))
x0.insert(2, cap(0, 2))
x0.insert(3, cap(0, 3))
x0.insert(4, cap(0, 4))
x0.insert(5, cap(0, 5))
x0.insert(6, cap(0, 6))
x0.insert(7, cap(0, 7))

x1.insert(0, cap(0, 0))
x1.insert(1, cap(0, 1))
x1.insert(2, cap(0, 2))
x1.insert(3, cap(0, 3))
x1.insert(4, cap(0, 4))
x1.insert(5, cap(0, 5))
x1.insert(6, cap(0, 6))
x1.insert(7, cap(0, 7))

x2.insert(0, cap(0, 0))
x2.insert(1, cap(0, 1))
x2.insert(2, cap(0, 2))
x2.insert(3, cap(0, 3))
x2.insert(4, cap(0, 4))
x2.insert(5, cap(0, 5))
x2.insert(6, cap(0, 6))
x2.insert(7, cap(0, 7))

x3.insert(0, cap(0, 0))
x3.insert(1, cap(0, 1))
x3.insert(2, cap(0, 2))
x3.insert(3, cap(0, 3))
x3.insert(4, cap(0, 4))
x3.insert(5, cap(0, 5))
x3.insert(6, cap(0, 6))
x3.insert(7, cap(0, 7))

x4.insert(0, cap(0, 0))
x4.insert(1, cap(0, 1))
x4.insert(2, cap(0, 2))
x4.insert(3, cap(0, 3))
x4.insert(4, cap(0, 4))
x4.insert(5, cap(0, 5))
x4.insert(6, cap(0, 6))
x4.insert(7, cap(0, 7))

x5.insert(0, cap(0, 0))
x5.insert(1, cap(0, 1))
x5.insert(2, cap(0, 2))
x5.insert(3, cap(0, 3))
x5.insert(4, cap(0, 4))
x5.insert(5, cap(0, 5))
x5.insert(6, cap(0, 6))
x5.insert(7, cap(0, 7))

x6.insert(0, cap(0, 0))
x6.insert(1, cap(0, 1))
x6.insert(2, cap(0, 2))
x6.insert(3, cap(0, 3))
x6.insert(4, cap(0, 4))
x6.insert(5, cap(0, 5))
x6.insert(6, cap(0, 6))
x6.insert(7, cap(0, 7))

x7.insert(0, cap(0, 0))
x7.insert(1, cap(0, 1))
x7.insert(2, cap(0, 2))
x7.insert(3, cap(0, 3))
x7.insert(4, cap(0, 4))
x7.insert(5, cap(0, 5))
x7.insert(6, cap(0, 6))
x7.insert(7, cap(0, 7))

print " "
print " "
print " "
print " "

#End Ascii
print "---------------------------------" #format is to round array values to zero decimal points on display without altering actual value
print "|" , format((x0[7]), '.0f') , "|" , format((x1[7]), '.0f') , "|" , format((x2[7]), '.0f') , "|" , format((x3[7]), '.0f') , "|" , format((x4[7]), '.0f') , "|" , format((x5[7]), '.0f') , "|" , format((x6[7]), '.0f') , "|" , format((x7[7]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[6]), '.0f') , "|" , format((x1[6]), '.0f') , "|" , format((x2[6]), '.0f') , "|" , format((x3[6]), '.0f') , "|" , format((x4[6]), '.0f') , "|" , format((x5[6]), '.0f') , "|" , format((x6[6]), '.0f') , "|" , format((x7[6]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[5]), '.0f') , "|" , format((x1[5]), '.0f') , "|" , format((x2[5]), '.0f') , "|" , format((x3[5]), '.0f') , "|" , format((x4[5]), '.0f') , "|" , format((x5[5]), '.0f') , "|" , format((x6[5]), '.0f') , "|" , format((x7[5]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[4]), '.0f') , "|" , format((x1[4]), '.0f') , "|" , format((x2[4]), '.0f') , "|" , format((x3[4]), '.0f') , "|" , format((x4[4]), '.0f') , "|" , format((x5[4]), '.0f') , "|" , format((x6[4]), '.0f') , "|" , format((x7[4]), '.0f') , "|       Garden after"
print "---------------------------------"
print "|" , format((x0[3]), '.0f') , "|" , format((x1[3]), '.0f') , "|" , format((x2[3]), '.0f') , "|" , format((x3[3]), '.0f') , "|" , format((x4[3]), '.0f') , "|" , format((x5[3]), '.0f') , "|" , format((x6[3]), '.0f') , "|" , format((x7[3]), '.0f') , "|       tenth turn"
print "---------------------------------"
print "|" , format((x0[2]), '.0f') , "|" , format((x1[2]), '.0f') , "|" , format((x2[2]), '.0f') , "|" , format((x3[2]), '.0f') , "|" , format((x4[2]), '.0f') , "|" , format((x5[2]), '.0f') , "|" , format((x6[2]), '.0f') , "|" , format((x7[2]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[1]), '.0f') , "|" , format((x1[1]), '.0f') , "|" , format((x2[1]), '.0f') , "|" , format((x3[1]), '.0f') , "|" , format((x4[1]), '.0f') , "|" , format((x5[1]), '.0f') , "|" , format((x6[1]), '.0f') , "|" , format((x7[1]), '.0f') , "|"
print "---------------------------------"
print "|" , format((x0[0]), '.0f') , "|" , format((x1[0]), '.0f') , "|" , format((x2[0]), '.0f') , "|" , format((x3[0]), '.0f') , "|" , format((x4[0]), '.0f') , "|" , format((x5[0]), '.0f') , "|" , format((x6[0]), '.0f') , "|" , format((x7[0]), '.0f') , "|"
print "---------------------------------"