import unittest

import pandas as pd
import numpy as np

import utils.file_io


class TestFunc(unittest.TestCase):
    def test_pickle_io(self):
        table = np.array([[4, 2], [12, -1]])
        utils.file_io.write_pickle(table, "test")
        table = utils.file_io.read_pickle("test")
        self.assertEqual(4, table[0][0])


if __name__ == "__main__":
    unittest.main()

