# Security

Most repos here are kernel extensions, so a bug in one runs with full kernel rights. Please report security problems privately, not in a public issue.

## How to report

Open the repo on GitHub, go to the **Security** tab and press **Report a vulnerability**. Only you and I can see the report. If a repo doesn't show that button, email admin@watchthelight.org with the repo name in the subject.

Say which repo and release, the machine and macOS build, and how to reproduce it. A panic report or a small test program helps a lot.

## What counts

- A kext that lets an unprivileged user or app crash the machine, read or write kernel memory, or gain root. For example a user client or sysctl that accepts input from a normal process without checking it.
- A driver that exposes data it shouldn't, such as Wi-Fi keys or passphrases in ioreg or a log.
- A leaked secret: a token, key or password in a repo, its history, a release or a CI log.
- A release binary that doesn't match its source, or a build or install script that downloads and runs something it shouldn't.

## What doesn't

- Having to relax SIP or AMFI, turn off Secure Boot, or load unsigned kexts. A Hackintosh needs that, and the READMEs say so.
- Crashes that only root can trigger. Root can already load kernel code on these setups, so please open a normal issue.
- Ordinary panics and hangs during normal use. Those are bugs; use the issue form in the repo.
- Problems in OpenCore, Lilu, VoodooI2C, NullMoth's driver or other upstream projects. Report those to them. If one of our repos ships the affected code, tell me too.

## Supported versions

Only the latest release of each repo gets fixes. If you're on an older one, check whether the latest release still has the problem before reporting.

## What to expect

This is one person's spare-time project, so there's no response time I can promise. I read every report, I'll reply when I've looked at it, and a fix goes out as a new release. Tell me if you want to be credited in the release notes.
