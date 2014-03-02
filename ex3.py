
print "I will now count my chickens:"
# Tells you what the program is going to do.

print "Hens", 25 + 30 /6
# Calculates the number of hens in the operation. It first divides 30 by 6 to give 5. Then, it adds 25 to 5, following the order of operations.
print "Roosters", 100 - 25 * 3 % 4
# First it multiplies 25 by 3 to yield 75, then it takes 4% of 75 giving 3 as a value. Subtracts 3 from 100 to give 97 as the output.
print "Now I will count the eggs:"
# prints what will be calculated next, which is eggs in this case.
print 3 + 2 + 1 -5 +4 % 2 - 1 / 4 + 6
# my calculator gave me 1.35 but python gives me 7, this is because my calculator prioritizes the % and division calulation over the others. Python must  follow PEMDAS, so it takes the first half of the operation to get 5, then % 2, to get 0.1 adds this to 1/4+6 which is 6.25 to get 6.35...maybe? let's try it out

# print 0.1 + 6.25
# nope, that is not the ticket...how did this mofo calculate this hot mess?
# print 3 + 2 + 1 -5
# gives us 1
# now let's try 
# print 4 % 2
# that gave us 0
# so we have 1 + 0 to = 1
# print 1 % 2
# gives us 1
# print 1 / 4 + 6
# so that part of the operation gave us 6
# we add 1 + 6 and we get 7! WHOOP WHOOP, it divides the operations in half and then adds them up, PEMDAS motherf***cker!

print "Is it true that 3 + 2 < 5 - 7?"
# It got 5 and -2, respectively so this is false
print 3 + 2 < 5 - 7
# above was test
print "What is 3 + 2?", 3 + 2
# gives us the output of this addition
print "What is 5 - 7?", 5 - 7
# gives us the expected outcome of this subtraction 
print "Oh, that's why it's False."
# gives us justification as to why the false answer was given
print "How about some more."
# primes us that we are going to do more regarding negative numbers
print "Is it greater?", 5 > -2
# Yep, it's greater alright!
print "Is it greater or equal?", 5 >= -2
# Still greater
print "Is it less or equal?", 5 <= -2
# It is not less, le false!
