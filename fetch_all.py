#!/usr/bin/env python3
"""Fetch Zhu Xian chapters 2-264 from wuxiaworld.eu into /root/RI/zhuxian/ as .md"""
import requests, time, pathlib
from bs4 import BeautifulSoup

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"}
OUT = pathlib.Path("/root/RI/zhuxian/eng")
OUT.mkdir(parents=True, exist_ok=True)
LOG = open(OUT / "fetch.log", "a")


def log(msg):
    print(msg, flush=True)
    LOG.write(msg + "\n")
    LOG.flush()


def fetch(n, tries=3):
    url = f"https://wuxiaworld.eu/chapter/zhu-xian-{n}"
    for attempt in range(tries):
        try:
            r = requests.get(url, headers=UA, timeout=25)
            if r.status_code == 200 and "reader-title" in r.text:
                soup = BeautifulSoup(r.text, "html.parser")
                t = soup.select_one("h1.reader-title")
                body = soup.select_one("#chapter-content")
                if not body:
                    raise ValueError("no content div")
                for tag in body(["script", "style", "noscript", "ins"]):
                    tag.decompose()
                paras = [p.get_text(" ", strip=True) for p in body.find_all("p")]
                if not paras:
                    paras = [l.strip() for l in body.get_text("\n").splitlines() if l.strip()]
                title = t.get_text(" ", strip=True) if t else f"Zhu Xian Chapter {n}"
                paras = [p for p in paras if "support Novels on Patreon" not in p and "adsbygoogle" not in p]
                content = "\n\n".join(paras).replace("&h.e.l.lip;", "…")
                return url, title, content
            elif r.status_code == 404:
                return url, None, None
            else:
                raise ValueError(f"HTTP {r.status_code}")
        except Exception as e:
            if attempt == tries - 1:
                log(f"{n:04d} ERROR after {tries} tries: {e}")
                return url, None, "ERROR"
            time.sleep(5)


saved = skipped = missing = errors = 0
for n in range(2, 265):
    f = OUT / f"{n:04d}.md"
    if f.exists():
        skipped += 1
        continue
    url, title, content = fetch(n)
    if content and content != "ERROR":
        f.write_text(f"# {title}\n\n{content}\n", encoding="utf-8")
        saved += 1
        if saved % 10 == 0:
            log(f"progress: {saved} new saved, at chapter {n}/264")
    elif content == "ERROR":
        errors += 1
    else:
        (OUT / f"{n:04d}.missing").touch()
        missing += 1
        log(f"{n:04d} MISSING (404)")
    time.sleep(1.5)

log(f"DONE: new_saved={saved} skipped_existing={skipped} missing={missing} errors={errors}")
