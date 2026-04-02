def entrance_fee(ages) -> int:
    """
    def entrance_fee(ages: list) -> int:
    놀이공원 입장료를 계산합니다.
    # 요금 체계를 딕셔너리로 관리 (수정이 용이함)
    FEES = {
        'kid': 5000,
        'adult': 10000,
        'senior': 7000
    }

    total_fee = 0
    for age in ages:
        if age >= 65:
            total_fee += FEES['senior']
        elif age >= 19:
            total_fee += FEES['adult']
        # 0~18세는 어린이 요금 (필요하다면 0~3세 무료 조건 추가 가능)
        elif age >= 0:
            total_fee += FEES['kid']

    return total_fee
    """
    kid, adult, senior = 5000, 10000, 7000
    total_fee = 0
    for age in ages:
        if age >= 65:
            total_fee = total_fee + senior
        elif age >= 19:
            total_fee = total_fee + adult
        else:
            total_fee = total_fee + kid
    return total_fee