import unittest
import timer


class timerTest(unittest.TestCase):

    def setUp(self):
        timer.start_timer(100)

    def test_start_timer(self):
        self.assertEqual(100, timer.time_left)

    def test_start_started_timer(self):
        result = timer.start_timer(100)

        self.assertEqual(False, result)

    def test_decrease_time(self):
        result = timer.decrease_time()

        self.assertTrue(result)
        self.assertEqual(99, timer.time_left)

    def test_decrease_time_from_non_started_timer(self):
        timer.is_running = False
        result = timer.decrease_time()

        self.assertEqual(False, result)

    def test_decrease_time_thats_over(self):
        timer.is_running = False
        timer.start_timer(0)
        result = timer.decrease_time()

        self.assertEqual(False, result)

    def tearDown(slef):
        timer.is_running = False

if __name__ == '__main__':
    unittest.main()
