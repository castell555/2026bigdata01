# 2. 배열 속성 (Attributes)
# 생성된 배열이 어떤 상태인지 확인하는 명령어입니다. (괄호 () 없이 사용)
# 모양 확인: arr.shape (예: (3, 2) → 3행 2열)
# 차원 확인: arr.ndim (예: 1차원, 2차원 등)
# 요소 개수: arr.size (전체 데이터 개수)
# 데이터 타입: arr.dtype (int64, float64 등)

# 1. 배열 생성 (Creation)
# 데이터를 담는 기본 단위인 ndarray를 만드는 방법입니다.
# 리스트로 생성: np.array([1, 2, 3])
# 연속 값 생성: np.arange(0, 10, 2) (0부터 10 미만까지 2씩 증가)
# 0 또는 1로 채우기: np.zeros((2, 3)), np.ones((3, 3))
# 랜덤 값: np.random.rand(2, 2) (0~1 사이 난수)

import numpy as np

l1 = [1, 2, 3]
array01 = np.array(l1)
print(l1)
array01 = np.random.random((3,3))
print(array01)

array02 = np.arange(0, 10, 2)
print(array02)

array03 = np.zeros((2, 3))
print(array03)

array04 = np.ones((2, 3))
print(array04)

array05 = np.full((2, 3), -1)
print(array05)

array06 = np.random.rand(2, 3)
print(array06)
print(array01.shape, array01.dtype, array01.ndim, array01.size)
print(array01.T)