# Courier Service Optimization Algorithm

## Description
This Assignment presents an algorithm to optimize delivery routes for a courier service, aiming to minimize delivery time. It uses a Hill Climbing algorithm to find efficient delivery sequences for multiple delivery lorries.

## Problem Statement
In a busy city, a courier service needs to deliver packages from a central station to various locations within the city. Lorries have limited capacities and must visit multiple locations in a single trip. The objective is to find the best delivery routes to minimize the total travel distance for all lorries.

## Algorithm
The algorithm used is Hill Climbing, a heuristic search algorithm. It starts with an initial solution (randomly assigned delivery sequences) and iteratively explores neighboring solutions by swapping delivery locations between lorries. If a neighboring solution results in a shorter total distance, it is accepted as the new current solution. The process continues until no better solutions can be found or a predefined number of iterations is reached.

## Usage
1. Create an input file in the specified format (see Input File Format section).
2. Run the algorithm using the provided script.
3. The algorithm will optimize the delivery routes and generate an output file.

## Input File Format
The input file should be in the following format('N' means not a path.):
1.  0,5,N,N,N,6 
2.  5,0,19,N,15,N
3.  N,19,0,22,N,10
4.  N,N,22,0,10,N
5.  N,15,N,10,0,12
6.  6,N,10,N,12,0
7.  truck_1#2
8.  truck_2#3

## Output
The output file will contain optimized delivery sequences for each lorry, along with the total distance traveled. For example:

1. truck_1#f,c
2. truck_2#b,e,d
3. 46

## Customization
You can customize the algorithm parameters (e.g., the number of iterations) in the script for your specific problem.

