(* ::Package:: *)

(* Project Euler
Problem 62
The cube, 41063625 (3453), can be permuted to 
produce two other cubes: 56623104 (3843) and 66430125 (4053). I
n fact, 41063625 is the smallest cube which has exactly three 
permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of 
its digits are cube.
*)
$IterationLimit = 10^100;
genAll[n_] := Map[FromDigits, Permutations[IntegerDigits[n]]]
genAll[123]
isCube[n_] := IntegerQ[n^(1/3)]
isCube[41063625]
numCubes[n_] := Count[Map[isCube, genAll[n]], True]
numCubes[41063625]

(* Lowest number with k permutations that are cubic *)
kCubes[i_, k_] := If[numCubes[i] == k, i, kCubes[i+1, k]]
(* Why is this returning 1 higher than it should? *)
kCubes[41063625-500, 3]

(* Try this without recursion 
kCubes2[i_] := If[numCubes[i] \[Equal] 5, i, ]
*)









(* ::InheritFromParent:: *)
(**)



