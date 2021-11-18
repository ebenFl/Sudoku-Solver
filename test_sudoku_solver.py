import unittest

from sudokuSolver import sudoku


[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

class TestSodokuSolver(unittest.TestCase):

    def setUp(self):
        self.puzzles = [
            [
                [0,0,0,0,7,0,0,0,9],
                [0,9,0,5,0,0,0,1,0],
                [0,0,6,9,8,0,0,0,3],
                [2,0,0,0,0,7,6,0,0],
                [0,0,4,0,0,0,2,0,0],
                [0,0,5,4,0,0,0,0,7],
                [8,0,0,0,4,9,5,0,0],
                [0,1,0,0,0,5,0,7,0],
                [4,5,0,0,3,0,0,0,0]
            ],
            [
                [0,0,9,0,3,0,4,0,0],
                [8,7,0,0,0,9,0,0,0],
                [0,3,0,0,8,0,9,1,0],
                [9,0,0,5,0,0,0,0,3],
                [0,0,5,0,4,0,2,0,0],
                [1,0,0,0,0,6,0,0,4],
                [0,5,4,0,6,0,0,2,0],
                [0,0,0,8,0,0,0,4,9],
                [0,0,8,0,1,0,6,0,0]
            ]
        ]

        self.solutions = self.puzzles = [
            [
                [5,4,3,2,7,1,8,6,9],
                [7,9,8,5,6,3,4,1,2],
                [1,2,6,9,8,4,7,5,3],
                [2,8,1,3,9,7,6,4,5],
                [9,7,4,6,5,8,2,3,1],
                [3,6,5,4,1,2,9,8,7],
                [8,3,7,1,4,9,5,2,6],
                [6,1,9,8,2,5,3,7,4],
                [4,5,2,7,3,6,1,9,8]
            ],
            [
                [5,2,9,6,3,1,4,8,7],
                [8,7,1,4,2,9,5,3,6],
                [4,3,6,7,8,5,9,1,2],
                [9,4,2,5,7,8,1,6,3],
                [7,6,5,1,4,3,2,9,8],
                [1,8,3,2,9,6,7,5,4],
                [3,5,4,9,6,7,8,2,1],
                [6,1,7,8,5,2,3,4,9],
                [2,9,8,3,1,4,6,7,5]
            ]
        ]


    def test_solve(self):
        for i in range(len(self.puzzles)):
            puzzle = self.puzzles[i]

            sudoku_puzzle = sudoku(puzzle)

            sudoku_puzzle.solve(0,0)

            self.assertEqual(sudoku_puzzle.grid,self.solutions[i])

    def test_validate(self):
        for i in range(len(self.solutions)):
            solution = self.solutions[i]

            sudoku_puzzle = sudoku(solution)

            self.assertEqual(sudoku_puzzle.validate(),True)


if __name__ == '__main__':
    unittest.main()