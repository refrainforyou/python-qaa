from lesson10.HW import log_event
import unittest
import os


class TestLogEvent(unittest.TestCase):
    log_file = 'login_system.log'

    @classmethod
    def setUpClass(cls):
        if os.path.exists(cls.log_file):
            os.remove(cls.log_file)

    def read_log_file(self):
        with open(self.log_file, 'r') as file:
            return file.read()

    def test_log_file_success(self):
        log_event('test_success', 'success')
        log_content = self.read_log_file()
        self.assertIn('Login event - Username: test_success, Status: success', log_content)

    def test_log_file_expired(self):
        log_event('test_expired', 'expired')
        log_content = self.read_log_file()
        self.assertIn('Login event - Username: test_expired, Status: expired', log_content)

    def test_log_file_error(self):
        log_event('test_error', 'error')
        log_content = self.read_log_file()
        self.assertIn('Login event - Username: test_error, Status: error', log_content)

    def test_log_file_unknown(self):
        log_event('test_unknown', 'unknown')
        log_content = self.read_log_file()
        self.assertIn('Login event - Username: test_unknown, Status: unknown', log_content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
