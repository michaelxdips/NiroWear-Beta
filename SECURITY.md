# Security

NiroWear is a limited binary beta, not a production-security certification. Published beta.1 and beta.2 use the same owner-approved Android Debug certificate as their beta-only update identity; the APKs are nondebuggable. Off-device signing recovery remains unverified. Verify current downloads using the hash and certificate in [README.md](README.md); historical hashes remain in [CHANGELOG.md](CHANGELOG.md).

Experimental beta is provided as-is, without warranties. NiroWear application source is proprietary, not open-source. © 2026 Stephen Michael, for first-party NiroWear material only; third-party rights remain separate. Public landing files grant no blanket reuse license. See [COPYRIGHT.md](COPYRIGHT.md).

## Reporting a concern

**Do not post exploit details, API keys, authentication headers, provider credentials, pairing secrets, private conversation exports or protected-screen captures in public issues.** If a credential has leaked, revoke or rotate it with its provider; deleting a public post does not revoke it.

GitHub private vulnerability reporting was confirmed enabled on 2026-10-11. Use the repository's Security tab, then **Report a vulnerability**, or [open a private report](https://github.com/michaelxdips/NiroWear-Beta/security/advisories/new). Confirm you are in the private reporting flow before attaching sensitive details; do not use a public issue.

If that flow becomes unavailable, use an existing, verified private channel to the repository owner. If none is available, open only a non-sensitive request asking the owner to establish one. Withhold exploit details and sensitive attachments until a private channel is confirmed. No reporting email or response-time commitment is established here.

## Data boundaries

- Keys use Android Keystore-backed AES-GCM; saved keys are not repopulated into editor fields. Encryption/decryption failure requires re-entry, not plaintext fallback.
- Conversation text is local but not separately encrypted. Backup is disabled; uninstalling or clearing app data can permanently remove it.
- Requested operations send credentials and relevant context directly to your configured HTTPS endpoint. Check its operator, policies and billing; a model name does not establish official upstream identity.
- Stop cancels local HTTP, not guaranteed remote computation or billing. System voice and external links use their respective handlers and policies.

See [PRIVACY.md](PRIVACY.md) for data handling and [README.md](README.md) for beta acceptance limits.
