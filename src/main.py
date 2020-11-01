from components.functions import LoadFile, SplitFile, SaveSolution
from components.PFM import PFM
from ortools.linear_solver import pywraplp

def main():
    file = LoadFile("instance1.txt")

    vertices, bows, origin, drain, list_edges = SplitFile(file)

    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    pfm = PFM(vertices, bows, origin, drain, list_edges, solver)
    pfm.init_variables()
    pfm.add_restriction()
    pfm.objective_function()
    pfm.solve()
    solver, solution, opt_solution = pfm.solution()
    SaveSolution(solver, solution, opt_solution, list_edges)



if __name__ == '__main__':
    main()
