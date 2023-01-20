def digit(c: str, invalid: bool) -> int:
    d = int(c)
    if d < 0 or d > 9:
        invalid |= True
        return -1
    return d


def validate_id(turkishid: int) -> bool:
    if len(str(turkishid)) != 11:
        return False
    invalid = False
    odd_sum = digit(str(turkishid)[0], invalid)
    if invalid:
        return False
    even_sum = 0
    for i in range(1, 9, 2):
        even_sum += digit(str(turkishid)[i], invalid)
        odd_sum += digit(str(turkishid)[i + 1], invalid)
    first_checksum = digit(str(turkishid)[9], invalid)
    final_checksum = digit(str(turkishid)[10], invalid)
    if invalid:
        return False
    computed_final = (odd_sum + even_sum + first_checksum) % 10
    if final_checksum != computed_final:
        return False
    first = (odd_sum*7-even_sum) % 10
    if first < 0:
        first += 10
    return first_checksum == first
