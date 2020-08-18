def canCompleteCircuit(gas: [int], cost: [int]):
    start = 0
    current_gas = 0
    total_gas = 0
    for i in range(len(gas)):
        current_gas = current_gas + gas[i] - cost[i]
        total_gas = total_gas + gas[i] - cost[i]
        if current_gas < 0:
            start = i+1
            current_gas = 0
    if total_gas >= 0:
        return start
    else:
        return -1

gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]
a = canCompleteCircuit(gas, cost)
print(a)