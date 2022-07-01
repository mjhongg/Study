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
* _git commit_ : commit 수행. vi 편집기로 commit 메시지 작성
* _git commit -m "<commit 메시지>"_ : commit 메시지 한 줄 입력과 동시에 commit
* _git commit --amend_ : 이미 commit 한 건에 대해 commit 문구 변경 및 덮어쓰기
<br>

**git reset** : commit 취소
* _git reset --soft <commit id>_ : commit 된 파일들을 staging area 로 돌려놓음 (commit 하기 직전 상태)
* _git reset --mixed <commit id>_ : commit 된 파일들을 working directory 로 돌려놓음 (add 하기 직전 상태)
* _git reset --hard <commit id>_ : commit 된 파일들 중 tracked 파일들을 working directory 에서 삭제
	* _git clean -f_ : untracked files 까지 삭제하고자 하는 경우
	* _git clean -n_ : 삭제 대상(untracked files) 목록 확인
* _HEAD~n_ : 가장 최신 commit 부터 n개의 commit 취소
* _HEAD^_ : 가장 최식 commit 취소 (기본 옵션 mixed)
<br>

**git revert** : commit 취소
* _git revert <commit id>_ : commit id 까지 이력을 남기며 취소
<br>

**reset과 revert**
* _reset_ : 되돌아간 commit 이후의 commit 이력을 남기지 않음
* _revert_ : 되돌아간 commit 이후의 commit 이력을 남겨두고 새로운 commit 을 생성
<br>

**git merge** : 브랜치 병합
* _git merge feature_ : feature 브랜치를 병합
	* _git checkout master_ : 우선 기준이 될 브랜치로 checkout. 그 후 위 명령어 수행
	* _git merge master feature_ : featuer 브랜치를 master 브랜치에 병합
	* _Fast-forward_ : feature 브랜치가 master 브랜치에 기반한 브랜치일 경우. 최신 commit 위치만 변경됨
	* _3-way Merge_ : master 가 feature 의 조상 브랜치이지만 master 브랜치의 또 다른 신규 commit 으로인해 가장 최신 commit 과 조상이 되는 commit 달라졌을때. 신규 commit 을 발생시키면서 병합
* conflict 발생
	* merge 하는 두 브랜치에서 동일 파일의 한 부분을 동시에 수정 시 conflict 발생. 직접 수정 필요
	* 충돌이 일어난 파일에 대해서는 unmerged 상태로 표시됨
<br>

**git rebase** : 브랜치 병합
* 
<br>

**stashing**
<br>

**git log** : 작업 내역 조회
* _git log_ : commit 기록 조회
* _git log --all_ : 모든 브랜치의 commit 기록 조회
* _git log --oneline_ : commit 기록 한 줄로 출력
* _git log --graph_ : commit 기록 그래프 형식으로 출력
* _git log -p_ : diff 결과 출력
* _git log -2_ : 최근 2개의 commit 내역 출력
<br>

**git reflog**
