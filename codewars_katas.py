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
           
