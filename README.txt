#################
## py-dijkstra ##
#################

Dijkstra algorithm implemented in python for data structure

This code has a function and two sample graph inputs. The second graph is disconnected!

Function dijkstra parameters:
	-*graph: The adjacent matrix of graph as a two-dimensional nested-list
	-*source: The starting point of algorithm's index in matrix above (*graph)

Function dijkstra return values:
	-*dist: First return value is the list of cost for traveling from *source to the index vertex. For *source's index the value would be 0 and for unreachable vertices its value would be Inf.
	-*prev: Second return value is a guide list for the cheapest path. For *source's index its value would be -1, and for unreachable vertices its value would be NaN.

Function dijkstra local variables:
	-*Q: Set of unvisited vertices
	-*n: The number of vertices
	-*inf, *nan: The constant float values for Inf and NaN
	-*disconnect: The list of unreachable vertices

Ebick && Matin