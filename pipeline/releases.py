#!/usr/bin/env python3
"""Knowledge is built per T24 release. jar/ is R23 (MANIFEST R23_AMR.0); the
installed Model Bank C:\R25 is R25 (read-only). Each release has its own
complete DB -- never a delta over another release (plan Decision 8).
See plan/state/decisions.md "Releases"."""
from pathlib import Path

DEFAULT_RELEASE = "R23"

RELEASES = {
    "R23": Path("jar"),
    "R25": Path(r"C:\R25\bnk\t24lib"),
}


def db_path(release):
    if release not in RELEASES:
        raise ValueError(f"unknown release '{release}' -- known: {', '.join(sorted(RELEASES))}")
    if release == "R23":
        return Path("temenos_knowledge.db")
    return Path("releases") / release / "temenos_knowledge.db"


class MissingReleaseDB(SystemExit):
    pass


def open_release_db(release, db=None):
    """Open the knowledge DB for a release (or an explicit --db path). Refuses a
    missing file: sqlite3.connect would silently create an empty DB and every
    field would then look 'not found'."""
    import sqlite3
    path = Path(db) if db else db_path(release)
    if not path.is_file():
        raise MissingReleaseDB(
            f"no knowledge DB for {release} at {path} -- build it with "
            f"'python pipeline/build_release.py --release {release}'")
    return sqlite3.connect(path)


def add_release_args(ap):
    """--release (default R23) and --db (explicit path, overrides --release)."""
    ap.add_argument("--release", default=DEFAULT_RELEASE, help=f"T24 release (default {DEFAULT_RELEASE})")
    ap.add_argument("--db", default=None, help="explicit knowledge DB path (overrides --release)")


def connect(args):
    try:
        db_path(args.release)
    except ValueError as exc:
        raise SystemExit(str(exc))
    return open_release_db(args.release, args.db)
