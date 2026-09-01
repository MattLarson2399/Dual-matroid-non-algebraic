load "matroids.m2";
needsPackage "MinimalPrimes"

kk = ZZ/2;
R = kk[X_1..X_10];
S1 = kk[T_1..T_6];
phi1 = map(S1, R, {T_1, T_2, T_3, T_1*T_2*T_3*(T_4 + T_6), T_1*T_3*(T_4 + T_5 + T_6), T_1^2*T_2*T_3*(T_4 + T_5), T_1*T_2*(T_5 + T_6), T_4, T_5, T_6});


I = trim kernel phi1

assert isPrime I

groundSet = set gens R;


M_bases = bases(R, I)

given = set apply(M_bases, s -> set s);
nonbases = select(subsets(gens R, 6), s -> not given#?(set s));

   << ", nonbases: " << #nonbases << endl;
scan(nonbases, s -> << s << endl);