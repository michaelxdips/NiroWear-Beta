# NiroWear user guide

This guide describes **0.1.0-beta.2**, the published sideload beta. Start with installation and one short keyboard prompt; use the later sections when you need more control.

[Download APK](https://github.com/michaelxdips/NiroWear-Beta/releases/download/v0.1.0-beta.2/NiroWear-0.1.0-beta.2.apk) · [README](../README.md) · [Troubleshooting](TROUBLESHOOTING.md)

## What you need

- A Wear OS 3+ watch with Android API 30+. The reference evaluation setup is a round 466 × 466 Wear OS 5 / API 34 emulator, not a guarantee of physical-watch support.
- Android SDK Platform Tools on a computer and a supported watch debugging connection.
- Internet access on the watch.
- Your own API key and an exact text-generation model ID for a supported API. Review the provider's terms and billing first.

NiroWear has no account service or included API credit. Model and endpoint availability depend on your provider. No Play Store installation is available.

## Install the APK

1. Download [NiroWear-0.1.0-beta.2.apk](https://github.com/michaelxdips/NiroWear-Beta/releases/download/v0.1.0-beta.2/NiroWear-0.1.0-beta.2.apk). Do not use GitHub's “Source code” ZIP or tarball; those contain public documentation, not the app.
2. Calculate its SHA256. On Windows PowerShell, run:

   ```powershell
   Get-FileHash -Algorithm SHA256 .\NiroWear-0.1.0-beta.2.apk
   ```

   On Linux, use `sha256sum NiroWear-0.1.0-beta.2.apk`; on macOS, use `shasum -a 256 NiroWear-0.1.0-beta.2.apk`.

   Expected value, ignoring letter case:

   ```text
   d524c3bae5a26ab5cac7c8c3b80f62824b1ecc82506f180ca005954eeaeaa0b6
   ```

   If it differs, do not install. Download again from the release link and check again.
3. Enable developer options and the supported debugging method on your watch. For wireless debugging, follow the watch's pairing screen. Where supported, replace the placeholders below with the displayed address and ports:

   ```text
   adb pair <watch-ip>:<pair-port>
   adb connect <watch-ip>:<debug-port>
   adb devices -l
   ```

   The pairing port and debug port may differ. Keep pairing codes private. Older watch setups may use a different ADB connection workflow.
4. Identify the intended watch's serial from `adb devices -l`. Install only to that target:

   ```text
   adb -s <serial> install NiroWear-0.1.0-beta.2.apk
   ```

   For an existing same-certificate installation, use:

   ```text
   adb -s <serial> install -r NiroWear-0.1.0-beta.2.apk
   ```
5. Open NiroWear from the watch's app launcher. Disable debugging when you no longer need it.

The package is `com.nirowear`, version `0.1.0-beta.2`, versionCode `3`. The APK is nondebuggable but uses the same owner-approved Android Debug certificate as beta.1 for updates, not production-grade signing.

**Do not uninstall or clear app data to fix a certificate mismatch. Either action can permanently remove history, settings, and access to stored keys.** See [installation troubleshooting](TROUBLESHOOTING.md#installation-and-updates).

## Add your first provider

1. Tap the top header to open **Menu**.
2. Choose **Providers / model**.
3. Pick the API type supported by your endpoint:

   | Button | API | Default base URL |
   |---|---|---|
   | **Add OpenAI** | OpenAI Responses | `https://api.openai.com/v1` |
   | **Add Anthropic** | Anthropic Messages | `https://api.anthropic.com/v1` |
   | **Add Gemini** | Gemini streaming GenerateContent | `https://generativelanguage.googleapis.com/v1beta` |
   | **Add compatible** | OpenAI-compatible Chat Completions | Enter your endpoint's documented HTTPS API base |

4. Fill in **Name**, **Base URL**, **Manual model ID**, and **API key**. Use a short name you recognize. Enter an API base, not a full `/responses`, `/models`, or `/chat/completions` request URL. Do not put keys, query parameters, fragments, or embedded credentials in the URL.
5. If you need an ID, tap **Discover models**, then choose a listed model. Alternatively, enter its exact ID in **Manual model ID**. Compatible endpoints can work with a manual ID even if discovery fails.
6. Optionally tap **Validate · uses API** to test generation with the selected model. It sends a short prompt to your endpoint and may cost money. A successful model listing is not a successful generation test.
7. Choose **Save securely**. Saving selects this profile. Tap **Back** to return to the reader.

Saving a new profile is not proof that its key/model can generate. Choose the correct API type from provider documentation; model names do not select protocols. A third-party endpoint using a familiar model name is still a third-party endpoint. Broad live upstream verification remains incomplete.

**Only enter keys you are authorized to use. Your selected endpoint receives the key and requested conversation context. Check the endpoint's operator, terms, account eligibility, region restrictions, and charges before sending.**

### Saved keys and replacement

Keys start masked; **Reveal key** shows only what you are currently entering. **Hide key** masks it again. Provider screens use secure-window protection, so screenshots or screen sharing may be blocked.

Saved keys are encrypted using Android Keystore-backed AES-GCM storage. **Edit / replace key** always opens with a blank key input:

- Leave **API key** blank to keep the saved key while changing the name, base, or model.
- To replace it, enter the new key, use **Validate · uses API**, then **Save securely**. Replacement save performs another validation request, which may also incur charges.
- If secure decryption fails, re-enter your key through the normal editor. There is no plaintext fallback.

Do not send keys in GitHub issues, screenshots, chat prompts, or collaboration requests.

## Send your first message

1. Tap the keyboard icon, labeled **Keyboard input** for accessibility.
2. On **Prompt**, tap the text field and use your installed Wear keyboard.
3. Enter a small nonconfidential prompt, such as:

   ```text
   Explain why the sky is blue in three sentences.
   ```

4. Tap **Send**. Read the response as it arrives.
5. Send a follow-up, such as `Explain that in more detail, with one example.` The current conversation provides context.

Answers are concise by default, but an explicit request for detail, steps, examples, code, or comparisons asks for a fuller response. NiroWear displays long answers as scrollable content rather than squeezing them onto one screen. Output length and quality still depend on the selected model.

### Voice input

1. Tap the microphone icon, labeled **Voice input**.
2. Speak using the installed system recognizer.
3. If text is returned, review or correct it on **Prompt**.
4. Tap **Send** only when you are happy with the text.

Speech is not automatically sent to the AI provider. Recognizer availability, microphone permissions, network use, and speech processing belong to your system recognizer. Real spoken-transcription coverage is incomplete; use keyboard input if recognition is missing or blocked.

## Read a streaming answer

Scroll vertically through the document. Near the bottom, the view follows incoming content. Scroll upward to read earlier paragraphs without being pulled back down.

The down-arrow **Latest** action has the accessibility label **Jump to latest**. Tap it to return to the current tail. It is an icon, not a text button.

Tap **Stop** to cancel the active client request. Received partial text remains available with stopped status. Wait for generation to settle before another send or provider switch. A failed or interrupted stream is not automatically retried.

**Stop cannot guarantee that remote computation or billing stops. Retry, edit/resend, validation, and ordinary sends can each create billable provider requests.**

## Retry or edit a conversation

### Retry the latest assistant response

1. Wait until generation is idle.
2. Scroll to the circular-arrow icon after the latest assistant response, labeled **Retry response**.
3. Tap it to remove that response and request a replacement from the currently selected provider/model.

Retry does not keep alternate variants. It is a new request, not a continuation of a cancelled connection.

### Edit an earlier user message

1. Wait until generation is idle and find the user message you want to change.
2. Long-press it to open **Prompt**.
3. Review the changed text before committing.
4. Tap **Edit & resend**.

**This replaces that message and permanently deletes all later messages in that conversation before requesting a new continuation. There is no branch or undo copy. Cancelling the editor with Back avoids committing the edit. Deleting local continuation text does not delete copies already held by a provider.**

## History, new chats, and provider switching

- Open **Menu → History** and tap a conversation title to resume it.
- Choose **New chat** in Menu or History while idle to start a separate conversation. Existing conversations remain in History.
- To switch providers while idle, open **Providers / model** and tap the desired profile.
- To change a profile's model, use **Edit / replace key**, choose or enter the model ID, and **Save securely**. Leave the key blank if you are keeping it.

Switching does not branch or erase the current conversation. Earlier assistant messages retain the provider/model labels that produced them. Sending after a switch shares the retained linear context with the newly selected endpoint; use **New chat** first if you do not want that context sent there.

History stores user and assistant text locally, including original assistant Markdown. Conversation text is not separately encrypted. There is no NiroWear cloud backup, user-facing history export, or conversation deletion control in this beta. Uninstalling or clearing data can permanently remove local history. Content restoration and exact reader-position restoration are not the same guarantee; full signed-beta restoration coverage is incomplete.

## Reading formatted content

### Markdown and Unicode

Headings, paragraphs, bullets, numbered lists, quotes, bold/italic text, inline code, and dividers display as document content. Unicode symbols and scripts use device fonts; missing glyphs can appear as boxes.

Try a nonconfidential prompt:

```text
Explain inertia with a heading, three bullet points, and a short example.
Include these symbols in a final line: α β Ω ± × √ ∞ ≤ ≥.
```

### Code

Fenced code blocks use monospace text and preserve formatting. When the response includes a language label, it appears with the block. Pan horizontally inside wide code, then scroll vertically through the surrounding document.

```text
Show a complete small Kotlin function that returns the square of an Int.
Put it in a fenced Kotlin code block and explain one edge case.
```

A rightward swipe at a horizontal block's left edge may trigger the platform's back/dismiss gesture. Pan within the block and return with History if you leave the reader. Scoped signed-emulator code/source-math endpoint checks passed at font scales 1.0 and 1.3; arbitrary documents and physical watches remain unverified.

### Tables

Markdown tables become vertical records: each row's values appear under their column labels. Scroll through all records rather than looking for a miniature spreadsheet.

```text
Compare walking and cycling in a Markdown table with columns Activity,
Equipment, and One benefit. Use two rows.
```

### Math

The published beta displays Unicode math and LaTeX **source fallback**, not native formula typography. Fractions, roots, powers/subscripts, calculus, matrices, cases, and aligned equations remain source text. Wide formula source supports horizontal pan.

```text
Explain the quadratic formula. Show its LaTeX source and define each symbol.
Then show a 2 by 2 identity matrix in LaTeX source.
```

Seeing `\frac{...}{...}` or `\begin{matrix}...\end{matrix}` is expected in this beta, not proof of typeset fraction or matrix support.

### Links

Tap an HTTP(S) link to request an external Android/Wear handler. NiroWear has no built-in browser. Destination opening depends on installed watch/phone handlers and system permissions; complete handoff coverage is incomplete.

## Get help or share feedback

Use [troubleshooting](TROUBLESHOOTING.md) for safe recovery and [Contributing](../CONTRIBUTING.md) for docs, tooling, tests, device feedback, and collaboration.

**Public reports must exclude keys, pairing codes, authentication headers, private conversations, and credential screens. Use [private vulnerability reporting](https://github.com/michaelxdips/NiroWear-Beta/security/advisories/new) for sensitive security issues.**

Read [privacy facts](../PRIVACY.md), [security guidance](../SECURITY.md), and [copyright notice](../COPYRIGHT.md). AI answers may be wrong; independently verify important information.
