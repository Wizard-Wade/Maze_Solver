import unittest
import maze

class testsolver(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = maze.maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._maze__cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

        
if __name__ == "__main__":
    unittest.main()