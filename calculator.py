from datetime import datetime

# Updated every time this file is saved — watch this timestamp change in test_calculator.py
LOADED_AT = datetime.now().strftime("%H:%M:%S") #?

class Calculator:
    def __init__(self):
        self._initialized = True

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        if a > 0 and b > 0:
            return a * b
        return 0
