<div align="center">
    <h1>boj-user-translation</h1>
    <p><a href="https://github.com/kiwiyou/boj-user-translation/blob/main/README.md">English</a> / 한국어</p>
</div>

백준 온라인 저지 문제를 위한 유저 번역 저장소입니다.
번역물을 실제 문제에 적용하고 싶으시다면 [o-ey](https://github.com/kiwiyou/o-ey)를 참조해 주세요.

## 번역 참여 방법

Git과 Python 3이 필요합니다.

### 번역 환경 세팅

이 저장소를 포크 후, (페이지 오른쪽 위) 로컬에 클론해 주세요. (페이지 위쪽 녹색 버튼)
Git Bash를 열어 다음 명령어를 입력하면 저장소 폴더로 이동하실 수 있습니다.

```bash
cd <클론한 폴더 위치>
```

### 번역물 추가

Git Bash에서 저장소 폴더로 이동하신 뒤, 다음 명령어를 입력해 주세요.

```bash
python3 new-tr.py <문제 번호> <언어 코드> <번역자명>
```

- `<언어 코드>` 자리에는 [IETF language tag](https://www.wikiwand.com/en/IETF_language_tag)를 삽입하되, `-`는 `_`로 바꿔 주세요. (예: 한국어라면 `ko_KR`, 영어라면 `en_US`).

명령어를 입력하면 `src/<문제번호>/<언어 코드>-<번역자명>.html` 파일이 생성되고, `index` 파일이 수정됩니다.
생성된 파일의 내용 부분을 번역하신 뒤, 아래 명령어로 작업 내용을 GitHub에 업로드합니다.

```bash
git add .
git commit -m "작업 내용"
git push
```

### 번역물 확인

`o-ey` 확장 프로그램의 버튼을 누르면 나오는 창 맨 밑에 포크한 자신의 GitHub 저장소 주소를 한 줄 입력하세요.
수 분 이내로 변경사항이 적용되며, 백준 문제에서 자신의 번역을 확인해볼 수 있습니다.

### 저장소에 기여

저장소 페이지 위쪽 Pull requests → New pull request → Create Pull Request를 눌러 Pull Request를 생성합니다.
추가로 남기실 말이 있다면 적으신 후에 Create Pull Request 버튼을 다시 누르시면 기여 요청이 완료됩니다.

## 번역 규칙

- 새로운 섹션(문제, 입력, 출력, 제한 등)은 현재 추가할 수 없습니다.
- XSS를 비롯한 **악의적인 HTML 삽입은 금지합니다.**
- **문제의 의도를 존중한다면** 문단 순서를 바꾸거나, 문장을 다시 쓰거나, 등장인물의 이름을 변경하는 것은 괜찮습니다.
- 문제에 잘못된 점이 있다면 경고문을 적으셔도 좋으나,
  **경고문을 번역자가 삽입했다는 내용을 번역문에 추가해 주세요.**
- 문제 스타일은 [문제 포매팅 가이드라인](https://github.com/kiwiyou/boj-user-translation/blob/main/formatting-ko.md)을 따라 주세요.
- 위 제한을 따르면 자유롭게 번역하셔도 무방합니다.
- 제가 유창하지 않은 언어의 번역은 Pull Request의 승인이 늦어질 수 있습니다.
- Pull Request 전에 변경 사항을 `o-ey`로 한번 확인해 주세요.
  `o-ey` 버튼을 눌러 나오는 저장소 목록에서 자신의 저장소 주소를 추가하시면 됩니다.
