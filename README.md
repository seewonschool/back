## CONDA 환경 설정하는 법

1. 아래 명령어로 환경 생성

```
conda env create -f environment.yml
```

2. 환경 활성화 후 pip 패키지 다시 설치

```
conda activate devops-prj
python -m pip install selenium fake_useragent webdriver_manager
```
