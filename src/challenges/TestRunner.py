class TestRunner:
    def __init__(self, tests, functionDefinition) -> None:
        self._tests = tests
        self._method = functionDefinition
    
    def run(self):
        return [self._method(testItem) for testItem in self._tests]
    