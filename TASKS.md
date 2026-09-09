# Git practice tasks

Work through these roughly in order. Each one names the concept it drills
and what "done" looks like — it deliberately does *not* spell out exact
commands, so you build recall instead of copying. If you get stuck, the
command reference at the bottom (and `concepts.txt`) has what you need.

Part A is foundations (Week 4). Part B is the focus of the actual
in-class assessment (Week 7–8: branching, merging, conflicts) — spend
most of your time there, and try Part B a few times until it's fast.

## Part A — Foundations

### 1. Check your setup
Confirm Git knows who you are, and that new repos default to a branch
called `main`. Fix anything that isn't already set correctly.
**Done when:** `git config --list` shows a correct `user.name`,
`user.email`, and `init.defaultBranch`.

### 2. The stage → commit cycle
Add a new model to `RATES` in `shop.py` (e.g. `"electric": 18.0`), then
give it starting stock in `FLEET`. Before staging, look at what changed.
After staging, look again — notice the second view answers a different
question than the first.
**Done when:** you've used both "unstaged diff" and "staged diff" at
least once, then committed with a clear, imperative-mood message.

### 3. .gitignore in practice
Create a throwaway file that shouldn't be tracked (e.g. `notes.local.txt`
or a `__pycache__/` folder from actually running `shop.py`). Ignore it
properly. Then deliberately commit a file you shouldn't have, and
practice removing it from tracking *without* deleting it from disk.
**Done when:** the ignored file no longer shows up in `git status`, and
you've used the "stop tracking but keep on disk" command once for real.

### 4. Fix your last commit, not a new one
Make a commit with a slightly wrong message or missing a small file,
*then* fix it in place instead of stacking a correction commit on top.
**Done when:** `git log` shows one clean commit, not two, and you
understand why this is only safe for commits nobody else has seen yet.

### 5. Read history like a graph
Add two or three more small, separate commits (separate concerns, not
one blob). Then view history three different ways: full detail, one line
per commit, and the ASCII graph across all branches.
**Done when:** you can explain, from the graph output alone, which
commit is the parent of which.

## Part B — Branching, merging, conflicts (the assessed skills)

### 6. Create a branch and make it diverge
Create a feature branch off `main`. On it, add a `total_bikes()` function
to `shop.py` that returns the sum of everything in `FLEET`. Commit it.
**Done when:** `git branch -vv` shows your new branch ahead of `main`,
and `main` itself is untouched (switch back and check `shop.py` there).

### 7. Fast-forward merge
Merge that branch straight back into `main`, with no new commits having
landed on `main` in the meantime.
**Done when:** you can say whether Git created a new merge commit or
just moved a pointer, and you can explain why.

### 8. A true (three-way) merge
Create a new branch. Make a commit on it. Switch to `main` and make a
*different* commit there too (different part of the file), so the two
lines of history diverge. Now merge the branch into `main`.
**Done when:** `git log --oneline --graph --all` shows a merge commit
with two parents.

### 9. Force a merge conflict, then resolve it
Create two branches from the same starting point. On each, edit the
*same line* of `shop.py` differently (e.g. change `OPENING_HOURS` to two
different values). Merge the first branch into `main` cleanly, then try
to merge the second.
**Done when:** you've seen Git refuse to auto-merge, opened the file and
found the `<<<<<<<` / `=======` / `>>>>>>>` markers, manually chosen the
final content, staged the resolved file, and completed the merge commit.
Run `shop.py` afterward to confirm it still works.

### 10. Clean up
Delete the branches from tasks 6–9 now that they're merged. Try deleting
one that still has unmerged work on it and notice Git protects you —
then force it if you're sure.
**Done when:** `git branch` only lists branches you still need.

### 11. Stash a work-in-progress
Start editing `shop.py` (don't commit). Pretend an urgent fix is needed
on `main` right now: shelve your half-done change, switch branches,
make and commit the "urgent" fix, switch back, and restore your shelved
work.
**Done when:** your original edit is back in the working tree and the
stash list is empty again.

### 12. Tag a release point
Once `main` is in a good state, mark it. Use an annotated tag with a
message, then confirm you can inspect what it points to and who/why.
**Done when:** `git show` on your tag prints the tagger, message, and
underlying commit.

## Optional — Part C, remote workflow

Only do this once Part B is solid — the in-class assessment is local
Git, but this rounds out the picture. You already have `origin` pointing
at `https://github.com/NguKhangWei/github.git`.

### 13. Publish a branch and simulate review
Push `main`. Then create one more feature branch, push *it* explicitly
(note it needs the remote+branch named the first time), and open a pull
request on GitHub comparing it against `main` before merging.
**Done when:** you can explain the difference between what `git fetch`,
`git pull`, and `git push` each touch.

## Dry run (do this last, under a timer)

Simulate the actual demonstration: in one sitting, with a 10–15 minute
timer, do tasks 6, 9, and 10 back-to-back on a fresh small change —
branch, edit, stage, commit, merge, hit a conflict, resolve it, verify
`shop.py` still runs, clean up. This is the exact shape of what you'll
be asked to do live.

---

## Command reference

| Command | What it does |
|---|---|
| `git status` | What's staged, modified, untracked. |
| `git diff` / `git diff --staged` | Unstaged changes / what will be committed. |
| `git add <file>` | Stage a file's current content. |
| `git commit -m "..."` | Record the staged snapshot. |
| `git commit --amend` | Replace the tip commit instead of stacking a new one. |
| `git log --oneline --graph --decorate --all` | See the whole DAG at once. |
| `git branch` / `git branch -vv` | List branches / list with upstream + ahead-behind. |
| `git switch -c <name>` | Create and switch to a new branch. |
| `git switch <name>` | Switch to an existing branch. |
| `git merge <branch>` | Merge a branch into the current one. |
| `git branch -d <name>` / `-D` | Delete a merged branch / force-delete. |
| `git stash` / `git stash pop` | Shelve changes / restore them. |
| `git tag -a v1.0 -m "..."` | Create an annotated tag. |
| `git rm --cached <file>` | Stop tracking a file, keep it on disk. |
| `git fetch` / `git pull` / `git push` | Download only / download+merge / upload. |
