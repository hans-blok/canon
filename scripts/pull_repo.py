import argparse
import os
import subprocess
import sys
from pathlib import Path

GITHUB_OWNER = "hans-blok"


def run(cmd, cwd=None):
    proc = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return proc.returncode, proc.stdout.strip()


def detect_default_branch(remote_url: str) -> str:
    code, out = run(["git", "ls-remote", "--symref", remote_url, "HEAD"])
    if code != 0:
        raise RuntimeError(f"Failed to query default branch for {remote_url}:\n{out}")
    # Expected first line like: 'ref: refs/heads/main    HEAD'
    for line in out.splitlines():
        if line.startswith("ref: refs/heads/") and line.rstrip().endswith("HEAD"):
            ref = line.split()[1] if len(line.split()) > 1 else line.split()[0]
            branch = ref.replace("refs/heads/", "")
            return branch
    # Fallback
    return "main"


def ensure_external_dir(root: Path) -> Path:
    external = root / "external"
    external.mkdir(parents=True, exist_ok=True)
    return external


def pull_or_clone(repo_name: str, root: Path):
    external = ensure_external_dir(root)
    target = external / repo_name
    remote_url = f"https://github.com/{GITHUB_OWNER}/{repo_name}.git"

    if target.exists():
        # Existing directory: try to pull
        git_dir = target / ".git"
        if not git_dir.exists():
            # Not a git repo; abort for safety
            raise RuntimeError(f"Target exists but is not a git repo: {target}")
        # Make sure origin points to expected remote
        code, origin_url = run(["git", "-C", str(target), "remote", "get-url", "origin"])
        if code != 0:
            raise RuntimeError(f"Unable to read origin remote in {target}:\n{origin_url}")
        if origin_url != remote_url:
            code, out = run(["git", "-C", str(target), "remote", "set-url", "origin", remote_url])
            if code != 0:
                raise RuntimeError(f"Failed to set origin to {remote_url}:\n{out}")
        # Fetch and pull default branch
        default_branch = detect_default_branch(remote_url)
        code, out = run(["git", "-C", str(target), "fetch", "origin", "--prune"])
        if code != 0:
            raise RuntimeError(f"Fetch failed in {target}:\n{out}")
        code, out = run(["git", "-C", str(target), "pull", "origin", default_branch])
        if code != 0:
            raise RuntimeError(f"Pull failed in {target}:\n{out}")
        return f"Pulled origin/{default_branch} into {target}"
    else:
        # Clone fresh
        parent = target.parent
        parent.mkdir(parents=True, exist_ok=True)
        code, out = run(["git", "clone", remote_url, str(target)])
        if code != 0:
            raise RuntimeError(f"Clone failed: {remote_url}\n{out}")
        return f"Cloned {remote_url} into {target}"



def main():
    parser = argparse.ArgumentParser(description="Pull or clone a GitHub repo from hans-blok by name.")
    parser.add_argument("repo", nargs="?", help="Repository name, e.g., 'agent-services'")
    args = parser.parse_args()

    repo = args.repo
    if not repo:
        try:
            repo = input("Voer de repo-naam in (bijv. agent-services): ").strip()
        except EOFError:
            print("No repo name provided.", file=sys.stderr)
            sys.exit(2)
    if not repo:
        print("Repository name is required.", file=sys.stderr)
        sys.exit(2)

    root = Path(__file__).resolve().parent.parent
    try:
        msg = pull_or_clone(repo, root)
        print(msg)
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
