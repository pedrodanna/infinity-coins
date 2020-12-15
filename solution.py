#Number of cents
n = 12

def get_sum(tup):
    '''
    Function to get the real sum according to coins values.
    *Get a tuple of coin occurancies as parameter.
    *Returns the sum of occurancies multiplied by the coin value.
    '''
    return tup[0]*25 + tup[1]*10 + tup[2]*5 + tup[3] 

def make_change():   
    '''
    Function to return an array of tuples with all the coin changes 
    possibilities.
    *Create empty arr to be the future answer.
    *Loop over the coin types one by one creating all the possibilities.
    *Sum the value with 'get_sum' method and checks to see if it is a valid
    combinations of change.
    *Return the array of tuples with all the possibilities of change.
    '''
    ans = []
    quarter = 0
    while quarter*25 <= n:
        dime=0
        while dime*10 <= n:
            nickel=0
            while nickel*5 <= n:
                pennie=0
                qdn = quarter*25 + dime*10 + nickel*5
                if n-qdn > 0:
                    pennie = n-qdn
                else:
                    pennie=0
                
                tup = (quarter, dime, nickel, pennie)
                if get_sum(tup) == n:
                    ans.append(tup)
                
                nickel += 1
            dime += 1
        quarter += 1
    return ans

#Print answer
print(make_change())