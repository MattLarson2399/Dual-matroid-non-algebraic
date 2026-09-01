bases = (R, I) -> (
     --Take an ideal I in ring R.
     --Return the list of bases in the matroid.
     
     E = set gens R;
     mRank = dim I;
     potentialBases = subsets(E,mRank);
     baseList = toList set apply(potentialBases, base -> 
	  (if (codim eliminate(toList (E-base),I) == 0) then toList base)) - set{null};
     numBases = length baseList;
     B = baseList
     )

decoratedBases = (R,I) -> (
     --Take ideal I in ring R
     --Return the set of bases, with decoration for degree of projection map.
     B = bases(R,I);
     apply(B, base -> (base, degree(ideal(apply(base, var -> var - random(1,1000000))) + I)))
          )  
     
circuitsBySize = (R, I, n) -> (
     --Take an ideal I in ring R.
     --Returns a list of circuits in the matroid with n elements.
     
     E = set gens R;
     L = subsets(E,n);
     PolyList = apply(L, ci -> eliminate(toList (E - ci),I));
     circuitList = toList set apply(PolyList, ci ->
	  (if (codim ci == 1) and length support((flatten entries gens ci)#0) == n 
	       then toList support((flatten entries gens ci)#0))) - set{null};
     C = circuitList
     )
 
circuits = (R, I) -> (
     --Take an ideal I in ring R.
     --Returns a list of circuits in the matroid.
     sizedCircuits = for ind from 1 to (dim I) + 1 list circuitsBySize(R,I,ind);
     circuitList = toList set flatten sizedCircuits
     )
 
pCircuitsBySize = (R, I, n) -> (
     --Take an ideal I in ring R.
     --Returns a list of decorated circuits in the matroid with n elements.
     E = set gens R;
     L = subsets(E,n);
     PolyList = apply(L, ci -> eliminate(toList (E - ci),I));
     circuitList = toList set apply(PolyList, ci ->
	  (if (codim ci == 1) and length support((flatten entries gens ci)#0) == n 
	       then (toList support((flatten entries gens ci)#0), (flatten entries gens ci)#0))) - set{null};
     C = circuitList
     )

pCircuits = (R, I) -> (
     --Take an ideal I in ring R.
     --Returns the list of decorated circuits in the matroid.
     E = set gens R;
     sizedCircuits = for n from 1 to dim I + 1 list pCircuitsBySize(R,I,n);
     circuitList = toList set flatten sizedCircuits
     )

topDegree = (R,f) -> (
     --Takes polynomial f in ring R and gives topdegree.
     varList = gens R;
     td = for i from 0 to (length(varList) - 1)
     list degree(varList#i, f);
     td
     )