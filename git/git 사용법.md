### git 기본
**Repository** : 저장소 (원격 저장소, 로컬 저장소)
* Github : 원격 저장소
* 내가 작업하는 PC : 로컬 저장소
<br>
<br>

### git 명령어
<br>

**git clone** : 원격 저장소에 있는 내용을 복제
* git clone -b <특정 브랜치 이름> <원격 저장소 url> : 특정 브랜치의 내용을 복제. 특정 브랜치에서 작업하게 됨
* -b 옵션이 없을 시 : 기본 master 내용을 복제
<br>

**git branch** : 브랜치 관리
* git branch : 로컬 브랜치 조회
* git branch -r : 원격 브랜치 조회
* git branch <특정 브랜치 명> : 특정 브랜치 신규 생성
* git checkout <특정 브랜치 명> : 특정 브랜치로 작업 브랜치를 이동
* git checkout -b <특정 브랜치 명> : 특정 브랜치 신규 생성 및 해당 브랜치로 작업 브랜치 이동
<br>

**git commit** : 변경 내용 기록
<br>

**git reset**
<br>

**git revert**
<br>

**git amend**
<br>

**git log** : 작업 내역 조회
* git log : commit 기록 조회
* git log --all : 모든 브랜치의 commit 기록 조회
* git log --oneline : commit 기록 한 줄로 출력
* git log --graph : commit 기록 그래프 형식으로 출력
* git log -p : diff 결과 출력
* git log -2 : 최근 2개의 commit 내역 출력
