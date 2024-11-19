import logging
import unittest


class MyTest(unittest.TestCase):

    def test_sum_func(self):
        result = sum_of_elements(1, 2, 3)
        if self.assertEqual(6, result):
            logging.debug(f"test_sum_func was successfully tested")
        else:
            logging.error(f"test_sum_func was tested with error")


logging.basicConfig(filename="newlog", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def sum_of_elements(*args):
    logging.info(f"was summary: {args}")
    return sum(args)


a = sum_of_elements(1, 4, 5)

if __name__ == "__main__":
    unittest.main(verbosity=2)
