## POETRY 환경 설정하는 법

poetry가 설치되지 않았다면?

```
pip install poetry
```

1. 아래 명령어로 환경 생성

```
poetry install
```

2. 환경 활성화

```
poetry shell
```

3. 종속성 설치

```
poetry install
```

4. 잘 돌아가는 지 확인

```
cd sse
python main.py
```

---

poetry 비활성화 방법

```
exit
```

poetry 종속성 추가 (새로운 라이브러리 설치하는 경우)

```
poetry add <라이브러리명>
```

<br />
<br />

## Git Branch 관리

[Git Flow 전략](https://inpa.tistory.com/entry/GIT-%E2%9A%A1%EF%B8%8F-github-flow-git-flow-%F0%9F%93%88-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EC%A0%84%EB%9E%B5)을 사용합니다. <br/>
자세한 프로세스는 노션 문서 참고

```
main: 배포
release: 배포 테스트
develop: 개발
---
feature/*: 기능 개발 (develop에서 생성, develop으로 merge)
```
