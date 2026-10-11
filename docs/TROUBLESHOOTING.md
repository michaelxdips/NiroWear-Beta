# Troubleshooting and FAQ

For published **0.1.0-beta.1** only. Start with the symptom below, preserve valuable data, and report what you observed without secrets.

[User guide](USER_GUIDE.md) · [README](../README.md) · [Feedback forms](https://github.com/michaelxdips/NiroWear-Beta/issues/new/choose)

## Before changing anything

- Check the app version, watch model, Wear OS version, and whether this is a physical watch or emulator.
- Note the exact visible error and the action that preceded it.
- Stop repeated sends or validations if they keep failing; requests may incur provider charges.
- Do not clear data, uninstall, delete a provider, or disable secure-screen protection as a first troubleshooting step.

**Uninstalling or clearing app data can permanently remove local history, settings, and access to stored keys. This beta has no user-facing conversation export. Never post keys, authentication headers, pairing codes, private conversations, raw diagnostic dumps, or unredacted credential-screen captures.**

## Installation and updates

| Symptom | Safe steps | Useful report details |
|---|---|---|
| APK checksum differs | Do not install. Download again from the [published release](https://github.com/michaelxdips/NiroWear-Beta/releases/tag/v0.1.0-beta.1) and calculate SHA256 again. | File name, file size, computed hash, download URL; no personal file paths needed. |
| Watch does not appear in ADB | Check the watch's debugging screen and connection. Run `adb devices -l`. For supported wireless debugging, distinguish pairing and connection ports. | Watch/OS, Platform Tools version, sanitized error; omit addresses and pairing codes if private. |
| `INSTALL_FAILED_OLDER_SDK` | Check Android API level. The APK requires API 30+ and Wear OS 3+. Do not try to bypass the requirement. | Watch model, Wear OS and Android versions/API if known. |
| `INSTALL_FAILED_UPDATE_INCOMPATIBLE` or certificate mismatch | Confirm package and certificate against the published identity. Keep the existing app and data; do not uninstall to bypass the mismatch. | Existing version, APK source, exact error, whether it is a new install or update. |
| Version downgrade rejected | Check the installed version and versionCode. Do not force a downgrade over valuable data. | Installed version and the requested APK version. |
| App exits or will not open | Confirm the APK hash and intended target. Reopen once; if the problem repeats, stop and report. Do not reset app data. | Version, device, exact launch steps, visible result and repeatability. |

Published APK SHA256:

```text
25b091753743c5b439bb1413525ddef9f69a28d81bd7dae9773013e32605fdb7
```

Package: `com.nirowear`; versionCode: `2`. Certificate SHA256:

```text
7d4e6e99821d904f23900bd4e0cad5b64b1a2733a28243dcc8ab9d6e2768abe3
```

The nondebuggable beta uses an owner-approved Android Debug certificate, not production-grade signing. A matching filename alone does not establish a matching APK or certificate.

## Provider setup and model discovery

| Symptom | Safe steps | Useful report details |
|---|---|---|
| “Add or select provider from menu.” | Tap the top header, open **Providers / model**, and select a saved profile or add one. | Whether a profile appears selected; do not include its key. |
| Save fails on a new profile | Check nonblank name, exact model ID, API key, and valid HTTPS API base. Saving is not a generation test. | Provider type and sanitized error; omit credential fields. |
| Models unavailable or discovery fails | Check the endpoint's documented model ID. Enter it in **Manual model ID**; compatible endpoints do not require successful discovery. | API type, public endpoint operator if safe, model ID if nonconfidential, visible message. |
| Models listed but validation fails | A catalog does not prove text-generation access. Check selected model capability and account permission. Choose the correct API type from endpoint documentation. | Whether discovery or generation failed, chosen API type, safe model ID, exact visible error. |
| Replacement key cannot be saved | Enter the replacement, run **Validate · uses API**, then save. Replacement save performs another validation request. Do not repeat indefinitely. | Whether validation succeeded before save and the visible save result; never include either key. |
| Saved key field looks empty | Expected behavior. **Edit / replace key** never repopulates saved keys. Leave blank to retain the key. | Report only if the app requests re-entry or generation rejects it. |
| “Secure credential unavailable. Re-enter API key.” | Obtain your key from the provider and re-enter it through the normal editor. Do not extract app storage or seek a plaintext fallback. | Version, whether this followed restart/transfer/update, exact message. |
| Provider settings cannot be read | Keep app data intact. Reopen once if no active answer needs preserving; if it persists, report rather than reset or delete profiles. | Exact visible message and what preceded it. |

Use an API **base**, not a full generation or model-list URL. Release connections require HTTPS with platform trust. Do not embed credentials in URLs, bypass TLS checks, or send a key to an endpoint you do not trust.

## Sending and streaming

| Visible symptom or error | Safe steps | Useful report details |
|---|---|---|
| “API key rejected. Check your key.” | Verify the correct provider/account key in the provider's own console. Replace through the normal editor if needed. | API type and whether validation or chat failed. |
| “Provider permission denied.” | Check account, model, region, and use permissions with the endpoint operator. Do not assume a new key alone fixes it. | Safe model ID, operation, visible error. |
| “Model unavailable. Choose another model.” | Confirm the exact ID and text-generation capability with the provider. Change it explicitly; the app does not silently select a replacement. | Requested model ID if safe and API type. |
| “Rate limited. Retry later.” | Stop repeated requests. Wait according to the provider's limits and check its account dashboard. | Approximate time, operation, repeatability; no account screenshots. |
| “Cannot reach provider. Check connection.” | Check watch connectivity and HTTPS base URL. Check provider status. Retry only after deciding a new request is appropriate. | Watch network type, API type, visible error; no private network credentials. |
| Provider timeout or server error | Keep partial content. Check service status and wait. Retry is optional and creates a new request. | Whether text arrived first, time to failure, visible error. |
| “Stream interrupted or unsupported. Partial answer kept.” | Keep the partial answer. Confirm endpoint streaming API support and chosen provider type. Do not assume a familiar model name means protocol compatibility. | API type, partial text arrived yes/no, steps, safe minimal reproduction. |
| Stop appears to take time | Wait for the current request to settle before sending again. Client cancellation cannot guarantee immediate remote cancellation. | Delay observed, whether partial text stayed visible, whether another send became available. |
| Retry or Edit replaces content | Expected linear behavior. Retry replaces the latest assistant response; Edit & resend removes every message after the edited user turn. Neither keeps alternate copies. | Report only if behavior differs from that contract; use nonprivate sample content. |
| History cannot be read or answer cannot be saved | Keep the app and visible content intact. Follow the visible message; do not start by force-stopping, uninstalling, or clearing data. Report before destructive recovery. | Exact message, action before failure, whether received text remains visible. |

No automatic replay occurs after a failed or interrupted stream. Pressing **Retry**, **Send**, **Edit & resend**, or **Validate · uses API** can create a separate billable request.

## Input, reading, and accessibility

| Symptom | Safe steps | Useful report details |
|---|---|---|
| Keyboard does not open | Tap the keyboard icon, then tap the **Prompt** text field. Check that an installed Wear keyboard is available. | Keyboard name/version if known, watch/OS, exact steps. |
| Voice unavailable or blocked | Use keyboard input. Check installed system recognizer availability and its own permissions/settings. Do not grant unrelated permissions to NiroWear. | Exact message and recognizer name if known; omit recordings/private speech. |
| Voice text is inaccurate | Correct text in **Prompt** before **Send**. Recognition belongs to the system recognizer. | Nonconfidential example and recognizer/device details, if useful. |
| Reader stays above new text | Scroll-up detaches following by design. Tap the down-arrow **Latest** action, labeled **Jump to latest**. | Whether Latest is reachable, system font size, physical watch or emulator. |
| Code or math extends sideways | Pan horizontally inside the wide block. Scroll vertically outside or through surrounding content. Do not expect the full width to fit at once. | Minimal nonconfidential sample, font size, pan direction and visible result. |
| Rightward gesture leaves the reader | At a horizontal block's left edge, platform back/dismiss may take over. Reopen the app and use History if needed. | Where the swipe began, whether the block was already at its left edge. |
| Table no longer looks like a grid | Expected: tables display as vertical records under column labels. Scroll through all row values. | Report missing values with a tiny nonconfidential table sample. |
| LaTeX commands appear instead of a fraction/matrix | Expected source fallback. Native formula typesetting is unavailable in beta.1. | Report missing or unreadable source, not absence of native typesetting. |
| Symbols appear as boxes | Device font coverage varies. Compare ordinary text and provide a small Unicode example. | Exact characters, OS/font size, optional safe screenshot. |
| Link does not reach its destination | Check available watch/phone handlers and their permissions. NiroWear only requests an external HTTP(S) handoff; no built-in browser is supplied. | Safe public link, handler/device details, visible outcome. |
| Controls clip, labels are unclear, or reading order is difficult | Record the font size, screen shape, and exact interaction. Do not reduce accessibility settings just to conceal the issue. | Use the [device/accessibility form](https://github.com/michaelxdips/NiroWear-Beta/issues/new?template=device-feedback.yml). No medical information needed. |

## FAQ

### Is the beta free to download? Does chat cost money?

The published APK is available to download without a NiroWear purchase. It does not include API credit or an AI subscription. Your endpoint may charge for generation, validation, retry, and edit/resend under its own pricing.

### Does it need internet or a phone?

API requests need a working internet connection. Saved history can be read without a new API request. NiroWear has no required phone companion app; installation and external voice/link handling depend on your watch's available tools and services.

### Is this an official OpenAI, Google, or Anthropic app?

No. NiroWear is an independent client owned by Stephen Michael. Provider names identify selectable API options, not affiliation or endorsement.

### Which version can I download?

The published release is [0.1.0-beta.1](https://github.com/michaelxdips/NiroWear-Beta/releases/tag/v0.1.0-beta.1), versionCode `2`, with one APK asset. Use its explicit download link, not a generic stable “latest” URL or automatic source archive.

### Is every Wear OS 3+ watch supported?

No compatibility guarantee is made. Wear OS 3+ and Android API 30+ are minimum requirements. The reference evaluation setup is a round 466 × 466 Wear OS 5 / API 34 emulator. Physical-watch compatibility, battery, thermals, accessibility, and full signed-beta reader coverage remain incompletely verified.

### Does NiroWear include an AI subscription or account?

No. You bring your own API key and use your chosen endpoint. Its account rules, model access, retention, and billing apply. NiroWear has no separate account or relay service.

### Why can a listed model still fail?

Discovery and generation are separate operations. A catalog entry may lack text-generation capability or your account's access. **Validate · uses API** tests generation and may incur charges. Manual IDs remain available when compatible discovery fails.

### Does a familiar model name prove an official upstream service?

No. A third-party operator can expose a familiar label. Check the endpoint operator and documented API. The OpenAI Responses option and compatible Chat Completions option are distinct; choose by protocol, not model name. Broad genuine upstream verification is incomplete.

### Does Stop prevent all charges?

No. It cancels the client's HTTP request and preserves received partial text. The remote provider may already have performed billable work. Retry creates a new request.

### Can I keep both an old answer and its Retry, or branch an edited chat?

No. Retry replaces the latest assistant response. Editing replaces the selected user message and permanently deletes every later message before generating again. No alternate variants, branches, or undo copies are kept.

### What happens when I switch providers?

The same linear history remains. Earlier assistant labels retain their provider/model identity. A subsequent send passes the retained context to the newly selected endpoint. Start **New chat** first if that context should not be shared there.

### Is history encrypted or backed up?

Conversation text is local and not separately encrypted. Keys use Keystore-backed AES-GCM storage. There is no NiroWear cloud backup or user-facing conversation export/deletion control. Android backup is disabled in the manifest, but OEM transfer behavior is not universally guaranteed. See [PRIVACY.md](../PRIVACY.md).

### Why are provider-screen screenshots black or blocked?

Secure-window protection helps keep credentials out of captures. Do not disable it for a public report. Describe the nonsecret interaction and visible message in words instead.

### Are math, voice, and links complete?

No. Math uses Unicode/LaTeX source fallback, not native typesetting. Voice delegates to a system recognizer and real spoken transcription is not fully verified. HTTP(S) links request external handlers, but destination completion is not fully verified.

### Can I build the app from this repository?

No. Application source is private, proprietary, and not open-source. Public docs/tooling PRs are welcome; private source collaboration is individually owner-reviewed through the [collaboration form](https://github.com/michaelxdips/NiroWear-Beta/issues/new?template=developer-collaboration.yml). An issue does not automatically grant access or a license.

### Are AI answers reliable?

Not necessarily. They may be false, incomplete, or outdated. Independently verify important facts and do not treat a generated answer as a guarantee of safety, accuracy, or provider permission.

## Report a remaining problem

1. Search existing public issues for the same symptom.
2. Open the relevant [feedback form](https://github.com/michaelxdips/NiroWear-Beta/issues/new/choose).
3. Include published app version, watch/OS, physical watch or emulator, exact steps, expected result, actual result, and repeatability.
4. For rendering issues, include a small invented or otherwise nonconfidential sample. Screenshots are optional and must exclude secrets and private content.
5. State what safe checks you tried and which checks you did not run. Do not reset data or spend API credit just to complete a report.

**For vulnerabilities, exposed credentials, or sensitive exploit details, use [GitHub private vulnerability reporting](https://github.com/michaelxdips/NiroWear-Beta/security/advisories/new), not a public issue. If a key was exposed, revoke or rotate it at the provider immediately.**

See [Contributing](../CONTRIBUTING.md) for docs, tooling, tests, accessibility feedback, and collaboration boundaries.
