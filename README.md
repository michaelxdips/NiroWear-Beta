<div align="center">

<img src="docs/branding/nirowear-icon.png" width="88" height="88" alt="NiroWear Thread mark: a single stroke with one page edge left open" />

# NiroWear

**Ask on your watch. Read beyond one screen.**

BYOK AI chat for Wear OS. Type or dictate a question, read the answer as it arrives, come back to the whole conversation later.

**Public beta · 0.1.0-beta.6 · Sideload only · Source now MIT**

[**Download 0.1.0-beta.6**](https://github.com/michaelxdips/NiroWear-Beta/releases/download/v0.1.0-beta.6/NiroWear-0.1.0-beta.6.apk) · [Release notes](https://github.com/michaelxdips/NiroWear-Beta/releases/tag/v0.1.0-beta.6) · [Source code](https://github.com/michaelxdips/NiroWear) · [Install guide](docs/USER_GUIDE.md#install-the-apk)

**Bring your own API key.** Generation needs internet access and may incur provider charges; no API credit is included.

<a href="#read-the-answer-not-a-miniature-desktop"><img src="docs/screenshots/real-response.png" width="168" height="168" alt="A real AI answer shown as readable document text on a round NiroWear screen" /></a>

One view into a real answer, not the whole answer squeezed onto your wrist.

</div>

> **This repository distributes signed APKs and user documentation.**
> The application source moved out of this repository and is now public under the MIT license at
> **[github.com/michaelxdips/NiroWear](https://github.com/michaelxdips/NiroWear)**. Build
> instructions, architecture notes and contribution rules live there.

## Find your way

| Explore the experience | Get started or help |
|---|---|
| [Before, during, and after an answer](#a-question-does-not-end-at-one-screen) | [Download and install](#download-and-install) |
| [Choose an API and model](#choose-your-api-and-model) · [Keyboard and voice](#ask-with-keyboard-or-voice) | [Step-by-step user guide](docs/USER_GUIDE.md) |
| [Streaming, Stop, and Latest](#read-while-the-answer-arrives) · [Formatted answers](#read-the-answer-not-a-miniature-desktop) | [Troubleshooting and FAQ](docs/TROUBLESHOOTING.md) |
| [Retry and edit](#change-the-answer-or-the-question) · [History and switching](#return-to-a-conversation-or-start-fresh) | [Help improve NiroWear](#help-improve-nirowear) · [Known limits](#limitations-worth-knowing) |

## What changed in beta.6

Three things a beta.2 reader would not recognise:

- **LaTeX is now typeset.** Earlier betas showed formula *source* as monospace text. beta.6 renders fractions, roots, matrices, cases and aligned equations natively in release builds.
- **Setup no longer needs the watch keyboard.** Open **Providers / model → Add provider → Set up from phone**. The watch shows a short LAN address; open it on a phone or laptop, paste the key into a normal web form, and the watch saves and validates it by itself. The page is encrypted end-to-end and valid for two minutes, one use.
- **Validation errors name the real cause.** A rejected key now reads *"API key rejected"* and a missing model reads *"Model unavailable"*, instead of one message blaming three fields.

Full per-release detail is in the [changelog](CHANGELOG.md).

## A question does not end at one screen

Start with a question, pause to inspect the answer, then come back when you need it. NiroWear treats assistant output as a document to read, not an oversized chat bubble.

<table>
  <tr>
    <td align="center"><a href="#ask-with-keyboard-or-voice"><img src="docs/screenshots/chat-home.png" width="144" height="144" alt="Chat home before asking, with keyboard and voice entry controls" /></a><br /><strong>1. Before: ask</strong><br />Keyboard opens Prompt.<br />Review text, then Send.</td>
    <td align="center"><a href="#read-while-the-answer-arrives"><img src="docs/screenshots/streaming-stop.png" width="144" height="144" alt="An answer arriving incrementally with Stop visible" /></a><br /><strong>2. During: read</strong><br />Follow incoming text.<br />Stop keeps received text.</td>
  </tr>
  <tr>
    <td align="center"><a href="#read-the-answer-not-a-miniature-desktop"><img src="docs/screenshots/code-reader.png" width="144" height="144" alt="Kotlin code in a monospace block that supports horizontal pan" /></a><br /><strong>3. Pause: inspect</strong><br />Pan through wide code.<br />Read tables as labeled records.</td>
    <td align="center"><a href="#return-to-a-conversation-or-start-fresh"><img src="docs/screenshots/history.png" width="144" height="144" alt="History list for returning to saved NiroWear conversations" /></a><br /><strong>4. After: return</strong><br />Open History.<br />Resume a saved conversation.</td>
  </tr>
</table>

Select a screenshot to jump to its feature guide below. The [table view](#read-the-answer-not-a-miniature-desktop) shows how a grid becomes readable records.

All six screenshots on this page are genuine, uncropped **466 × 466 emulator captures**, displayed smaller for browsing. They illustrate the workflow; they are not beta.6-specific visual verification of one continuous recorded chat. Each captures one scroll position, not an entire response. They are not mockups and not proof of physical-watch compatibility. Provider screens are capture-protected, so no credential-screen image is included.

## Explore the published beta

Expand a section for controls, examples, and limits. The README covers everyday use; linked guide sections add detailed setup and recovery steps.

### Choose your API and model

<details>
<summary><strong>Your endpoint, your key, your model — setup and switching</strong></summary>

NiroWear connects directly to the HTTPS API endpoint you configure. Tap the top header for **Menu**, then open **Providers / model**. Choose the API supported by your endpoint:

- **OpenAI** uses the native Responses protocol.
- **Anthropic** uses the Messages protocol.
- **Gemini** uses `generateContent` over SSE.
- **OpenAI-compatible** uses Chat Completions and accepts a base URL plus a manually typed model ID.

The wire protocol follows the provider type you pick. It is never guessed from a model name, because a familiar model name does not prove which API is actually behind an endpoint.

**Getting the key in.** Tap **Set up from phone**. The watch shows an address like `http://192.168.1.24:41234/`. Open it on any device with a real keyboard, pick the provider, paste the key, tap **Send to watch**. The page is encrypted with ephemeral ECDH P-256 and AES-GCM, expires after two minutes, and works once. Manual entry stays available underneath if the watch has no Wi-Fi address.

**Model discovery and authentication are separate checks.** If your compatible endpoint will not list models, type the model ID yourself and chat anyway. Discovery failing never invalidates a configuration you already know works, and NiroWear never silently substitutes a different model.

Switching provider or model mid-conversation keeps one linear history. Each assistant message records which profile and model produced it.

</details>

### Ask with keyboard or voice

<details>
<summary><strong>Two first-class input paths</strong></summary>

Tap **Keyboard** to open the prompt editor, review your text, then Send. Tap **Voice** to delegate to the platform recognizer; the transcript comes back as text you can edit before sending, so a misheard word never becomes an accidental prompt.

Long answers are never shortened because the screen is small. The reader scrolls; the answer does not get truncated.

</details>

### Read while the answer arrives

<details>
<summary><strong>Streaming, Stop, and the Latest control</strong></summary>

Tokens render as they arrive. While you stay near the bottom, the view follows the incoming text.

Scroll upward and following stops: NiroWear will not pull you back down while you are reading. A small **Latest** control appears; tap it to rejoin the end of the answer.

**Stop** cancels the underlying HTTP request and keeps whatever text already arrived. Partial content stays visible and is saved. NiroWear never replays visible output on its own.

</details>

### Read the answer, not a miniature desktop

<details>
<summary><strong>Markdown, code, tables, math, and links on a 466 px round screen</strong></summary>

Assistant output is parsed into semantic blocks — headings, paragraphs, lists, quotes, inline code, code blocks, math, tables, dividers, links — and each block lays itself out. It is never rendered as one giant text node.

**Code** keeps its indentation in a monospace block and pans horizontally rather than wrapping, because wrapped code changes what it appears to say.

**Tables** become labelled vertical records instead of a four-column grid squeezed into 466 px. No cell is dropped and no column is silently hidden.

**Math** is typeset natively in beta.6 and later: fractions, roots, powers, subscripts, integrals, summations, limits, matrices, cases and aligned equations render as formulas rather than LaTeX source. A wide formula pans; it is never shrunk into illegibility. Input the renderer deliberately refuses — file-inclusion macros, macro definitions, unbalanced braces — falls back to readable source text instead of rendering blank.

**Links** open through the system handler, and only `http`/`https` targets with a host are accepted.

Raw Markdown is stored as sent, so the renderer can improve without a migration.

</details>

### Change the answer or the question

<details>
<summary><strong>Retry the latest answer, or edit an earlier question</strong></summary>

**Retry** replaces the latest assistant response with a fresh generation from the same context.

**Edit** an earlier user message by holding it. NiroWear replaces that message, removes everything after it, and generates a new continuation from there. The edit is linear on purpose: there are no branches and no alternate-response variants to choose between.

</details>

### Return to a conversation or start fresh

<details>
<summary><strong>History, new chats, and switching providers</strong></summary>

Open **Menu → History** to resume a saved conversation, or **New chat** to start clean. History is stored on the watch, is not separately encrypted, and has no cloud backup.

Switching provider or model does not fork the conversation: the same linear history continues, and each answer keeps a record of which profile and model produced it. Sending again shares the retained context with the newly selected endpoint.

</details>

## Download and install

There is no store listing. The signed APK is the supported install path.

| | |
|---|---|
| Latest | [0.1.0-beta.6](https://github.com/michaelxdips/NiroWear-Beta/releases/tag/v0.1.0-beta.6) · versionCode 7 · 3,593,274 bytes |
| SHA-256 | `bd9c7eb968dc3b10c873591a79c81987c147980c480620af464dc2c65154fcb9` |
| Signing | Same beta identity as every prior release, so upgrades keep your conversations |
| Requires | Wear OS 3 (API 30) or newer |

```text
adb install -r NiroWear-0.1.0-beta.6.apk
```

Step-by-step device and wireless-ADB instructions: [install the APK](docs/USER_GUIDE.md#install-the-apk).

**Want to build it yourself?** The source is MIT and public at [github.com/michaelxdips/NiroWear](https://github.com/michaelxdips/NiroWear), with its own README, build steps and contribution rules.

## Limitations worth knowing

These are current facts, not disclaimers to skim past.

- **Physical-watch acceptance is incomplete.** Touch reach, battery and thermals on a real Xiaomi Watch 2 are not fully verified. Emulator coverage is extensive; it is not the same thing.
- **Voice recognition quality is unaccepted.** The launch-and-return path is tested; transcription accuracy belongs to the platform recognizer.
- **Link destinations are unverified end to end.** NiroWear requests the system handler; what happens after that is outside the app.
- **TalkBack audio acceptance is incomplete.** Headings expose semantics; full reading order has not been signed off.
- **Live upstream coverage is incomplete.** Observed real requests used a configured third-party HTTPS Responses endpoint. A displayed model or provider name does not prove official upstream identity.
- **History is device-local and unencrypted.** Uninstalling or clearing data removes it permanently. Keys are encrypted; conversation text is not.
- **Arbitrary huge documents and every font size are untested.** Scoped checks cover reader endpoints at font scales 1.0 and 1.3, navigation, Activity recreation and history reopening after process or device restart.

See [troubleshooting and FAQ](docs/TROUBLESHOOTING.md) before resetting anything.

## Privacy, safety, and feedback

Before sending private content, review [privacy facts](PRIVACY.md) and your selected endpoint's policies. Keys are encrypted locally with AES-GCM under an Android Keystore key; conversation text is not. Switching providers and sending again shares the retained context with the new endpoint.

There is no NiroWear account, analytics, crash reporting or backend. Requests go from the watch directly to the endpoint you configured, so that provider's retention policy applies.

AI answers can be false, incomplete, or outdated. Check important claims independently. You are responsible for meeting your provider's account, region, age, and use restrictions; availability in the app is not permission to use a service.

**GitHub Issues are public. Never post API keys, authentication headers, pairing addresses, private conversations, or unredacted credential-screen captures. Report vulnerabilities through [GitHub private vulnerability reporting](https://github.com/michaelxdips/NiroWear-Beta/security/advisories/new), not public issues.**

## Help improve NiroWear

Good feedback connects a real action to a real result: what you tried, what you expected, and what happened.

| How you can help | Where to go |
|---|---|
| Improve this documentation, fix a broken link, clarify a step | A focused [documentation PR](CONTRIBUTING.md#public-pull-requests) |
| Report a reproducible app bug | [Bug and feedback forms](https://github.com/michaelxdips/NiroWear-Beta/issues/new/choose) |
| Share physical-watch or emulator observations: readability, font size, touch reachability, input, accessibility | [Device and accessibility feedback](https://github.com/michaelxdips/NiroWear-Beta/issues/new?template=device-feedback.yml) |
| Change the application itself | [Source repository](https://github.com/michaelxdips/NiroWear) — MIT licensed, PRs welcome |
| Report a security issue | [Private vulnerability reporting](https://github.com/michaelxdips/NiroWear-Beta/security/advisories/new) |

For device reports, include the watch model, OS version, NiroWear version, relevant display and font settings, and repeatable steps. Say whether you used a physical watch or an emulator. Do not spend API credit or reset valuable app data just to finish a report.

Read [contribution guidance](CONTRIBUTING.md) before submitting. Keep public requests nonconfidential.

## Copyright and notices

Copyright © 2026 Stephen Michael, for first-party NiroWear material.

**Application source is MIT licensed** and public at [github.com/michaelxdips/NiroWear](https://github.com/michaelxdips/NiroWear). This repository remains the distribution point for signed beta APKs and user documentation. See [COPYRIGHT.md](COPYRIGHT.md) for the split between the two repositories.

One bundled dependency is not permissive: `jlatexmath-android` is GPL v2-or-later **with an independent-module linking exception**, which explicitly permits linking it with MIT code and distributing the result under terms of your choice. The GPL text, the exception and a corresponding-source pointer ship inside the app. Third-party components, icons and other materials retain their respective owners' rights and license terms.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), [SECURITY.md](SECURITY.md), and the [published release history](CHANGELOG.md).

The launcher mark is NiroWear's own [Thread identity](docs/branding/PROVENANCE.md), introduced in beta.4. Historical releases retain their original icons and unchanged APKs.
