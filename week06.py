# 2. 배열 속성 (Attributes)
# 생성된 배열이 어떤 상태인지 확인하는 명령어입니다. (괄호 () 없이 사용)
# 모양 확인: arr.shape (예: (3, 2) → 3행 2열)
# 차원 확인: arr.ndim (예: 1차원, 2차원 등)
# 요소 개수: arr.size (전체 데이터 개수)
# 데이터 타입: arr.dtype (int64, float64 등)

import numpy as np

array01 = np.random.random((3,3))
print(array01)
print(array01.shape, array01.dtype, array01.ndim, array01.size)
print(array01.T)