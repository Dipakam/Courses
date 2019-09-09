Directions to use SAT solver:
1. Paste the required formula in cnf.txt file provided in the DIMACS format.
2. Make sure that the file starts with p cnf #propositions #clauses #No comments should be there in the lines before.
3. Command to execute program : python3 mew.py
4. Output format : SAT if formula is satisfiable along with a model (An array of literals which are to be kept true) UNSAT otherwise.
5. Time is printed on the next line.

Heuristics of Decomposition of clauses:
In every function call we are passing two veriables Current Clauses and a set of literals that we have assumed to be true. We use for loop
over the literals in the first clause and we assume the selected literal to be true. (in the first iteration the first literal in the first
clause (Current clause) is selected for Decomposition i.e in the first iteration we are splitting up the first disjunction .. we know that
for the given clause to be true at least one of the literal in that clause should be true and we are basically selecting that literal )
After selecting the literal we are removing the clauses that turn out to be true after assuming that literal to be true. Also we are removing
the literals that are negation of this literal ( if we have selected -2 then we will remove all the 2s)And then we pass this set of new
clauses and litrerals in a recursive function call .The base case for our function is easy -> We check if there are any contradictions in the
list of literals. If there is any contradiction , we return nothing. We check if the list of clauses is empty -> remember that we remove a
clause when it turns out to be satisfiable due to our assumption.  We also remove the empty lists in the lists of literals if any.
If we don't get any contradiction and the list of the clauses is empty then we return -1 (means SAT) also we store the list of the literals
in the variable 'ans'. If the returned value is -1 then the formula is satisfiable.
