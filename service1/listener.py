import logging

import pybreaker

logger = logging.getLogger(__name__)


class OneListener(pybreaker.CircuitBreakerListener):
    "Listener used by circuit breakers that execute database operations."

    def before_call(self, cb, func, *args, **kwargs):
        "Called before the circuit breaker `cb` calls `func`."
        logger.error(f'[before_call]')

    def state_change(self, cb, old_state, new_state):
        "Called when the circuit breaker `cb` state changes."
        logger.error(f'[state_change] old_state:{old_state} new_state:{new_state}')

    def failure(self, cb, exc):
        "Called when a function invocation raises a system error."
        logger.error(f'[failure]')
        return {
            'message': 'hello'
        }

    def success(self, cb):
        "Called when a function invocation succeeds."
        logger.error(f'[success]')
