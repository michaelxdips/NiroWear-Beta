<div align="center">

# NiroWear

**Your AI. Your key. On your wrist.**

An AI chat app for Wear OS: bring your own API key, choose a model, and read streamed answers on your watch.

**Public beta · 0.1.0-beta.1 · Sideload only**

[Download the published APK](https://github.com/michaelxdips/NiroWear-Beta/releases/download/v0.1.0-beta.1/NiroWear-0.1.0-beta.1.apk) · [Release notes](https://github.com/michaelxdips/NiroWear-Beta/releases/tag/v0.1.0-beta.1)

</div>

## Start here

- [User guide](docs/USER_GUIDE.md): installation, provider setup, first chat, and reading controls.
- [Troubleshooting and FAQ](docs/TROUBLESHOOTING.md): safe recovery steps and known limitations.
- [Contribute](CONTRIBUTING.md): improve public docs and tooling, share device or accessibility feedback, or request collaboration.
- [Report a problem](https://github.com/michaelxdips/NiroWear-Beta/issues/new/choose): nonconfidential bugs and feedback.

**Contributors welcome.** Documentation fixes, public repository tooling PRs, test cases, and careful device/accessibility feedback all help. Application source is private and proprietary; source collaboration requires an owner-reviewed [collaboration issue](https://github.com/michaelxdips/NiroWear-Beta/issues/new?template=developer-collaboration.yml), not an automatic access grant.

## See it on a round screen

<table>
  <tr>
    <td align="center"><img src="docs/screenshots/chat-home.png" width="144" height="144" alt="NiroWear chat home with keyboard and voice input icons" /><br /><strong>Keyboard and voice</strong></td>
    <td align="center"><img src="docs/screenshots/real-response.png" width="144" height="144" alt="An AI answer displayed in the NiroWear document reader" /><br /><strong>Full answers</strong></td>
  </tr>
  <tr>
    <td align="center"><img src="docs/screenshots/streaming-stop.png" width="144" height="144" alt="An answer streaming with the Stop control visible" /><br /><strong>Streaming and Stop</strong></td>
    <td align="center"><img src="docs/screenshots/table-record.png" width="144" height="144" alt="A Markdown table shown as labeled vertical records" /><br /><strong>Watch-sized tables</strong></td>
  </tr>
  <tr>
    <td align="center"><img src="docs/screenshots/code-reader.png" width="144" height="144" alt="A Kotlin code block in a horizontally pannable reader" /><br /><strong>Readable code</strong></td>
    <td align="center"><img src="docs/screenshots/history.png" width="144" height="144" alt="Saved conversations in NiroWear History" /><br /><strong>Local history</strong></td>
  </tr>
</table>

Six real, uncropped 466 × 466 emulator captures. Each shows one scroll or pan position, not an entire answer squeezed onto one screen. These are not mockups or proof of physical-watch compatibility.

## What the published beta does

### Choose your provider and model

NiroWear connects directly to your configured HTTPS API endpoint using your own key. Four choices are available in **Menu → Providers / model**:

| Add option | Supported generation API |
|---|---|
| **Add OpenAI** | OpenAI Responses |
| **Add Anthropic** | Anthropic Messages |
| **Add Gemini** | Gemini streaming GenerateContent |
| **Add compatible** | OpenAI-compatible Chat Completions |

Choose the API your endpoint supports; a model name does not establish its protocol or who operates it. Live coverage across all four upstream services is incomplete.

**Discover models** retrieves a catalog; **Manual model ID** lets you enter an exact ID, including when compatible-endpoint discovery is unavailable. A listed model is not necessarily usable for text generation. **Validate · uses API** sends a small generation request and can incur charges. Saving a new profile does not itself prove generation works. Replacing a saved key requires validation and performs another validation during save.

Key entry is masked. Saved keys use Android Keystore-backed AES-GCM encryption; editing a profile never fills its saved key into the input field. Leave that field blank to retain the existing key. Secure-storage failure requires re-entry, with no plaintext fallback.

### Ask, stream, and revise

- **Keyboard:** open **Prompt**, type with your installed Wear keyboard, then tap **Send**.
- **Voice:** use the system speech recognizer, then review or correct returned text in **Prompt** before sending. Recognizer availability varies; real spoken transcription has not been fully verified.
- **Streaming:** read answers as they arrive. **Stop** cancels the client request and keeps received partial text. It cannot guarantee that the provider stops computation or billing.
- **Retry:** the circular-arrow control, labeled **Retry response** for accessibility, replaces the latest assistant response with a new request using the selected provider/model. No alternate versions are kept.
- **Edit:** long-press an earlier user message, change it, then choose **Edit & resend**. This replaces that message and permanently deletes every later message in that conversation before generating a new continuation. There is no branch or undo copy.

Retry and edit/resend are explicit new API requests and may incur charges. Failed or interrupted streams are not automatically replayed. Provider/model switching is available while idle and keeps the same linear conversation; earlier assistant messages retain their original provider/model labels.

### Read and return

- **History** opens saved local conversations. **New chat** starts a separate conversation without deleting existing ones.
- Near the bottom, the reader follows incoming text. Scroll upward to read earlier content without being pulled back down. The down-arrow **Latest** action, labeled **Jump to latest**, returns to the tail.
- Assistant answers appear as a scrollable document, not oversized chat bubbles. Detailed answers remain available; ask explicitly for detail, examples, or steps when needed.
- **Markdown:** paragraphs, headings, lists, quotes, emphasis, inline code, and dividers.
- **Unicode:** mathematical symbols, Greek letters, and other scripts use device fonts; glyph coverage varies.
- **Code:** fenced blocks preserve formatting and use monospace text. Pan horizontally inside wide blocks, then scroll vertically through the answer.
- **Tables:** rows become vertical records with column labels, rather than a tiny desktop grid.
- **Math:** Unicode and LaTeX source remain readable, with horizontal pan for wide formulas. **Native formula typesetting is unavailable.** Fractions, roots, matrices, cases, and aligned equations remain source text rather than typeset layouts.
- **Links:** HTTP(S) links hand off to available Android/Wear handlers. There is no built-in browser; reaching the destination depends on your watch/phone setup and has not been fully verified.

## Download and install

The current published release is **0.1.0-beta.1**, published **2026-10-10**. Download the APK, not GitHub's automatic source archives: those contain public landing files, not buildable application source.

Minimum: **Wear OS 3 or newer with Android API 30 or newer**. The reference evaluation setup is a round **466 × 466 Wear OS 5 / API 34 emulator**. Minimum requirements are not a tested-device list; broad physical-watch support is unverified. No Play Store release is available.

| Published APK identity | Value |
|---|---|
| Download | [NiroWear-0.1.0-beta.1.apk](https://github.com/michaelxdips/NiroWear-Beta/releases/download/v0.1.0-beta.1/NiroWear-0.1.0-beta.1.apk) |
| Package | `com.nirowear` |
| Version / versionCode | `0.1.0-beta.1` / `2` |
| Size | 25,994,739 bytes |
| SHA256 | `25b091753743c5b439bb1413525ddef9f69a28d81bd7dae9773013e32605fdb7` |
| Signing certificate SHA256 | `7d4e6e99821d904f23900bd4e0cad5b64b1a2733a28243dcc8ab9d6e2768abe3` |

**Signing caution:** this nondebuggable APK uses an owner-approved Android Debug certificate as its beta update identity. That is not production-grade signing. See [security guidance](SECURITY.md).

1. Download the APK and verify its SHA256 against the value above.
2. Pair/connect Android SDK Platform Tools with your intended watch using its supported debugging workflow.
3. Check `adb devices -l`, then install with `adb -s <serial> install NiroWear-0.1.0-beta.1.apk`.
4. Open NiroWear, tap the top header for **Menu**, and open **Providers / model**.
5. Add the correct provider type, HTTPS API base, key, and model ID. Choose **Save securely**, return with **Back**, then use the keyboard icon to send a first prompt.

The [user guide](docs/USER_GUIDE.md#install-the-apk) includes checksum, pairing, update, and provider setup steps.

**Do not uninstall or clear app data to bypass a signing mismatch.** Doing so can permanently remove conversations, settings, and access to stored keys. There is no user-facing conversation export or deletion control in this beta.

## Limitations worth knowing

This is an evaluation beta, not a production-certified release.

- Full signed-beta reader, table, font, restoration, and horizontal-pan coverage is incomplete.
- Physical-watch touch, battery, thermals, accessibility, and broad compatibility are not fully verified. Human visual review of the protected provider editor is incomplete.
- Genuine spoken transcription and complete external-link destinations are not fully verified.
- Broad live upstream coverage is incomplete. Observed genuine requests used a configured third-party HTTPS Responses endpoint; a displayed model/provider name does not prove official upstream identity.
- Native math typesetting is unavailable. Source fallback is the actual published behavior.
- History stays on the device, is not separately encrypted, and has no NiroWear cloud backup. Uninstalling or clearing data can remove it permanently.

See [troubleshooting and FAQ](docs/TROUBLESHOOTING.md) before resetting anything.

## Privacy, safety, and feedback

Your key and requested conversation context go to your selected endpoint. Switching providers and sending again shares the retained conversation context with the new endpoint. Its operator controls processing, retention, and charges. There is no separate NiroWear relay or account, and no configured analytics or crash-reporting SDK. System voice processing follows the recognizer's policies. Read [PRIVACY.md](PRIVACY.md).

AI answers can be false, incomplete, or outdated. Check important claims independently. You are responsible for meeting your provider's account, region, age, and use restrictions; availability in the app is not permission to use a service.

**GitHub Issues are public. Never post API keys, authentication headers, pairing codes, private conversations, or unredacted credential-screen captures. Report vulnerabilities through [GitHub private vulnerability reporting](https://github.com/michaelxdips/NiroWear-Beta/security/advisories/new), not public issues.**

## Copyright and notices

Copyright © 2026 Stephen Michael, for first-party NiroWear material. Application source is proprietary and not open-source. Public availability of this distribution/documentation repository does not grant a blanket reuse license. See [COPYRIGHT.md](COPYRIGHT.md).

Third-party components, icons, and other materials retain their respective owners' rights and license terms. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), [SECURITY.md](SECURITY.md), and [published release history](CHANGELOG.md).
