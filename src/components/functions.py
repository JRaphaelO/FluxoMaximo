def LoadFile(file):
    path = "resources/" + file
    file_reference = open(path, "r")
    text_file = []

    for line in file_reference:
        text_file.append(line)

    return text_file

def SplitFile(text_file):
    vertices = text_file[0].split('\n')[0]
    bows = text_file[1].split('\n')[0]
    origin = text_file[2].split('\n')[0]
    drain = text_file[3].split('\n')[0]

    list_edges = []

    for x in range(4, len(text_file)):
        edges = {} 
        line = text_file[x].split(' ')
        edges["origin"] = int(line[0])
        edges["destiny"] = int(line[1])
        edges["cost"] = int(line[2].split("\n")[0])

        list_edges.append(edges)

    return vertices, bows, origin, drain, list_edges

def SaveSolution(solver, solutions, opt_solution, list_edges):
    path = "output/solution.txt"
    file = open(path, 'a')

    file.write('Numero de arcos = ' + str(solver.NumVariables()) + '\n')
    file.write('Numero de restricoes = ' + str(solver.NumConstraints()) + '\n')
    file.write('Valor objetivo otimo = ' + str(opt_solution) + '\n\n')

    file.write('Fluxo dos arcos:\n\n')

    count = 0
    for variable in solutions:
        if variable.name() != 'arco_X':
            file.write('fluxo: ' + str(list_edges[count]["origin"]) + ' -> ' + str(list_edges[count]["destiny"]) + '\n')
            file.write(str(variable) + ' solucao = ' + str(variable.solution_value()) + ' (capacidade: ' + str(variable.ub()) + ' || capacidade restante: ' + str(variable.ub() - variable.solution_value()) + ')\n\n')
        count += 1

    file.write('\n**************************************************************\n')
    file.write('**************************************************************\n\n')

    file.close()
