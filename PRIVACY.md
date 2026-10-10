# NiroWear beta privacy facts

NiroWear is a bring-your-own-key Wear OS chat client. This technical disclosure describes the beta; it is not a promise about any endpoint operator's processing or retention.

## Local data

Conversations, titles, raw user/assistant content, statuses and provider/model provenance are stored in local application data. Conversation text is not separately encrypted by this implementation. Provider settings and selected model are local.

API keys use Android Keystore-backed AES-GCM encryption. Only versioned encrypted payloads and credential references are persisted. Decryption failure requires re-entry; no plaintext fallback. Keys are masked by default and saved keys are not loaded into editor fields. Provider screens use secure-window protection.

Backup is disabled. Clearing application data or uninstalling can permanently remove history/settings and access to keys. No NiroWear cloud backup is configured. Keep valuable data intact when updating.

## Requested network operations

Your credential and conversation context are sent directly to the endpoint you select for requested discovery, validation or generation. Release networking requires HTTPS with platform trust. No separate NiroWear relay or analytics SDK is configured.

The endpoint operator's privacy policy, terms and billing apply. A configured model label does not establish official upstream identity. OpenAI requests use `store=false`; this is not a universal zero-retention guarantee. Stop cancels the local HTTP call but cannot guarantee remote compute/billing stops.

## System input and links

Voice delegates to your installed system recognizer; microphone use and any remote speech processing depend on that recognizer. Review returned text before Send. External links delegate to Wear/Android handlers and destination policies apply.

## Feedback

GitHub Issues are public in this landing repository. Submit only nonsecret reproduction details. Do not submit keys, headers, credentials, pairing secrets, private conversation exports or protected editor captures. Remove personal information from screenshots before sharing.

Beta does not add analytics or crash-reporting SDKs. Publisher-specific legal/contact terms must be approved before external binary publication; this page alone does not establish that approval.
