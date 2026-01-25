# macOS에 Oh My Zsh 설정하기

## Oh My Zsh란?

Oh My Zsh는 Zsh 셸 구성을 관리하기 위한 오픈소스 커뮤니티 기반 프레임워크입니다. 300개 이상의 플러그인과 140개 이상의 테마를 제공하여 터미널 생산성을 향상시킵니다.

## 사전 요구사항

### Zsh 버전 확인

macOS는 기본적으로 Zsh를 포함하지만 버전을 확인하세요:

```bash
zsh --version
```

**권장 버전**: Zsh 5.0.8 이상
**최소 버전**: Zsh 4.3.9 이상

### 기본 셸을 Zsh로 변경 (필요시)

```bash
chsh -s $(which zsh)
```

터미널을 재시작하여 변경사항을 적용합니다.

### 필수 도구

- curl 또는 wget
- Git 2.4.11 이상

Git 설치 확인:

```bash
git --version
```

## 설치 방법

### 1. curl을 사용한 설치 (권장)

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### 2. wget을 사용한 설치

```bash
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### 3. 대체 미러 사용 (중국 등 접근 제한 지역)

```bash
sh -c "$(curl -fsSL https://install.ohmyz.sh/)"
```

설치가 완료되면 터미널이 자동으로 Zsh로 전환되고 Oh My Zsh가 활성화됩니다.

## 기본 설정

### 설정 파일 위치

Oh My Zsh 설정은 `~/.zshrc` 파일에서 관리됩니다.

```bash
# 설정 파일 편집
nano ~/.zshrc
# 또는
vim ~/.zshrc
# 또는
code ~/.zshrc
```

### 설정 변경 후 적용

```bash
source ~/.zshrc
```

## 테마 설정

### 기본 테마 변경

`~/.zshrc` 파일에서 `ZSH_THEME` 변수를 수정:

```bash
# 기본 테마
ZSH_THEME="robbyrussell"

# 인기있는 테마들
ZSH_THEME="agnoster"
ZSH_THEME="powerlevel10k/powerlevel10k"
ZSH_THEME="bureau"
ZSH_THEME="cloud"
```

### 랜덤 테마 사용

```bash
ZSH_THEME="random"
```

### 사용 가능한 테마 확인

```bash
ls ~/.oh-my-zsh/themes/
```

### Powerlevel10k 테마 설치 (추천)

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

`~/.zshrc`에서 테마 설정:

```bash
ZSH_THEME="powerlevel10k/powerlevel10k"
```

터미널 재시작 후 설정 마법사가 자동으로 실행됩니다.

## 플러그인 설정

### 플러그인 활성화

`~/.zshrc` 파일의 `plugins` 배열에 플러그인 추가:

```bash
plugins=(
  git
  docker
  kubectl
  node
  npm
  python
  vscode
  macos
  brew
)
```

**주의**: 플러그인은 공백으로 구분하며 쉼표를 사용하지 않습니다.

### 추천 플러그인

#### 1. zsh-autosuggestions (자동 완성 제안)

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

`~/.zshrc`에 추가:

```bash
plugins=(... zsh-autosuggestions)
```

#### 2. zsh-syntax-highlighting (문법 강조)

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

`~/.zshrc`에 추가:

```bash
plugins=(... zsh-syntax-highlighting)
```

#### 3. zsh-completions (추가 자동 완성)

```bash
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions
```

`~/.zshrc`에 추가:

```bash
fpath+=${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions/src
plugins=(... zsh-completions)
```

### 기본 제공 유용한 플러그인

- **git**: Git 명령어 단축키 및 별칭
- **docker**: Docker 명령어 자동 완성
- **kubectl**: Kubernetes 명령어 자동 완성
- **brew**: Homebrew 자동 완성
- **node**: Node.js 개발 도구
- **python**: Python 개발 도구
- **vscode**: VS Code 관련 별칭
- **macos**: macOS 전용 유틸리티

## 업데이트 설정

### 자동 업데이트 설정

`~/.zshrc`에서 설정:

```bash
# 자동 업데이트 (기본값)
zstyle ':omz:update' mode auto

# 업데이트 알림만
zstyle ':omz:update' mode reminder

# 업데이트 비활성화
zstyle ':omz:update' mode disabled
```

### 업데이트 주기 설정

```bash
# 기본값: 14일
zstyle ':omz:update' frequency 14

# 7일마다 업데이트
zstyle ':omz:update' frequency 7
```

### 수동 업데이트

```bash
omz update
```

## 별칭(Alias) 관리

### 특정 플러그인 별칭 비활성화

`~/.zshrc`에서 oh-my-zsh.sh를 로드하기 전에 추가:

```bash
# 모든 별칭 비활성화
zstyle ':omz:*' aliases no

# Git 플러그인 별칭만 비활성화
zstyle ':omz:plugins:git' aliases no
```

### 사용자 정의 별칭 추가

`~/.zshrc` 하단에 추가:

```bash
# 사용자 정의 별칭
alias zshconfig="code ~/.zshrc"
alias ohmyzsh="code ~/.oh-my-zsh"
alias ll="ls -lah"
alias ..="cd .."
alias ...="cd ../.."
alias gs="git status"
alias ga="git add"
alias gc="git commit"
alias gp="git push"
```

## 사용자 정의 설정

### Custom 디렉토리

사용자 정의 플러그인, 테마, 설정은 다음 위치에 저장:

```bash
~/.oh-my-zsh/custom/
```

### 사용자 정의 플러그인 생성

```bash
mkdir -p ~/.oh-my-zsh/custom/plugins/my-plugin
nano ~/.oh-my-zsh/custom/plugins/my-plugin/my-plugin.plugin.zsh
```

## 삭제

### Oh My Zsh 완전 삭제

```bash
uninstall_oh_my_zsh
```

### 수동 삭제

```bash
rm -rf ~/.oh-my-zsh
rm ~/.zshrc
cp ~/.zshrc.pre-oh-my-zsh ~/.zshrc
```

## 문제 해결

### 플러그인이 작동하지 않을 때

```bash
# 캐시 재생성
rm -f ~/.zcompdump*
compinit
```

### 느린 셸 시작 시간

```bash
# 플러그인을 하나씩 비활성화하여 원인 찾기
# 또는 다음 도구로 프로파일링
time zsh -i -c exit
```

## 추천 설정 예시

완전한 `.zshrc` 설정 예시:

```bash
# Oh My Zsh 설치 경로
export ZSH="$HOME/.oh-my-zsh"

# 테마 설정
ZSH_THEME="powerlevel10k/powerlevel10k"

# 플러그인 설정
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  docker
  kubectl
  brew
  macos
  node
  python
  vscode
)

# 업데이트 설정
zstyle ':omz:update' mode auto
zstyle ':omz:update' frequency 7

# Oh My Zsh 로드
source $ZSH/oh-my-zsh.sh

# 사용자 정의 별칭
alias zshconfig="code ~/.zshrc"
alias ll="ls -lah"
alias gs="git status"

# 환경 변수
export EDITOR='vim'
export PATH="$HOME/bin:$PATH"
```

## 참고 자료

- [Oh My Zsh 공식 웹사이트](https://ohmyz.sh/)
- [Oh My Zsh GitHub](https://github.com/ohmyzsh/ohmyzsh)
- [Oh My Zsh Wiki](https://github.com/ohmyzsh/ohmyzsh/wiki)
- [Powerlevel10k 테마](https://github.com/romkatv/powerlevel10k)
- [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)

## 추천 조합

iTerm2 + Oh My Zsh + Powerlevel10k + 플러그인 조합으로 최상의 터미널 환경을 구성할 수 있습니다.
