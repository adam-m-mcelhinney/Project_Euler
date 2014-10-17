(* ::Package:: *)

(* Project Euler 34
145 is a curious number
, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal 
to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums 
they are not included.
*)
$RecursionLimit = 10^10000;
curSum[n_] := (
				t = IntegerDigits[n]; 
				t= Factorial/@t;
				s = Sum[i, {i, t}];
				s - n
				)
(*
curSum[145];
Range[1,100];
DiscretePlot[curSum[x],
					{x, 1, 100000}
					, PlotRange \[Rule] {{1, 100000}
						, {-10, 10}}
					, PlotStyle\[Rule] PointSize[.025]
					, Filling\[Rule]None
					];
		
*)		
2+2;
curious[n_] := (
				t = IntegerDigits[n]; 
				t= Factorial/@t;
				s = Sum[i, {i, t}];
				If[s == n, n, 0]
				)
curious[145];
curious[146];
(* Cheating and assuming that all curious digits live in this range 
Per the probelm definition, need to exclude 1 and 2. 
*)
r = curious/@Range[3, 1000000];
Total[r]




(* This is broke. Cannot figureo out why currently
allCurious[n_, cur_] := (
				n
				t = curious[n];
				If[n >= 10^10
					, cur
					, allCurious[n+1, Append[cur, t]]
					(*
					, If[ t \[NotEqual] 0
						, allCurious[n+1, Append[cur, t]]
						, allCurious[n+1, cur]
						]
					*)
				]
				)
*)



