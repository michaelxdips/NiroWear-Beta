# Contributing to NiroWear

Help make the published Wear OS beta easier to use and evaluate. Useful contributions include clear documentation, small public-tooling fixes, reproducible test cases, and device or accessibility feedback.

This repository contains beta distribution information, guides, screenshots, notices, and feedback forms. It does **not** contain the application source. NiroWear application source is private, proprietary, and not open-source.

## Ways to help now

| Contribution | Best route |
|---|---|
| Fix a typo, broken link, or unclear public instruction | A focused pull request |
| Improve existing public repository checks or documentation tooling | A focused pull request explaining the change |
| Report an app bug or share a repeatable test case | A [public issue](https://github.com/michaelxdips/NiroWear-Beta/issues/new/choose) |
| Share watch compatibility, reading, input, or accessibility observations | [Device and accessibility feedback](https://github.com/michaelxdips/NiroWear-Beta/issues/new?template=device-feedback.yml) |
| Discuss development or testing collaboration requiring private source | [Developer collaboration](https://github.com/michaelxdips/NiroWear-Beta/issues/new?template=developer-collaboration.yml) |
| Report a vulnerability or credential exposure | [Private vulnerability reporting](https://github.com/michaelxdips/NiroWear-Beta/security/advisories/new) |

Docs and public-tooling PRs do not require application-source access. Testers can also help without source: describe exact actions, expected behavior, actual behavior, and the published version used.

## Public pull requests

1. Read the relevant public guide or notice and check existing issues/PRs for duplicates.
2. Keep the change focused. Describe the user problem and why the proposed text or tooling addresses it.
3. Document only behavior available in the published beta. Do not turn an unverified observation into a compatibility guarantee.
4. Check changed links and instructions. For tooling, run the relevant existing check when possible; report the command and result, or say clearly that it was not run.
5. Submit the PR with a short summary and any limits to your verification.

Do not add APKs, private application files, credentials, signing material, private conversation data, or unrelated binaries. Do not replace the existing screenshot gallery or third-party legal materials as part of an unrelated change. Copyright and licensing changes require owner review; public access is not a blanket reuse license.

For public text or tooling changes, use GitHub no-reply author and committer email addresses, stage and commit the intended files, then run `python .github/check_public.py` from this repository. The check requires the exact allowed file set, matching staged/working bytes, and no-reply metadata on the newest commit; explain any new file instead of weakening the allowlist. The owner reviews contribution permissions before merging material with unclear authorship or reuse rights. Submission does not automatically assign copyright.

There are no application build instructions in this repository because application source is not published. GitHub's automatic source archives contain the public landing files only.

## Device and accessibility feedback

Use the [shared device/accessibility form](https://github.com/michaelxdips/NiroWear-Beta/issues/new?template=device-feedback.yml). Include:

- Watch make/model, Wear OS version, Android API level if known, and NiroWear version.
- Display size or shape and system font size if relevant.
- Exact steps and whether the result repeats.
- What was difficult: clipping, reading order, touch reachability, control labels, keyboard, voice, horizontal pan, or link handoff.
- Optional screenshots of nonconfidential content only.

You do not need to disclose a disability, medical information, location, serial number, or account details. Describe the interaction problem instead. Say whether an observation came from a physical watch or emulator. A report from one device does not establish support for every device.

Test cases and documentation suggestions are welcome even when you cannot reproduce an issue on another watch. Do not spend API credit or reset valuable app data just to complete a report.

## Request private-source collaboration

Open a [developer collaboration issue](https://github.com/michaelxdips/NiroWear-Beta/issues/new?template=developer-collaboration.yml) describing your proposed scope, relevant experience, and public work samples if you want to share them. Useful scopes include tests, documentation, Wear OS device evaluation, accessibility review, and focused app work.

The owner reviews each request individually. An issue, PR, or helpful report does not automatically grant private repository access, permission to redistribute source, or an open-source license. Do not upload private documents or request credentials in the issue; the owner can discuss any needed private arrangements separately.

There is no automatic CLA, copyright assignment, employment offer, payment commitment, or promise of access attached to this invitation. Do not assume any of those terms from participation.

## Keep reports safe

**Public issues and PRs are visible to everyone. Never include API keys, authentication headers, pairing codes, private prompts/responses, signing files, or unredacted credential screens. Do not attach raw diagnostic dumps that may contain secrets.**

If you exposed a key, revoke or rotate it at the provider immediately. Use [GitHub private vulnerability reporting](https://github.com/michaelxdips/NiroWear-Beta/security/advisories/new) for vulnerabilities and sensitive reproduction details. See [SECURITY.md](SECURITY.md).

Copyright © 2026 Stephen Michael, for first-party NiroWear material. Third-party rights remain separate; see [COPYRIGHT.md](COPYRIGHT.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
