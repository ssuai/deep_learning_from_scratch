# ch02 유닛 테스트

Python 표준 라이브러리 `unittest`를 사용합니다.


## 테스트 파일 구조

`test_and_gate.py`는 AND 게이트의 진리표 4가지 입력을 각각 검증합니다.

```python
from unittest import TestCase

from and_gate import AND


class Test(TestCase):
    def test_and_00(self):
        y = AND(0, 0)
        self.assertEqual(y, 0)

    def test_and_01(self):
        y = AND(0, 1)
        self.assertEqual(y, 0)

    def test_and_10(self):
        y = AND(1, 0)
        self.assertEqual(y, 0)

    def test_and_11(self):
        y = AND(1, 1)
        self.assertEqual(y, 1)
```

- `test_`로 시작하는 메서드가 하나의 테스트입니다.
- `AND(0, 0)`처럼 함수를 호출한 뒤 `assertEqual`로 기대값과 비교합니다.
- 같으면 통과, 다르면 실패입니다.



## 테스트가 하는 일

`and_gate.py`의 `AND(x1, x2)`가 논리 AND와 같은지 확인합니다.

| 입력 | 기대 출력 |
|------|-----------|
| (0, 0) | 0 |
| (0, 1) | 0 |
| (1, 0) | 0 |
| (1, 1) | 1 |

가중치나 구현을 바꿔도 이 네 케이스가 통과하면 AND 게이트 동작은 유지된 것입니다.

같은 방식으로 NAND/OR 게이트는 `test_nand_gate.py`, `test_or_gate.py`에서 검증합니다.



## CLI에서 실행


### `ch02`로 이동한 뒤 파일을 직접 실행

```bash
cd ch02
python -m unittest test_and_gate.py -v
```

`test_nand_gate.py`처럼 파일 끝에 `unittest.main()`이 있으면 다음도 됩니다.

```bash
cd ch02
python test_nand_gate.py
```

성공하면 `OK`, 실패하면 `FAIL`과 어느 assertion이 깨졌는지가 나옵니다.

### 프로젝트 루트에서 실행

```bash
# ch02 전체 테스트
python -m unittest discover -s ch02 -p "test_*.py" -v

# 파일 하나
python -m unittest discover -s ch02 -p "test_and_gate.py" -v
```



## VS Code / Cursor에서 실행

1. 왼쪽 **Testing** 패널(플라스크 아이콘)을 엽니다.
2. `ch02` 아래 `test_and_gate.py`, `test_nand_gate.py`, `test_or_gate.py`가 보여야 합니다.
3. 파일/클래스/메서드 옆 **▶**로 원하는 범위만 실행합니다.
4. 에디터에서 `test_and_00` 같은 메서드 위 **Run Test** / **Debug Test**를 눌러도 됩니다.

관련 설정은 프로젝트 루트의 `.vscode/settings.json`에 있습니다.

### 설정하는 법

**방법 1. Command Palette (권장)**

1. `Cmd + Shift + P`로 Command Palette를 엽니다.
2. `Python: Configure Tests`를 실행합니다.
3. 프레임워크로 **unittest**를 선택합니다.
4. 테스트 디렉터리로 **ch02**를 선택합니다.
5. 파일 패턴으로 **`test_*.py`** 를 선택합니다.

이렇게 하면 `.vscode/settings.json`이 자동으로 만들어지거나 갱신됩니다.

**방법 2. settings.json을 직접 작성**

프로젝트 루트에 `.vscode/settings.json`을 만들고 아래처럼 적습니다.

```json
{
    "python.testing.unittestEnabled": true,
    "python.testing.pytestEnabled": false,
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./ch02",
        "-p",
        "test_*.py"
    ]
}
```

**방법 3. Settings UI**

1. `Cmd + ,`로 Settings를 엽니다.
2. 검색창에 `python testing unittest`를 입력합니다.
3. **Python > Testing: Unittest Enabled**를 켭니다.
4. **Python > Testing: Pytest Enabled**는 끕니다.
5. 이 프로젝트만 적용하려면 탭에서 **Workspace**를 선택한 뒤 수정합니다.

설정을 바꾼 뒤에는 Testing 패널에서 **Refresh Tests**를 눌러 테스트를 다시 찾습니다.

| 설정 | 의미 |
|------|------|
| `python.testing.unittestEnabled: true` | unittest 사용 |
| `python.testing.pytestEnabled: false` | pytest와 충돌하지 않도록 끔 |
| `-s ./ch02` | 테스트를 찾을 디렉터리 |
| `-p test_*.py` | 테스트 파일 이름 패턴 |
| `-v` | 각 테스트 결과를 자세히 출력 |


