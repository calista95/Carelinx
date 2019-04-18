from nodes import * #import our nodes 

#function: visit each node in the tree and add its string to the results
#input: node, result array holding all the strings 
#output: recursive call until base case is reached 
def recursion(n, result):
    if n["is_text"] == True: #append string to result if it exists 
        result.append(n["string"])
    if not n["children"]: #base case: node does not have children, so return 
        return
    else: 
        for x in n["children"]:
            recursion(x, result)

#function: extracts string from node and its children
#input: node
#output: string 
def extract(n):
    result=[] #this is where we store the string fragments from the node and all its children nodes 
    recursion(n, result) #recursive call 
    print( ''.join(result) )
    return ''.join(result) #return the result as a string 

#function: compares whether two nodes have the same string 
#input: your two nodes
#output: none (string output)
def compare(n1, n2):
    if extract(n1) == extract(n2):
        print("Strings from both nodes are the same")
    else:
        print("Strings from both nodes are different")

#function: gets and verifies user input against bad or out of bounds inputs
#input: string of xth node (for example, "first" or "second"), this is purely for aesthetics and not for function
#output: integer of the node, checked for validity 
def getInput(x): 
    print("Enter the number of the "+x+" node you want to compare.")
    while(True):
        amount=input()
        try:
            if int(amount)<0 or int(amount)>17 : #raise exception if negative number or greater than 17 (I hardcoded only 17 nodes)
                raise Exception
            amount = int(amount) #convert it to int 
            break
        except Exception:
            print('Input not valid. Please try again.')
    return amount

def main():

    nodeList = [0,node1,node2,node3,node4,node5,node6,node7,node8,node9,node10,node11,node12,node13,node14,node15,node16,node17]

    firstNode = getInput("first")
    secondNode = getInput("second")
    compare(nodeList[firstNode], nodeList[secondNode]) #I used the firstNode and secondNode values as keys to access the node, then I called the function

if __name__ == "__main__":
    main()

