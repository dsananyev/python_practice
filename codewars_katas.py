#1
'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

def xo(s):
    sum_x, sum_o = 0
    if len(s) == 0:
        exit()
    elif 'x' not in s.lower() and 'o' not in s.lower():
        return True
    else:
        for i in s.lower():
            if i == 'x':
                sum_x +=1
            elif i == 'o':
                sum_o +=1
        if sum_x == sum_o:
            return True
         
#2
'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text):
    arr = text.split(' ')
    newarr = []
    for i in range(len(arr)):
        newarr.append(arr[i][::-1])
    s = ' '.join((newarr))
    return s

#3
'''
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer.
If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2
'''

def sum_array(a):
    if len(a) == 0:
        return 0
    else:
        sum = 0
        for i in range(len(a)):
            sum += a[i]
        print(sum)
        return sum

#4
'''
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string,
 or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
'''

def duplicate_encode(word):
    word = word.lower()
    output = ''
    for i in word:
        if word.count(i) > 1:
            output += ')'
        else:
            output += '('
    return output

#5
'''
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
'''

def find_it(seq):
    for i in range(0,len(seq)):
        count = 0
        for j in range(0, len(seq)):
            if seq[i] == seq[j]:
                count +=1
        if count % 2 != 0:
            return seq[i]
        
            