## CONDA 환경 설정하는 법

1. 아래 명령어로 환경 생성

```
conda env create -f environment.yml
```

2. 환경 활성화

```
conda activate devops-prj
```

3. pip 패키지 다시 설치

```
python -m pip install selenium fake_useragent webdriver_manager
```

4. 잘 돌아가는 지 확인

```
cd cse_main
python cse_main.py
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
