import maze
import pytest

@pytest.mark.parametrize('file_name, goal',
                         [('maze1.txt',(0, 5)),
                          ('maze2.txt',(8, 13)),
                          ('maze3.txt',(2, 1)),
                          ('maze4.txt',(1, 1)),
                          ('maze5.txt',(1, 5))
                          ])
def test_prueba(file_name, goal):
    m = maze.Maze(file_name)
    m.solve
    assert m.goal == goal
