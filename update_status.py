"""Update repository statuses in a README file based on last commit date."""

import datetime
import json
import logging
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

README_PATH = Path("README.md")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
RATE_LIMIT_STATUS_CODES = {403, 429}
NOT_FOUND_CODE = 404
ACTIVE_DAYS = 90
SEMI_ACTIVE_DAYS = 180
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36",
}


def get_github_date(repo_url: str) -> str | None:
    """Fetch the last commit date for a GitHub repository."""
    match = re.search(r"github\.com/([^/]+)/([^/)]+)", repo_url)
    if not match:
        return None

    owner, repo = match.groups()
    repo = repo.split("/")[0].replace(".git", "")

    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(api_url, method="GET")

    if GITHUB_TOKEN:
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")

    try:
        time.sleep(0.5)
        with urllib.request.urlopen(req, timeout=3) as response:
            data = json.loads(response.read().decode())
            return data.get("pushed_at")
    except urllib.error.HTTPError as e:
        if e.code in RATE_LIMIT_STATUS_CODES:
            logger.error("CRITICAL: Rate limit hit on %s. Stopping script.", repo_url)
            sys.exit(1)
        if e.code == NOT_FOUND_CODE:
            return "DEAD"
        logger.error("Error fetching %s", repo_url)
        return None
    except urllib.error.URLError:
        logger.error("URL error for %s", repo_url)
        return None

def calculate_status(date_str: str | None) -> str:
    """Calculate the status of a repository based on its last commit date."""
    if not date_str:
        return "Unknown"

    if date_str == "DEAD":
        return "⚠️ Dead Link"

    last_push = datetime.datetime.strptime(date_str[:10], "%Y-%m-%d").replace(
        tzinfo=datetime.timezone.utc,
    )
    now = datetime.datetime.now(datetime.timezone.utc)
    days_diff = (now - last_push).days

    if days_diff <= ACTIVE_DAYS:
        return "🟢 Active"
    if days_diff <= SEMI_ACTIVE_DAYS:
        return "🟡 Semi-Active"
    return "🔴 Inactive"


def update_readme() -> None:
    """Update the README file with the latest status of repositories."""
    with README_PATH.open(encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines: list[str] = []

    row_regex = r"(\|.*?\[.*?\]\((https:\/\/github\.com\/[^\)]+)\).*?\|.*?\|)(.*?)(\|)"

    count = 0
    for line in lines:
        match = re.search(row_regex, line)
        if match:
            prefix, url, _, suffix = match.groups()
            logger.info("Checking: %s", url)

            last_push = get_github_date(url)
            new_status = calculate_status(last_push)

            new_line = f"{prefix} {new_status} {suffix}\n"
            updated_lines.append(new_line)
            count += 1
            continue

        updated_lines.append(line)

    with README_PATH.open("w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    logger.info("Done! Updated %d links.", count)


if __name__ == "__main__":
    update_readme()
