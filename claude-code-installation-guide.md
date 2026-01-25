# macOS에 Claude Code 설치하기

## 시스템 요구사항

- **운영체제**: macOS 13.0 이상
- **하드웨어**: 4GB 이상 RAM
- **네트워크**: 인터넷 연결 필수
- **Shell**: Bash 또는 Zsh 권장
- **지역**: [Anthropic 지원 국가](https://www.anthropic.com/supported-countries)

## 설치 방법

### 1. Native 설치 (권장)

Native 설치는 Node.js가 필요 없으며 자동 업데이트를 지원합니다.

터미널을 열고 다음 명령어를 실행하세요:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

설치가 완료되면 프로젝트 디렉토리로 이동하여 Claude Code를 실행합니다:

```bash
cd your-awesome-project
claude
```

설치 확인:

```bash
claude doctor
```

### 2. Homebrew 설치 (대안)

Homebrew를 사용하여 설치할 수도 있습니다:

```bash
brew install --cask claude-code
```

**주의**: Homebrew 설치는 자동 업데이트되지 않습니다. 최신 버전으로 업데이트하려면:

```bash
brew upgrade claude-code
```

## 인증 설정

### 개인 사용자

1. **Claude Pro 또는 Max 플랜** (권장): [Claude Pro/Max](https://claude.ai/pricing)에 가입하고 Claude.ai 계정으로 로그인
2. **Claude Console**: [Claude Console](https://console.anthropic.com)을 통해 OAuth 프로세스를 완료 (활성화된 결제 필요)

### 팀 및 조직

1. **Claude for Teams 또는 Enterprise** (권장): 중앙 집중식 결제 및 팀 관리
2. **Claude Console 팀 결제**: 공유 조직 설정 및 팀원 초대
3. **클라우드 제공업체**: Amazon Bedrock, Google Vertex AI, Microsoft Foundry 사용 가능

## 특정 버전 설치

### 최신 버전 (기본값)

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Stable 버전

```bash
curl -fsSL https://claude.ai/install.sh | bash -s stable
```

### 특정 버전 번호

```bash
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
```

## 업데이트

### 자동 업데이트

Native 설치는 백그라운드에서 자동으로 업데이트됩니다.

- 시작 시 및 실행 중 주기적으로 업데이트 확인
- 백그라운드에서 자동 다운로드 및 설치
- 다음 실행 시 업데이트 적용

### 수동 업데이트

```bash
claude update
```

### 자동 업데이트 비활성화

환경 변수를 설정:

```bash
export DISABLE_AUTOUPDATER=1
```

## 삭제

### Native 설치 삭제

```bash
rm -f ~/.local/bin/claude
rm -rf ~/.local/share/claude
```

### Homebrew 설치 삭제

```bash
brew uninstall --cask claude-code
```

### 설정 파일 삭제 (선택사항)

**경고**: 모든 설정, 도구 권한, MCP 서버 구성, 세션 기록이 삭제됩니다.

```bash
# 사용자 설정 및 상태 제거
rm -rf ~/.claude
rm ~/.claude.json

# 프로젝트별 설정 제거 (프로젝트 디렉토리에서 실행)
rm -rf .claude
rm -f .mcp.json
```

## 보안 및 무결성

- **코드 서명**: "Anthropic PBC"가 서명하고 Apple이 공증한 바이너리
- **체크섬**: 모든 릴리스에 대해 SHA256 체크섬이 게시됨

## 참고 자료

- [공식 설치 가이드](https://code.claude.com/docs/en/setup)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Homebrew Formula](https://formulae.brew.sh/cask/claude-code)
- [설치 가이드 (MacPaw)](https://macpaw.com/how-to/install-claude-code-mac)
