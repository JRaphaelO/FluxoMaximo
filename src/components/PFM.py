class PFM:

    def __init__(self, vertices, edges, origin, drain, list_edges, solver):
        self.vertices = int(vertices)
        self.edges = int(edges)
        self.origin = int(origin)
        self.drain = int(drain)
        self.list_edges = list_edges
        self.solver = solver
        self.variables_solver = []
        self.restriction = []
        self.objective = None
        self.opt_solution = None

    def init_variables(self): 
        for edge in range(0, int(self.edges), 1):
            self.variables_solver.append(self.solver.NumVar(0, self.list_edges[edge]["cost"], "arco_" + str(edge + 1)))
        
        self.variables_solver.append(self.solver.NumVar(0, self.solver.infinity(), "arco_X"))
    
    def add_restriction(self):

        vertice = 2

        while vertice <= self.vertices: # 2 3 ... n
            constraint = self.solver.Constraint(0, 0)

            count = 0
            while count < len(self.list_edges):
                if vertice == self.list_edges[count]["origin"]:
                    constraint.SetCoefficient(self.variables_solver[count], 1)

                count += 1
            
            count = 0
            while count < len(self.list_edges):
                if vertice == self.list_edges[count]["destiny"]:
                    constraint.SetCoefficient(self.variables_solver[count], -1)

                count += 1

            if vertice == self.drain:
                constraint.SetCoefficient(self.variables_solver[len(self.variables_solver) - 1], 1)
                self.restriction.append(constraint)
            else:
                self.restriction.append(constraint)
                del constraint
            
            vertice += 1
       
        
    def objective_function(self):
        self.objective = self.solver.Objective()

        for variable in self.variables_solver:
            if variable.name() != 'arco_X':
                self.objective.SetCoefficient(variable, -1)

        self.objective.SetMinimization() 

    def solve(self):
        self.solver.Solve()
        self.opt_solution = self.variables_solver[len(self.variables_solver) - 1].solution_value()

        print('Numero de arcos =', self.solver.NumVariables())
        print('Numero de restricoes =', self.solver.NumConstraints())
        print('Valor objetivo otimo =', self.opt_solution)

    def solution(self):
        print("\n\nSolucao Otima")

        count = 0
        for variable in self.variables_solver:
            if variable.name() != 'arco_X':
                print('fluxo: ', self.list_edges[count]["origin"], ' -> ', self.list_edges[count]["destiny"])
                print(variable, ' solucao = ', variable.solution_value(), ' (capacidade: ', variable.ub(), ' || capacidade restante: ', variable.ub() - variable.solution_value(), ')\n')
            count += 1

        print('Valor objetivo otimo = ', self.opt_solution)

        return self.solver, self.variables_solver, self.opt_solution