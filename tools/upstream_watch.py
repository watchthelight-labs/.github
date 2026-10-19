#!/usr/bin/env python3
# <wtl> project: watchthelight-labs | file: tools/upstream_watch.py | author: watchthelight </wtl>
"""Posts upstream activity to Discord for each repo of WATCH_REPOS: watchthelight's PRs opened, comments and reviews
on his PRs, his PRs being closed or merged, and @mentions. Run by .github/workflows/upstream-watch.yml every 10 minutes;
SINCE (ISO time) is the start of the previous successful run, so nothing is posted twice or skipped."""
import json, os, sys, urllib.request, urllib.parse

GH = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
HOOK = os.environ["DISCORD_WEBHOOK"]
ME = os.environ.get("WATCH_USER", "watchthelight")
REPOS = os.environ.get("WATCH_REPOS", "nullmoth/nvidia-macos-driver").split()
SINCE = os.environ["SINCE"]


def gh(path, params=None):
    url = path if path.startswith("http") else GH + path
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    out = []
    while url:
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "Authorization": f"Bearer {TOKEN}",
                                                   "X-GitHub-Api-Version": "2022-11-28"})
        with urllib.request.urlopen(req) as r:
            data = json.load(r)
            link = r.headers.get("Link", "")
        if isinstance(data, dict) and "items" in data:
            data = data["items"]
        if not isinstance(data, list):
            return data
        out += data
        url = next((p.split(";")[0].strip("<> ") for p in link.split(",") if 'rel="next"' in p), None)
    return out


_issue = {}
def issue(url):
    if url not in _issue:
        _issue[url] = gh(url)
    return _issue[url]


posts = []
def post(title, url, body, color, who):
    body = (body or "").strip()
    posts.append({"title": title[:250], "url": url, "description": (body[:900] + (" ..." if len(body) > 900 else "")) or None,
                  "color": color, "author": {"name": who}})


for repo in REPOS:
    mentioned = lambda text: f"@{ME}".lower() in (text or "").lower()
    # issue and PR conversation comments
    for c in gh(f"/repos/{repo}/issues/comments", {"since": SINCE, "per_page": 100}):
        if c["created_at"] < SINCE or c["user"]["login"] == ME:
            continue
        it = issue(c["issue_url"])
        mine = it["user"]["login"] == ME and "pull_request" in it
        if mine or mentioned(c["body"]):
            kind = "comment on your PR" if mine else "mention"
            post(f"{repo} #{it['number']}: {kind} by {c['user']['login']}", c["html_url"], c["body"], 0x3498DB if mine else 0xF1C40F, c["user"]["login"])
    # review comments on code
    for c in gh(f"/repos/{repo}/pulls/comments", {"since": SINCE, "per_page": 100}):
        if c["created_at"] < SINCE or c["user"]["login"] == ME:
            continue
        pr = issue(c["pull_request_url"])
        if pr["user"]["login"] == ME or mentioned(c["body"]):
            post(f"{repo} #{pr['number']}: review comment by {c['user']['login']} on {c.get('path', '')}", c["html_url"],
                 c["body"], 0x9B59B6, c["user"]["login"])
    # reviews and state changes on his PRs
    for pr in gh("/search/issues", {"q": f"repo:{repo} is:pr author:{ME} updated:>={SINCE[:19]}Z", "per_page": 100}):
        n = pr["number"]
        for rv in gh(f"/repos/{repo}/pulls/{n}/reviews", {"per_page": 100}):
            if (rv.get("submitted_at") or "") >= SINCE and rv["user"]["login"] != ME:
                post(f"{repo} #{n}: review {rv['state'].lower().replace('_', ' ')} by {rv['user']['login']}", rv["html_url"],
                     rv.get("body"), 0x9B59B6, rv["user"]["login"])
        if pr.get("closed_at") and pr["closed_at"] >= SINCE:
            full = gh(f"/repos/{repo}/pulls/{n}")
            merged = bool(full.get("merged_at"))
            post(f"{repo} #{n} {'MERGED' if merged else 'closed'}: {pr['title']}", pr["html_url"],
                 f"by {(full.get('merged_by') or {}).get('login', '?') if merged else 'the maintainer'}", 0x2ECC71 if merged else 0xE74C3C, ME)
    # PRs he opened
    for it in gh("/search/issues", {"q": f"repo:{repo} is:pr author:{ME} created:>={SINCE[:19]}Z", "per_page": 100}):
        post(f"{repo} #{it['number']}: your PR opened: {it['title']}", it["html_url"], it.get("body"), 0x2ECC71, ME)
    # mentions in new issue / PR bodies
    for it in gh("/search/issues", {"q": f"repo:{repo} mentions:{ME} created:>={SINCE[:19]}Z", "per_page": 100}):
        if it["user"]["login"] != ME and mentioned(it.get("body")):
            post(f"{repo} #{it['number']}: mentioned in a new {'PR' if 'pull_request' in it else 'issue'} by {it['user']['login']}",
                 it["html_url"], it.get("body"), 0xF1C40F, it["user"]["login"])

if os.environ.get("TEST") == "1":
    post("upstream watch is running", "https://github.com/watchthelight-labs/.github/actions",
         f"Watching {', '.join(REPOS)} for comments on PRs by {ME}, closes and merges, and mentions.", 0x95A5A6, "upstream-watch")

seen = set()
for i in range(0, len(posts), 10):
    batch = [p for p in posts[i:i + 10] if not (p["url"] in seen or seen.add(p["url"]))]
    if batch:
        req = urllib.request.Request(HOOK, data=json.dumps({"username": "NullMoth watch", "embeds": batch}).encode(),
                                     headers={"Content-Type": "application/json", "User-Agent": "upstream-watch"})
        urllib.request.urlopen(req).read()
print(f"since {SINCE}: {len(posts)} post(s)")
