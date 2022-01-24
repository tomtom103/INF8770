from decimal import Decimal


def compute_frequency(msg: str) -> dict:
    """
    Compute the probability of each character in the message
    """
    msg = list(msg)
    prob = {}
    for char in msg:
        if char in prob:
            prob[char] += 1
        else:
            prob[char] = 1
    return prob

def get_probability_table(frequency_table: dict) -> dict:
    """
    Compute the probability table from the frequency table
    """
    prob = {}
    total = sum(frequency_table.values())
    for key, val in frequency_table.items():
        prob[key] = val / total
    return prob

def process_stage(prob_table: dict, stage_min: Decimal, stage_max: Decimal) -> dict:
    """
    Compute the probability table after a stage
    """
    stage_probs = {}
    stage_domain = stage_max - stage_min
    for idx in range(len(prob_table.items())):
        term = list(prob_table.keys())[idx]
        term_prob = Decimal(prob_table[term])
        cum_prob = term_prob * stage_domain + stage_min
        stage_probs[term] = [stage_min, cum_prob]
        stage_min = cum_prob
    return stage_probs

def get_encoded_value(last_stage_probs: dict) -> tuple:
    last_stage_probs = list(last_stage_probs.values())
    last_stage_values = []
    for sublist in last_stage_probs:
        for element in sublist:
            last_stage_values.append(element)
    
    last_stage_min = min(last_stage_values)
    last_stage_max = max(last_stage_values)
    encoded_value = (last_stage_min + last_stage_max) / 2

    return last_stage_min, last_stage_max, encoded_value

def encode(msg: str):
    """
    Encode a message using arithmetic encoding
    """
    msg = list(msg)

    encoder = []

    stage_min = Decimal(0.0)
    stage_max = Decimal(1.0)

    probability_table = get_probability_table(compute_frequency(msg))
    print(probability_table)
    for msg_term_idx in range(len(msg)):
        stage_probs = process_stage(probability_table, stage_min, stage_max)

        msg_term = msg[msg_term_idx]
        stage_min = stage_probs[msg_term][0]
        stage_max = stage_probs[msg_term][1]

        encoder.append(stage_probs)

    last_stage_probs = process_stage(probability_table, stage_min, stage_max)

    encoder.append(last_stage_probs)

    interval_min, interval_max, encoded_msg = get_encoded_value(last_stage_probs)
    return encoded_msg, probability_table, interval_min, interval_max

def decode(encoded_msg: Decimal, msg_length: int, probability_table: dict):
    """
    Decode an encoded message using arithmetic encoding
    """
    decoder = []

    decoded_msg = []

    stage_min = Decimal(0.0)
    stage_max = Decimal(1.0)

    for _ in range(msg_length):
        stage_probs = process_stage(probability_table, stage_min, stage_max)

        for msg_term, value in stage_probs.items():
            if encoded_msg >= value[0] and encoded_msg <= value[1]:
                break

        decoded_msg.append(msg_term)

        stage_min = stage_probs[msg_term][0]
        stage_max = stage_probs[msg_term][1]

        decoder.append(stage_probs)

    last_stage_probs = process_stage(probability_table, stage_min, stage_max)
    decoder.append(last_stage_probs)

    return decoded_msg, decoder
            

if __name__ == "__main__":
    original_msg = "abcabcde"
    print("Original message:", original_msg)
    encoded_msg, probability_table, interval_min, interval_max = encode(original_msg)
    print("Encoded message:", encoded_msg)
    print("Probability table:", probability_table)
    print("Interval min:", interval_min)
    print("Interval max:", interval_max)

    decoded_msg, decoder = decode(encoded_msg, len(original_msg), probability_table)
    print("Decoded message:", decoded_msg)