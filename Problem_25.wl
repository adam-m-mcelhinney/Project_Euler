(* ::Package:: *)

(* Project Euler Problem 25
What is the first term in the Fibonacci 
sequence to contain 1000 digits?
*)

$RecursionLimit = 10^1000;

Fibonacci[1];
fibCount[i_, count_] := (t = Fibonacci[i];
				If[IntegerLength[t] != 1000
				, fibCount[i+1, count+1]
				, count]
				)
r = fibCount[1, 1];
IntegerLength[r]
r
				
	






