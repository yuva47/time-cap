import unittest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
from src.time_cap import time_cap


class TestTimeCap(unittest.TestCase):
    def test_time_cap_decorator(self):
        @time_cap
        def dummy_function():
            import time
            time.sleep(0.1)

        with patch("src.time_cap.datetime") as mock_datetime:
            start_time = datetime(2024, 1, 1, 12, 0, 0, 0)
            end_time = start_time + timedelta(milliseconds=100)

            mock_datetime.now.side_effect = [start_time, end_time]

            with self.assertLogs(level="INFO") as captured_logs:
                dummy_function()

            self.assertTrue(
                any("dummy_function took 100.0 milliseconds" in log for log in captured_logs.output),
                "The time_cap decorator did not print the expected execution time."
            )


if __name__ == "__main__":
    unittest.main()
