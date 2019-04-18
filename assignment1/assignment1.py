import sys

#input: list of integer coin denominations and value desired 
#output: 
#   if there is a solution, return a list of coins that make up the solution
#   else, return an empty list
def amountToCoins(amount, denoms):
    table = [[] for _ in range(amount+1)] #hash table to store the solution sets 
    solution = [sys.maxsize]*(amount+1) #initialize solution table with each spot having largest system number allowed
    solution[0] = 0 #initialize zero value b/c 0 ways to get 0 coins 
    for i in range(1,amount+1): #solve for every subproblem 
        for j in range(len(denoms)): #each subproblem looks at each coin in the given set 
            if denoms[j] <= i: #if the coin value is less than or equal to the subproblem at hand 
                if solution[i-denoms[j]]+1 < solution[i]: #subproblem plus current coin denom is better than current solution
                    table[i].clear()
                    table[i].append(denoms[j]) #put in the coin denomination in the hashmap
                    for x in table[i-denoms[j]]: #copy the answers to the subproblem in the hashmap
                        table[i].append(x)
                    solution[i] = solution[i-denoms[j]]+1 #update the solution
    if solution[amount] == sys.maxsize:
        return []
    else:
        return table[amount]

def main():
    denoms=list()
    amount=0
    #get user input for number of coins and verify input 
    print("Enter all your coin denominations. Enter 0 when you are done.")
    while(True):
        amount=input()
        try:
            if int(amount) <0: #raise exception if negative number
                raise Exception
            if int(amount) == 0: #if user entered 0, exit the loop 
                break
            denoms.append(int(amount))
        except Exception:
            print('Input not valid (you may have entered an invalid character or a negative number). Please try again.')
    #display array of coins to user
    print('Your coins: ')
    for x in denoms:
        print(str(x)+" ", end="")
    print("\n")
    #get user input for desired amount and verify input 
    print("Enter the integer amount you want your coins to add up to.")
    while(True):
        amount=input()
        try:
            if int(amount)<0: #raise exception if negative number
                raise Exception
            amount=int(amount)
            break
        except Exception:
            print('Input not valid. Please try again.')
    #display coin value to user
    print('Your coin value: '+str(amount))
    print('\n')
    denoms = sorted(denoms) #make sure that denoms are sorted 
    result = amountToCoins(amount, denoms) #function call 
    if not result:
        print("No solution")
    else:
        print("The coins that make up your solution are:")
        for x in result:
            print(x, end=" ")

        
if __name__ == "__main__":
    main()