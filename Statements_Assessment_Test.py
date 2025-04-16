#Statements Assessment Test

#Let's test your knowledge!

#1 Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
stx = st.split()

for _ in stx:
    if _[0] == 's':
        print(_)


#2 Use range() to print all the even numbers from 0 to 10.

for _ in range(0,10):
    if _%2 == 0:
        print(_)


#3 Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

mylist = [x for x in range(0,50) if x % 3 == 0]

print(mylist)


#4 Go through the string below and if the length of a word is even print "even!"

st2 = 'Print every word in this sentence that has an even number of letters'

st21 = st2.split()

for _ in st21:
    if len(_) % 2 == 0:
        print(f"the number {len(_)} is even!")


#5 Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for _ in range(1,101):
    if _ % 3 == 0 and _ % 5 == 0:
        print(f"{_} FizzBuzz") 
    elif _ % 3 == 0:
        print(f"{_} Fizz")
    elif _ % 5 == 0:
        print(f"{_} Buzz")
    else:
        print(_)


#6 Use List Comprehension to create a list of the first letters of every word in the string below:

st3 = 'Create a list of the first letters of every word in this string'

mylistagain = [x[0] for x in st3.split()]
print(mylistagain)