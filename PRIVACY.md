# NiroWear beta privacy facts

NiroWear is a bring-your-own-key Wear OS chat client. This technical disclosure describes the beta; it is not a promise about any endpoint operator's processing or retention.

## Local data

Conversations, titles, raw user/assistant content, statuses and provider/model provenance are stored in local application data. Conversation text is not separately encrypted by this implementation. Provider settings and selected model are local.

API keys use Android Keystore-backed AES-GCM encryption. Only versioned encrypted payloads and credential references are persisted. Decryption failure requires re-entry; no plaintext fallback. Keys are masked by default and saved keys are not loaded into editor fields. Provider screens use secure-window protection.

Android backup is disabled in the manifest; extraction rules exclude the credential-protected storage domains currently used by NiroWear. Credentials are stored in `noBackupFilesDir`. Device-transfer behavior can vary by Android/OEM; no NiroWear cloud backup is configured. Clearing application data or uninstalling can permanently remove history/settings and access to keys. Keep valuable data intact when updating.

## Requested network operations

Requested model discovery sends authentication and model-list requests, not your conversation history. Validation sends authentication and a short test prompt, may incur API charges, and is separate from discovery. Generation sends authentication, conversation context through the current user message and client instructions directly to the endpoint you select. Providers also see ordinary connection metadata such as your network IP address. Release networking requires HTTPS with platform trust. No separate NiroWear relay or analytics SDK is configured.

The endpoint operator's privacy policy, terms and billing apply. A configured model label does not establish official upstream identity. OpenAI requests use `store=false`; this is not a universal zero-retention guarantee. Stop cancels the local HTTP call but cannot guarantee remote compute/billing stops.

API access may have age, region, account-type and paid-tier restrictions. Check current [OpenAI service terms](https://openai.com/policies/services-agreement/), [Gemini API terms](https://ai.google.dev/gemini-api/terms), [Anthropic commercial terms](https://www.anthropic.com/legal/commercial-terms) or your actual compatible endpoint's terms. Gemini unpaid services may use prompts/responses to improve Google products and involve human review; do not send sensitive information to those services. API support is not a certification that every account or use is permitted.

History remains local until application data is cleared or the app is uninstalled; editing/retrying deletes the replaced continuation. No user-facing conversation-delete control or NiroWear account/cloud deletion service is provided by this beta. Provider-side retention/deletion is governed by the selected service, not by local history changes. NiroWear does not request advertising identifiers or add an analytics/crash-reporting SDK; system recognizers and external handlers have their own behavior.

## System input and links

Voice delegates to your installed system recognizer; microphone use and any remote speech processing depend on that recognizer. Review returned text before Send. External links delegate to Wear/Android handlers and destination policies apply.

## Feedback

GitHub Issues are public in this landing repository. Submit only nonsecret reproduction details. Do not submit keys, headers, credentials, pairing secrets, private conversation exports or protected editor captures. Remove personal information from screenshots before sharing.

Project owner: Stephen Michael. This disclosure accompanies the owner-authorized binary beta; selected endpoint policies still apply. Report nonconfidential privacy/documentation concerns through GitHub Issues. For sensitive security/privacy concerns, use [private vulnerability reporting](https://github.com/michaelxdips/NiroWear-Beta/security/advisories/new), following [SECURITY.md](SECURITY.md). Never post credentials or private conversations.
