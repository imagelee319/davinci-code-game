class RangeException(Exception):
    def __init__(self):
        super().__init__('입력 범위를 벗어났습니다.')

