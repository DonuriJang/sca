# macOS에 iTerm2 설치하기

## iTerm2란?

iTerm2는 macOS의 기본 터미널을 대체하는 강력한 터미널 에뮬레이터입니다. 향상된 기능과 사용자 정의 옵션을 제공합니다.

## 시스템 요구사항

- **운영체제**: macOS 12.4 이상
- **최신 버전**: iTerm2 3.6.6 (2025년 11월 17일 빌드)

## 설치 방법

### 1. 공식 웹사이트에서 다운로드 (권장)

가장 표준적이고 안전한 방법입니다.

1. [iTerm2 공식 다운로드 페이지](https://iterm2.com/downloads.html) 접속
2. 최신 안정 버전(Stable Release) 다운로드
3. 다운로드한 ZIP 파일 압축 해제
4. iTerm.app 파일을 **Applications** 폴더로 드래그 앤 드롭
5. Applications 폴더에서 iTerm2 실행

#### 보안 검증 (선택사항)

다운로드한 파일의 무결성을 확인하려면:
- 공식 웹사이트에서 제공하는 PGP 서명 사용
- Keybase를 통한 검증 가능

### 2. Homebrew를 통한 설치

Homebrew가 이미 설치되어 있다면 터미널에서 간단하게 설치할 수 있습니다:

```bash
brew install --cask iterm2
```

설치 후 Applications 폴더에서 iTerm2를 실행하거나 Spotlight(⌘ + Space)에서 "iTerm"을 검색하여 실행합니다.

## 첫 실행

1. Applications 폴더 또는 Launchpad에서 iTerm2 실행
2. macOS 보안 경고가 나타나면 "열기" 클릭
3. 설정 및 사용자 정의 시작

## 업데이트

### 공식 다운로드 설치 시

iTerm2 메뉴에서 자동 업데이트 확인:
- **iTerm2 > Check For Updates**

또는 설정에서 자동 업데이트 활성화:
- **iTerm2 > Settings > General > Update**

### Homebrew 설치 시

```bash
brew upgrade iterm2
```

## 기본 기능

- 분할 패널 (Split Panes)
- 핫키 윈도우 (Hotkey Window)
- 검색 기능
- 자동완성
- 페이스트 히스토리
- 무제한 스크롤백
- 풍부한 커스터마이징 옵션

## 추천 설정

### 1. 컬러 스킴 변경

**iTerm2 > Settings > Profiles > Colors** 에서 다양한 컬러 스킴 적용 가능

### 2. 폰트 설정

**iTerm2 > Settings > Profiles > Text** 에서 프로그래밍에 적합한 폰트 선택

### 3. 핫키 설정

**iTerm2 > Settings > Keys > Hotkey** 에서 전역 단축키 설정 (예: ⌘ + `)

## 삭제

### 애플리케이션 삭제

```bash
# Applications 폴더에서 삭제
rm -rf /Applications/iTerm.app
```

또는 Finder에서 Applications 폴더로 이동하여 iTerm을 휴지통으로 드래그

### Homebrew로 설치한 경우

```bash
brew uninstall --cask iterm2
```

### 설정 파일 삭제 (선택사항)

```bash
# iTerm2 설정 및 데이터 삭제
rm -rf ~/Library/Preferences/com.googlecode.iterm2.plist
rm -rf ~/Library/Application\ Support/iTerm2
```

## 보안 업데이트

iTerm2는 정기적으로 보안 업데이트를 제공합니다. SSH 통합을 사용하는 경우 특히 최신 버전으로 업데이트하는 것이 중요합니다.

## 추가 기능

### AI 플러그인 (선택사항)

최신 버전에서는 AI 기능을 위한 별도 플러그인 설치 가능:
- 플러그인 수동 설치 필요
- 설정에서 수동으로 활성화

## 참고 자료

- [iTerm2 공식 웹사이트](https://iterm2.com/)
- [iTerm2 다운로드 페이지](https://iterm2.com/downloads.html)
- [iTerm2 GitHub](https://github.com/gnachman/iTerm2)
- [Homebrew Formula](https://formulae.brew.sh/cask/iterm2)
- [macOS Setup Guide - iTerm2](https://sourabhbajaj.com/mac-setup/iTerm/)

## 추천 조합

iTerm2는 다음과 같은 도구들과 함께 사용하면 더욱 강력합니다:
- Oh My Zsh (Zsh 프레임워크)
- Powerlevel10k (Zsh 테마)
- Claude Code (AI 코딩 도우미)
