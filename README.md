<div align="center">

# NiroWear

**Your AI. Your key. On your wrist.**

Wear OS chat with keyboard, system voice input and streamed answers built for reading—not oversized chat bubbles.

**Public beta · 0.1.0-beta.1 · Sideload only**

[Download APK](https://github.com/michaelxdips/NiroWear-Beta/releases/download/v0.1.0-beta.1/NiroWear-0.1.0-beta.1.apk) · [Release notes](https://github.com/michaelxdips/NiroWear-Beta/releases/tag/v0.1.0-beta.1) · [Feedback](https://github.com/michaelxdips/NiroWear-Beta/issues/new/choose)

</div>

## Watch-first, full-length answers

Bring your own provider, choose your model, ask by keyboard or voice, then read complete answers as a scrollable document. Long answers stay long; layout adapts to the watch.

<table>
  <tr>
    <td align="center"><img src="docs/screenshots/chat-home.png" width="200" height="200" alt="NiroWear chat home with keyboard and voice input icons" /><br /><strong>Ask from your wrist</strong></td>
    <td align="center"><img src="docs/screenshots/real-response.png" width="200" height="200" alt="Real AI answer in NiroWear document reader" /><br /><strong>Read full answers</strong></td>
  </tr>
  <tr>
    <td align="center"><img src="docs/screenshots/streaming-stop.png" width="200" height="200" alt="Answer streaming with Stop control visible" /><br /><strong>Stream + Stop</strong></td>
    <td align="center"><img src="docs/screenshots/table-record.png" width="200" height="200" alt="Markdown table adapted into labeled records" /><br /><strong>Watch-sized tables</strong></td>
  </tr>
  <tr>
    <td align="center"><img src="docs/screenshots/code-reader.png" width="200" height="200" alt="Kotlin code block in horizontally pannable reader" /><br /><strong>Readable code</strong></td>
    <td align="center"><img src="docs/screenshots/history.png" width="200" height="200" alt="Saved conversations in NiroWear History" /><br /><strong>Keep conversations</strong></td>
  </tr>
</table>

Six genuine, uncropped 466 × 466 captures from the preceding signed validation candidate. No mock UI or generated artwork. Beta.1 removes developer fixture packaging; visible product design is unchanged. Each image shows one scroll/pan viewport, not an entire answer fitted onto one screen.

## Features and controls

### BYOK with secure key entry

Tap the top header to open **Menu**, then **Providers / model**. Choose **Add OpenAI**, **Add Anthropic**, **Add Gemini** or **Add compatible**. Fields: **Name**, **Base URL**, **Manual model ID**, **API key**.

Keys start masked; **Reveal key** / **Hide key** affect current entry only. **Save securely** stores Android Keystore-backed AES-GCM ciphertext; profiles hold credential references, not plaintext keys. **Edit / replace key** opens with a blank key field: leave it blank to retain the saved key. Decryption failure requires re-entry, never plaintext fallback. Provider screens use secure-window protection.

### Four adapters—not one guessed protocol

| Entry | Generation API | Model discovery |
|---|---|---|
| **Add OpenAI** | Native OpenAI Responses | Dynamic IDs; listing does not establish text-generation compatibility |
| **Add Anthropic** | Native Anthropic Messages | Paginated model catalog |
| **Add Gemini** | Native Google Gemini GenerateContent streaming | Paginated catalog filtered for `generateContent` support |
| **Add compatible** | OpenAI-compatible Chat Completions | Endpoint-dependent; manual ID works without discovery |

**Discover models** lists choices; it is not proof that the selected model can generate. **Validate · uses API** performs a generation request to check credential access and selected-model usability, and can incur provider charges. Discovery, authentication and generation are separate outcomes. Saving a new profile is not a successful generation test; replacing a saved key requires validation, including a check during secure save.

Native Responses and compatible Chat Completions are distinct adapters. Select the protocol your endpoint supports; model names do not choose protocols or prove official upstream identity. Implemented adapters do not mean every upstream service has genuine live acceptance.

### Manual models and mid-chat switching

Enter **Manual model ID** or select a discovered ID. Compatible endpoints remain usable when model discovery fails; NiroWear does not silently choose another model.

While idle, open **Providers / model** and tap a profile to select it, or use **Edit / replace key** to change its model and **Save securely**. Switching preserves one linear conversation. Each assistant message retains the provider profile ID and model ID that produced it; a later switch does not rewrite earlier provenance. Providers/model switching is disabled during generation.

### Keyboard input

Tap the keyboard icon, accessibility label **Keyboard input**, to open **Prompt**. Tap the text field to use your installed Wear keyboard, then **Send**. Keyboard input remains available when voice recognition is missing.

### System voice input

Tap the microphone icon, accessibility label **Voice input**. NiroWear delegates to the installed system speech recognizer. Returned text opens **Prompt** for review or correction before **Send**; speech is not automatically sent to your AI provider. Recognizer availability and speech processing depend on your system setup. Real spoken-transcription acceptance remains outstanding.

### Streamed reader and Stop

Answers arrive incrementally through direct-to-provider requests and render as document blocks. **Stop** cancels the underlying HTTP call and retains partial content with stopped status. Interrupted or failed streams keep received text; NiroWear does not automatically replay them. Input resumes after generation settles.

Stop cannot guarantee that remote computation or billing stops. Requests go to your configured endpoint, whose policies and charges apply.

### Retry

After an assistant turn, scroll to the circular-arrow icon, accessibility label **Retry response**. Retry removes the latest assistant response and generates a new continuation from the preceding user turn, using the currently selected provider/model. No alternate variants or branches. Retry is an explicit new API request and can incur charges.

### Linear Edit

While idle, long-press an earlier user message to open **Prompt**, then choose **Edit & resend**.

**This replaces that user message and permanently deletes every later message in that conversation before requesting a new continuation. There is no branch or undo copy.**

### History and New chat

**Menu**, then **History**, opens saved conversations. Tap a title to resume. Raw user/assistant content, including original assistant Markdown and provider/model provenance, stays in local application data.

**New chat**, available in Menu and History while idle, starts a separate conversation without deleting existing ones. History has no NiroWear cloud backup. Conversation text is not separately encrypted; clearing app data or uninstalling can permanently remove it.

### Latest without forced scrolling

Near the bottom, the reader follows incoming content. Scroll upward to read earlier text without being pulled back down. A down-arrow icon, accessibility label **Jump to latest**, returns to the current tail. This is the **Latest** action; it is an icon, not a text button.

### Markdown

Headings, paragraphs, bullet and numbered lists, quotes, bold/italic text, inline code and dividers render as semantic blocks. Assistant output is not one giant text node. Raw Markdown remains stored so rendering can evolve without losing the original response.

### Unicode and symbols

Unicode text—including Greek letters, mathematical operators and non-Latin scripts—uses Android system font fallback. Readability still depends on available device fonts; broad physical-watch typography and accessibility acceptance is not complete.

### Code blocks

Fenced code uses monospace text and preserves source formatting, with a language label when supplied. Pan horizontally inside wide code blocks; scroll vertically through the document. NiroWear does not shrink whole code samples to fit the round screen.

### Tables

Markdown tables become vertical records: each cell follows its column heading. Rows remain readable without squeezing a desktop grid onto the watch. Scroll to read all records.

### Math: readable source, not native typesetting

Beta.1 retains Unicode math and LaTeX source for inline/display formulas, fractions, roots, powers/subscripts, calculus, matrices, cases and aligned equations. Wide formulas use horizontal pan rather than unreadable shrinking.

**Native formula typography is unavailable in this beta.** Fractions, matrices and similar LaTeX structures remain source text, not typeset layouts. No debug math engine or math fonts are bundled. Source fallback is a limited-beta exception, not completion of native-math acceptance.

### Links

HTTP(S) links hand off to available Android/Wear handlers. NiroWear has no built-in browser. Opening the final destination depends on watch/phone handlers; complete external-link acceptance remains outstanding.

## Download and install

Requires **Wear OS with Android API 30 or newer**. Reference setup: **Wear OS 5 / API 34, round 466 × 466 emulator**. Minimum API does not certify every watch; physical-watch acceptance is not complete. No Play Store release is available.

### Published beta.1 identity

| Field | Published value |
|---|---|
| Release | [0.1.0 Beta 1](https://github.com/michaelxdips/NiroWear-Beta/releases/tag/v0.1.0-beta.1), published 2026-10-10 |
| APK | [`NiroWear-0.1.0-beta.1.apk`](https://github.com/michaelxdips/NiroWear-Beta/releases/download/v0.1.0-beta.1/NiroWear-0.1.0-beta.1.apk) |
| Package | `com.nirowear` |
| Version / versionCode | `0.1.0-beta.1` / `2` |
| Size | 25,994,739 bytes |
| APK SHA256 | `25b091753743c5b439bb1413525ddef9f69a28d81bd7dae9773013e32605fdb7` |
| Certificate SHA256 | `7d4e6e99821d904f23900bd4e0cad5b64b1a2733a28243dcc8ab9d6e2768abe3` |

**Signing warning:** the owner approved the existing Android Debug certificate as this beta's update identity, not as production-grade signing. The published APK is nondebuggable. Local signing recovery was established; off-device recovery remains unverified. Future binary updates require the same approved identity, a new version/tag and a versionCode above `2`; the beta.1 asset must not be silently replaced.

Local `0.1.0-beta.2-dev` optimization work is unpublished. It does not change the beta.1 download, hash or certificate above, and is not a claim of a shipped optimized binary.

1. Download the linked beta.1 APK and verify its SHA256 against the value above and release notes.
2. Enable developer options and supported ADB/wireless debugging on your watch. Follow its pairing instructions using Android SDK Platform Tools.
3. Confirm the target with `adb devices -l`. Where supported, use `adb pair <watch-ip>:<pair-port>` and `adb connect <watch-ip>:<debug-port>`. Keep pairing codes private.
4. Install only on the intended watch: `adb -s <serial> install NiroWear-0.1.0-beta.1.apk`. For a same-certificate update, use `adb -s <serial> install -r NiroWear-0.1.0-beta.1.apk`.
5. Open NiroWear, tap the top header, then **Providers / model**. Add the correct adapter, HTTPS base URL, your own key and model ID; choose **Save securely**. Saving selects that profile.
6. Return with **Back**. Tap the keyboard or microphone icon, review the prompt, then **Send**.

**Do not uninstall or clear valuable history to work around a signing mismatch.** Updates require a matching certificate; uninstalling or clearing app data can permanently remove conversations, settings and access to stored keys.

This repository contains the public beta landing page, screenshots, notices and feedback forms—not application source. GitHub's automatic source archives contain landing files, not buildable app code. No app build instructions are provided here. NiroWear application source is proprietary, not open-source.

## Known beta limitations

- **Software release acceptance remains partial; general availability (GA) is blocked.** Publication is a limited beta, not production acceptance.
- Complete signed beta.1 reader/table/font/restoration coverage and horizontal-pan endpoints remain partial. Historical signed-reader observations and controlled debug checks are not complete acceptance of this published binary.
- Native math typography is unavailable; readable/pannable LaTeX source is the beta fallback.
- Physical-watch touch, battery, thermals, broad compatibility and hardware accessibility remain unaccepted. Protected provider-editor human visual review is also incomplete.
- System voice intent handling is implemented, but genuine spoken transcription has not completed acceptance.
- HTTP(S) handoff is implemented, but complete external-link destination acceptance is missing.
- Broad genuine upstream coverage across all four adapters is incomplete. Genuine network observations used a configured third-party HTTPS Responses endpoint, not verified official upstream identity.
- Beta-only debug-certificate identity is not production-grade signing; off-device signing recovery is unverified.

## Roadmap

Acceptance gates, not promised dates or speculative features:

| Stage | Focus |
|---|---|
| **Current** | Published limited beta.1; collect nonsecret feedback while keeping download identity and limitations explicit |
| **Next** | Close signed-reader/pan coverage, physical-watch and protected-editor/accessibility review, real voice/link completion and genuine upstream adapter acceptance; verify off-device signing recovery |
| **Later** | Native math typography with cleared dependency/font rights, production signing and remaining legal/privacy/distribution acceptance before GA |

## Privacy, security and feedback

Keys and requested conversation context go directly to your selected endpoint. Its operator controls remote processing, retention and billing. Release requests require HTTPS with platform trust. No separate NiroWear relay, analytics SDK or crash-reporting SDK is configured. Android backup is disabled in the manifest; device-transfer behavior can vary by OEM. System speech processing follows your recognizer's policies. Read [privacy facts](PRIVACY.md) and [security guidance](SECURITY.md).

[Report a bug or request a feature](https://github.com/michaelxdips/NiroWear-Beta/issues/new/choose). For bugs, include watch model, Wear OS version, beta version, reproduction steps, expected result and actual result. Feature requests should explain the user problem and watch use case. Nonsecret screenshots are optional.

**GitHub Issues are public. Never post API keys, authentication headers, provider credentials, pairing codes, private conversation exports or unredacted secure-screen captures. Do not post exploit details publicly; follow [SECURITY.md](SECURITY.md).**

## License & Legal

© 2026 Stephen Michael, for first-party NiroWear material only. NiroWear application source is proprietary and is not published here. This landing repository supports beta distribution, documentation, screenshots and feedback; public availability does not grant a blanket reuse license. See [copyright notice](COPYRIGHT.md). No project-wide open-source license is granted.

Third-party components and materials retain their respective owners' rights and license terms; the first-party notice does not claim ownership of them. [Third-party notices](THIRD_PARTY_NOTICES.md) and required license/data materials accompany the application and this repository.

NiroWear is beta software and may contain defects or incomplete behavior. It is not production-certified or commercially supported. Attribution corrections can use a nonconfidential [GitHub Issue](https://github.com/michaelxdips/NiroWear-Beta/issues/new/choose); sensitive security concerns use [private reporting](https://github.com/michaelxdips/NiroWear-Beta/security/advisories/new). See [Changelog](CHANGELOG.md) for published history and unreleased landing-page changes.

AI responses may be false, incomplete or outdated. Independently check factual claims before relying on or sharing them. API availability does not establish that your account, region or intended use meets provider terms.
