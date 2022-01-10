from typing import List

def modulation_delta(signal: List[int], n: int) -> List[tuple]:
    result = [(None, signal[0])]
    for i in range(1, len(signal)):
        delta = signal[i] - result[i-1][1]
        if delta > 0:
            result.append((1, result[i-1][1] + n))
        else:
            result.append((0, result[i-1][1] - n))
    return result

if __name__ == "__main__":
    signal = [7, 9, 11, 12, 13, 14, 15, 11, 11, 11, 11]
    print(f"Modulation delta: ${modulation_delta(signal, 2)}")
    print(f"Code final: ${[x[0] for x in modulation_delta(signal, 2)][1:]}")