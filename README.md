<div align="center">

# NiroWear

**Watch-first AI chat with your own provider and API key.**

<img src="docs/screenshots/chat-home.png" width="233" height="233" alt="NiroWear chat home with keyboard and voice controls" />
<img src="docs/screenshots/real-response.png" width="233" height="233" alt="Real AI response in NiroWear document reader" />

**0.1.0 Beta 1 · Wear OS · sideload distribution**

[Beta releases](https://github.com/michaelxdips/NiroWear-Beta/releases) · [Report a bug](https://github.com/michaelxdips/NiroWear-Beta/issues/new/choose) · [Privacy](PRIVACY.md) · [Notices](THIRD_PARTY_NOTICES.md)

</div>

## Beta availability

Download **`NiroWear-0.1.0-beta.1.apk`** from [Beta releases](https://github.com/michaelxdips/NiroWear-Beta/releases). Until final verification completes, the release remains a private draft. No Play Store installation is available.

APK SHA256: `25b091753743c5b439bb1413525ddef9f69a28d81bd7dae9773013e32605fdb7`.

This repository is a binary-beta landing page, not the application source repository. Native math and physical-device acceptance remain beta evaluation work, not completed production-release claims.

## Features

- **BYOK:** your endpoint, API key and model. Encrypted local key storage; manual model IDs supported.
- **Four adapters:** OpenAI Responses, Anthropic Messages, Google Gemini GenerateContent and OpenAI-compatible Chat Completions.
- **Streaming and Stop:** incremental answers; Stop cancels the HTTP call and keeps partial content.
- **Retry and linear Edit:** replace a response, or edit a user message and regenerate after deleting later turns. No branches or automatic replay.
- **History and Latest:** saved conversations, provider/model provenance and manual scrolling without forced jumps.
- **Keyboard and Voice intent:** native Wear input; speech recognition depends on the installed system recognizer.
- **Document-style reading:** Markdown, labeled table records, pannable code, Unicode and readable/pannable LaTeX source fallback.

Implemented adapters are not a claim that all upstream services were independently live-tested. Genuine network validation used a configured third-party HTTPS Responses endpoint; configured model names do not prove official upstream identity.

## Actual watch screenshots

Uncropped 466 × 466 NiroWear captures from the preceding signed validation candidate. No mock UI or generated artwork. Beta removes developer fixture packaging; visible product design is unchanged. Screens show normal scroll/pan viewports, not whole-answer simultaneous fit.

<table>
  <tr>
    <td align="center"><img src="docs/screenshots/streaming-stop.png" width="233" height="233" alt="Active streaming response and Stop button" /><br /><strong>Streaming + Stop</strong></td>
    <td align="center"><img src="docs/screenshots/table-record.png" width="233" height="233" alt="Markdown table rendered as labeled records" /><br /><strong>Watch-sized tables</strong></td>
  </tr>
  <tr>
    <td align="center"><img src="docs/screenshots/code-reader.png" width="233" height="233" alt="Kotlin code block with horizontal panning" /><br /><strong>Readable code</strong></td>
    <td align="center"><img src="docs/screenshots/history.png" width="233" height="233" alt="NiroWear conversation history" /><br /><strong>Saved conversations</strong></td>
  </tr>
</table>

## Install on Wear OS

Android API 30 or newer is required, on a Wear OS device. Reference emulator: Wear OS 5/API 34, round 466 × 466. Physical-watch compatibility is still being evaluated; minimum API alone does not certify every watch.

1. Download the APK from [Releases](https://github.com/michaelxdips/NiroWear-Beta/releases) once a beta is published. Verify its SHA256 against the release notes.
2. Enable your watch's developer options and supported ADB/wireless debugging. Use Android SDK Platform Tools and your watch's pairing instructions.
3. Confirm device identity with `adb devices -l`. For wireless debugging, use `adb pair <watch-ip>:<pair-port>` and `adb connect <watch-ip>:<debug-port>` when supported. Enter pairing secrets locally, never in bug reports.
4. Install only on the intended watch: `adb -s <serial> install NiroWear-0.1.0-beta.1.apk`.
5. Open NiroWear. In Menu → Providers, add the appropriate adapter, HTTPS base URL, your own key and accessible model ID. Save/select, then return to chat.
6. Choose Keyboard or Voice, review text, then Send. Scroll upward to detach; Latest returns to current content.

Existing installations require the same signing certificate for updates. Do not uninstall or clear valuable history to work around a signature mismatch. Approved future updates will use increasing version codes and the established beta identity.

Owner approved the existing Android Debug certificate for this beta update identity, not for production: SHA256 `7d4e6e99821d904f23900bd4e0cad5b64b1a2733a28243dcc8ab9d6e2768abe3`. Release APK is nondebuggable. This signing identity is beta-only; do not treat it as production-grade trust.

## Privacy & security

API keys use Android Keystore-backed AES-GCM. Profiles store credential references; saved key values are not repopulated into editor fields. Provider screens retain secure-window protection. Release requests use HTTPS with platform trust and no automatic replay.

Your key and conversation context go directly to your selected endpoint for requested operations. Its operator controls remote processing, retention and billing. Stop does not guarantee remote computation or billing stops. Conversation history is local; backup is disabled. No analytics SDK or separate NiroWear relay is configured. See [privacy facts](PRIVACY.md).

## Known beta limitations

- **Native math typesetting unavailable:** formulas use source fallback; no bundled debug math engine/fonts.
- Physical watch touch, battery, thermals and broad compatibility remain under evaluation.
- Voice transcription depends on system recognizer; opening the voice intent is not proof of accurate spoken transcription.
- External links depend on Wear/phone handlers; destination completion has not been accepted in the available setup.
- Not all adapters have genuine live upstream smoke coverage. Custom endpoints may differ from official services.
- Protected provider-editor human visual review and complete hardware accessibility acceptance remain outstanding.
- Fresh release pan-endpoint automation was limited by host History-row targeting; native formula typesetting is not claimed. Current controlled debug gesture tests passed.

## Feedback

Use [GitHub Issues](https://github.com/michaelxdips/NiroWear-Beta/issues/new/choose). Include watch model, Wear OS version, NiroWear beta version, steps, expected result and actual result. A nonsecret screenshot is optional.

**Never post API keys, Authorization headers, pairing codes, private conversations, provider credentials or unredacted secure-screen captures.** No analytics or crash-reporting SDK is added for beta feedback.

## License & attribution

This page does not grant a license to NiroWear source code. No project-wide open-source license has been established; source is not published here. Binary distribution requires owner approval.

Third-party components retain their licenses. [Third-party notices](THIRD_PARTY_NOTICES.md) and required texts/data are provided with the application and this repository. No debug JLaTeXMath or math font dependency is included in the beta release configuration.
