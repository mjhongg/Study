### git 기본
**Repository** : 저장소 (원격 저장소, 로컬 저장소)
* _Github_ : 원격 저장소
* _내가 작업하는 PC_ : 로컬 저장소
<br>
<br>

### git 명령어
<br>

**git clone** : 원격 저장소에 있는 내용을 복제
* _git clone -b <특정 브랜치 이름> <원격 저장소 url>_ : 특정 브랜치의 내용을 복제. 특정 브랜치에서 작업하게 됨
* _-b 옵션이 없을 시_ : 기본 master 내용을 복제
<br>

**git branch** : 브랜치 관리
* _git branch_ : 로컬 브랜치 조회
* _git branch -r_ : 원격 브랜치 조회
* _git branch <특정 브랜치 명>_ : 특정 브랜치 신규 생성
* _git branch <특정 브랜치 명> <특정 commit hash value>_ : 특정 commit 위치에서 특정 브랜치 신규 생성
* _git checkout <특정 브랜치 명>_ : 특정 브랜치로 작업 브랜치를 이동
* _git checkout -b <특정 브랜치 명>_ : 특정 브랜치 신규 생성 및 해당 브랜치로 작업 브랜치 이동
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
* _git log_ : commit 기록 조회
* _git log --all_ : 모든 브랜치의 commit 기록 조회
* _git log --oneline_ : commit 기록 한 줄로 출력
* _git log --graph_ : commit 기록 그래프 형식으로 출력
* _git log -p_ : diff 결과 출력
* _git log -2_ : 최근 2개의 commit 내역 출력
