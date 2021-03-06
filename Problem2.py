# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

endNumber = 4000000
first = 1
second = 2
third = first + second
sum = 2

while third <= endNumber:
    if (third % 2 == 0):
        sum = sum + third
    first = second
    second = third
    third = first + second

print "Sum is : ", sum
