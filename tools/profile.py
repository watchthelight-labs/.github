#!/usr/bin/env python3
# <wtl> project: watchthelight-labs | file: tools/profile.py | author: watchthelight </wtl>
"""Write profile/README.md (the org's front page on github.com) from the same data as labs.watchthelight.org:
the site's site.json (groups, blurbs) and its repos.json (the live repo list it was built from). No tokens needed:
both are public. Run by .github/workflows/profile.yml every 6 hours; commits only when the text changed.

  python tools/profile.py
"""
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_JSON = "https://raw.githubusercontent.com/watchthelight-labs/watchthelight-labs.github.io/main/site.json"
REPOS_JSON = "https://labs.watchthelight.org/repos.json"
ORG = "watchthelight-labs"
B = "style=flat-square&labelColor=0d0e12"


def get(url):
    if not url.startswith("http"):   # a local file, e.g. the site's dist/repos.json during a local run
        return json.loads(Path(url).read_text(encoding="utf-8"))
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def row(r):
    n = r["name"]
    rel = (f"[![release](https://img.shields.io/github/v/release/{ORG}/{n}?{B}&color=4d7a51&label=)]"
           f"(https://labs.watchthelight.org/{n}/releases/)") if r.get("release") else ""
    desc = (r.get("description") or "").replace("|", "/")
    if len(desc) > 140:
        desc = desc[:137].rsplit(" ", 1)[0] + "..."
    return f"| [**{n}**](https://labs.watchthelight.org/{n}/) | {desc} | {rel} |"


def main():
    import os
    site, repos = get(os.environ.get("PROFILE_SITE", SITE_JSON)), get(os.environ.get("PROFILE_REPOS", REPOS_JSON))
    by = {r["name"]: r for r in repos}
    groups = [dict(g) for g in site["groups"]]
    rest = sorted((n for n in by if not any(n in g["repos"] for g in groups)), key=str.lower)
    if rest:
        groups.append({"title": site.get("other_group", "More"), "repos": rest})
    out = [
        '<a href="https://labs.watchthelight.org"><img src="https://labs.watchthelight.org/og.png" '
        'alt="watchthelight labs" width="100%"></a>',
        "",
        f"[![site](https://img.shields.io/badge/labs.watchthelight.org-6a9a6e?{B}&logo=githubpages&logoColor=c8ccd0)]"
        "(https://labs.watchthelight.org) "
        f"[![repos](https://img.shields.io/badge/repos-{len(repos)}-2a2d33?{B})](https://github.com/orgs/{ORG}/repositories) "
        f"[![macOS](https://img.shields.io/badge/macOS_Tahoe-26.7.1-2a2d33?{B}&logo=apple&logoColor=c8ccd0)]"
        "(https://labs.watchthelight.org) "
        f"[![discord](https://img.shields.io/badge/discord-watchthelight-2a2d33?{B}&logo=discord&logoColor=c8ccd0)]"
        "(https://discord.com/users/697169405422862417)",
        "",
        site["intro"],
        "",
        "Each repo has its own pages on **[labs.watchthelight.org](https://labs.watchthelight.org)**, with its docs, "
        "releases and issues. Boot logs from the Legion and from people who run these drivers are in "
        "[research](https://labs.watchthelight.org/research/), and the AI setup behind the code is in "
        "[agents](https://labs.watchthelight.org/agents/).",
    ]
    for g in groups:
        items = [by[n] for n in g["repos"] if n in by]
        if not items:
            continue
        out += ["", f"### {g['title']}", "", "| | | |", "|---|---|---|"] + [row(r) for r in items]
    out += ["", "<sub>Generated from the live repo list every 6 hours by tools/profile.py.</sub>", ""]
    text = "\n".join(out)
    p = ROOT / "profile" / "README.md"
    old = p.read_text(encoding="utf-8") if p.exists() else ""
    if old != text:
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("profile/README.md updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
