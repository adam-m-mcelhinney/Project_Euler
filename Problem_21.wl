(* ::Package:: *)

(*
Project Euler Problem 21
*)

f[n_] := (
			t = Divisors[n]; 
			div = t[[Range[1,Length[t]-1]]]; 
			Sum[q, {q, div}])
(*
f[220]
f[284]
f[220] \[Equal] 284;
220 \[Equal] f[284];
*)
amicable[n_] := ( test = f[n]; other = f[test]; If[n == other, n, 0])
amicable[220];
am = amicable/@ Range[2, 10000];
(* No idea why this is not correct *)
Sum[i, {i, am}]
(*
Divisors[220]
f[220]
Divisors[284]
f[284]
*)



