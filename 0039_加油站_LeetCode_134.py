class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        record = []
        for i in range(len(gas)):
            record.append(dict({'start': i, 'value': gas[i] - cost[i]}))
        while len(record) > 1:
            front = record.pop(0)
            if front['value'] > 0:
                while len(record) != 0 and record[0]['value'] >= 0:
                    front['value'] += record.pop(0)['value']
            while len(record) != 0 and record[0]['value'] < 0:
                front['value'] += record.pop(0)['value']
            record.append(front)
        if record[0]['value'] < 0:
            return -1
        else:
            return record[0]['start']
