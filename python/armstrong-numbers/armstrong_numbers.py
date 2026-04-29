def is_armstrong_number(number):

    length = 0
    digits =[]
    x = number
    if number ==0:
        return True
    else:

        while x > 0:
            length+=1
            digits.append(x%10)
            x = x//10
        sum = 0
        for x in range(length):
            sum+= digits[x]**length
        if sum == number:
            return True
        else:
            return False
    
        
