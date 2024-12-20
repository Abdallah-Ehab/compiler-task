from collections import defaultdict

# grammer = {
#     "S":["aSB","b"],
    
#     "B":["bBa","a"]
# }

grammer = defaultdict(list)





## edge cases : 
# 1.check if the grammer is simple by looping over each array then finding if the first letter is terminal then finding if
# the first letter repeats ---> not disjoin ---> not simple
# 
# 
 
#  find the alphabet of the language


def check_simple():
    terminals = set()
    for key in grammer:
        old_starting_letter = ""
        for term in grammer[key]:
            if term[0] == old_starting_letter or term[0].isupper() or term == "":
                return False,None
            terminals.add(term[0])
            old_starting_letter = term[0]
    return True,terminals

## this function is to get the correct term to be replaced aka (alpha*A)
def get_the_right_term(cur_symbol,top_of_stack):
    for term in grammer[top_of_stack]:
        if term[0] == cur_symbol:
            return list(term)



def push_down(input_symbols,terminals,goal_symbol):
    stack = [goal_symbol]
    i = 0
    while stack and i < len(input_symbols):
        curr_symbol = input_symbols[i]
        if curr_symbol in terminals and stack[-1] in terminals and curr_symbol == stack[-1]:
            ## pop and advance
            stack.pop()
            i +=1
        elif curr_symbol in terminals and stack[-1] not in terminals:
            ## replace and retain
            
            the_right_term = get_the_right_term(cur_symbol=curr_symbol,top_of_stack=stack[-1])
            stack.pop()
            stack.extend(the_right_term[::-1])
        else:
            return False
    return True

if __name__ == "__main__":
    running = True
    while running:
        rule = input("Enter the grammer rule in the form of S : rule \n")
        if rule == "q":
            running = False
            break
        nonterminal_symbol, terminals_symbols = rule.split(":")
        nonterminal_symbol = nonterminal_symbol.strip()
        terminals_symbols = terminals_symbols.strip()
        
        grammer[nonterminal_symbol].append(terminals_symbols)
    goal_symbol = list(grammer.keys())[0]
    print(grammer)
    print(goal_symbol)
    is_simple,terminals = check_simple()
    if not is_simple:
        print("grammer is not simple")
    else:
        res = push_down("ababa",terminals=terminals,goal_symbol=goal_symbol)
        if res:
            print("good")
        else:
            print("bad")
        

            
        
