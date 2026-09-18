# ChatGPT Action Playbooks

This folder contains reusable action playbooks for ChatGPT when it works on this repository through Shellby. They are **not slash commands** and are not auto-loaded. ChatGPT should read the relevant playbook when the user's natural-language request matches its purpose.

Local file access:
- **sSb**: Mac Studio
- **mSb**: MacBook

Core examples:
- “근거 찾아서 evidence에 등록해줘” → `search-evidence.md`
- “이 DOI 추가해줘” → `import-doi.md`
- “전체 검증해” → `verify.md`
- “학술적으로 다듬어줘” → `style-pass.md`
- “critical review 해” → `critical-review.md`
- “editor review 해” → `editor-review.md`
- “논문 방향을 토론해봐” → `paper-debate.md`

`CHATGPT.md` is the source of truth. These playbooks must not override its phase gates, citation rules, oncology methods, or Git safety rules.
