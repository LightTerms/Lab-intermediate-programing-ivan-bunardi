#lab intermediate


from collections import Counter

class ClickCounter:
    def __init__(self):
        self.counter = Counter()

    def reset(self):
        self.counter = Counter()

    def click(self):
        self.counter['clicks'] += 1

    def getValue(self):
        return self.counter['clicks']

# Example usage
tally = ClickCounter()
tally.reset()
tally.click()
tally.click()
result = tally.getValue()
print(result)  # Output: 2
tally.click()
result = tally.getValue()
print(result)  # Output: 3
