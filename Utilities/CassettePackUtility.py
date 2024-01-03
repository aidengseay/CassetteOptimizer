################################################################################
# Cassette Pack Utility
# ======================
# This file is responsible for all packing algorithms.
# Created by Aiden Seay, Winter 2023
################################################################################
# IMPORTS
from ortools.linear_solver import pywraplp

################################################################################

# Find the most optimal way to pack the cassette
def packCassette(songInputList, binCap):

    durationList = []
    returnList = [[],[]]

    for song in songInputList:
        durationList.append(song.duration)
    
    data = {}
    data["weights"] = durationList
    data['values'] = [1] * len(songInputList)
    assert len(data['weights']) == len(data['values'])
    data["num_items"] = len(data['weights'])
    data["all_items"] = range(data['num_items'])

    data["bin_capacities"] = [binCap, binCap]
    data["num_bins"] = len(data['bin_capacities'])
    data["all_bins"] = range(data["num_bins"])

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if solver is None:
        print("SCIP solver unavailable.")
        return

    # Variables.
    # x[i, b] = 1 if item i is packed in bin b.
    x = {}
    for i in data["all_items"]:
        for b in data["all_bins"]:
            x[i, b] = solver.BoolVar(f"x_{i}_{b}")

    # Constraints.
    # Each item is assigned to at most one bin.
    for i in data["all_items"]:
        solver.Add(sum(x[i, b] for b in data["all_bins"]) <= 1)

    # The amount packed in each bin cannot exceed its capacity.
    for b in data["all_bins"]:
        solver.Add(
            sum(x[i, b] * data["weights"][i] for i in data["all_items"])
            <= data["bin_capacities"][b]
        )

    # Objective.
    # Maximize total value of packed items.
    objective = solver.Objective()
    for i in data["all_items"]:
        for b in data["all_bins"]:
            objective.SetCoefficient(x[i, b], data["values"][i])
    objective.SetMaximization()
    
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        for b in data["all_bins"]: # iterate through the bins b
            for i in data["all_items"]: # iterate through the song indices i
                if x[i, b].solution_value() > 0:
                    returnList[b].append(songInputList[i])
    else:
        print("The problem does not have an optimal solution.")

    return returnList

################################################################################