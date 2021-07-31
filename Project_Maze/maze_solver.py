import argparse
import main as Project_Maze


def Main():
    pars = argparse.ArgumentParser()
    pars.add_argument("-o", "--outputfile", help="Output the result to a file", action="store_true")
    pars.add_argument("-i", "--inputfile", help="Output the result to a file", action="store_true")
    ars = pars.parse_args()
    if ars.outputfile:
        data = open("outputfile.txt", "a")
        if Project_Maze.res.solve_Maze(Project_Maze.mat) is False:
            data.write(str("-1"))
        else:
            for i in Project_Maze.res.solve_Maze (Project_Maze.mat):
                for result in i:
                    data.write(str(result) + " ")
                data.write('\n')


Project_Maze.res.solve_Maze(Project_Maze.mat)

if __name__ == '__main__':
    Main()