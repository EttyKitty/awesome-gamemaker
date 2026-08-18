"""Update repository statuses and star counts in a README file."""

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
from typing import Final

LOG_FORMAT: Final[str] = "%(levelname)s: %(message)s"
README_PATH: Final[Path] = Path("README.md")
GITHUB_TOKEN: Final[str | None] = os.getenv("GITHUB_TOKEN")

RATE_LIMIT_STATUS_CODES: Final[set[int]] = {403, 429}
NOT_FOUND_CODE: Final[int] = 404
ACTIVE_DAYS: Final[int] = 90
SEMI_ACTIVE_DAYS: Final[int] = 180

ROW_REGEX: Final[re.Pattern[str]] = re.compile(
    r"^(\|.*?\[.*?\]\((https?://[^\)]+)\).*?\|.*?\|)(.*?)(\|.*)$",
    re.MULTILINE,
)

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def get_repo_info(repo_url: str) -> tuple[str | None, int | None]:
    """Fetch the latest commit date and star count from the HEAD (default branch)."""
    match = re.search(r"github\.com/([^/]+)/([^/)]+)", repo_url)
    if not match:
        return None, None

    owner, repo = match.groups()
    repo = repo.split("/")[0].replace(".git", "")

    api_url = f"https://api.github.com/repos/{owner}/{repo}/commits/HEAD"
    req = urllib.request.Request(api_url)
    req.add_header("Accept", "application/vnd.github+json")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")

    try:
        time.sleep(0.5)
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            return data.get("commit", {}).get("committer", {}).get("date"), data.get("stargazers_count")
    except urllib.error.HTTPError as e:
        if e.code in RATE_LIMIT_STATUS_CODES:
            logger.critical("Rate limit hit on %s. Terminating.", repo_url)
            sys.exit(1)
        if e.code == NOT_FOUND_CODE:
            return "DEAD", None
        logger.error("HTTP Error %s for %s", e.code, repo_url)
    except (urllib.error.URLError, TimeoutError):
        logger.error("Connection error for %s", repo_url)

    return None, None


def calculate_status(date_str: str | None) -> str:
    """Calculate the status badge based on the date string."""
    if not date_str:
        return "Unknown"

    if date_str == "DEAD":
        return "⚠️ Dead Link"

    try:
        last_commit_date = datetime.datetime.fromisoformat(
            date_str.replace("Z", "+00:00")
        )

        now = datetime.datetime.now(datetime.timezone.utc)
        days_diff = (now - last_commit_date).days

        if days_diff <= ACTIVE_DAYS:
            return "🟢 Active"
        if days_diff <= SEMI_ACTIVE_DAYS:
            return "🟡 Semi-Active"
    except (ValueError, TypeError):
        return "Unknown"
    else:
        return "🔴 Inactive"


def update_readme() -> None:
    """Parse README, update statuses and star counts for all URLs, and save changes."""
    if not README_PATH.exists():
        logger.error("%s not found.", README_PATH)
        return

    with README_PATH.open(encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines: list[str] = []
    update_count = 0

    for line in lines:
        match = ROW_REGEX.search(line)
        if not match:
            updated_lines.append(line)
            continue

        prefix, url, _, _ = match.groups()
        logger.info("Processing: %s", url)

        pushed_at, stars = get_repo_info(url)
        new_status = calculate_status(pushed_at)

        stars_cell = f"{stars:,}" if stars is not None else "-"
        new_line = f"{prefix} {new_status.strip()} | {stars_cell} |\n"
        updated_lines.append(new_line)
        update_count += 1

    with README_PATH.open("w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    logger.info("Successfully updated %d entries.", update_count)


if __name__ == "__main__":
    update_readme()
