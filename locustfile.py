import time

from locust import User, task

import app

class ComputeUser(User):

    @task
    def test_compute_fib_value(self):
        start = time.time() 

        try:

            result = app.compute_fib_value()
            total_ms = (time.time() - start) * 1000
            self.environment.runner.stats.log_request(

                "function",

                "compute_fib_value",

                total_ms,

                0
            )

        except Exception as e:

            total_time = (time.time() - start) * 1000
            self.environment.runner.stats.log_error(
                "function",
                "compute_fib_value",
                e
            )