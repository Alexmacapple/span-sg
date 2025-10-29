#!/usr/bin/env python3
"""
Wrapper pour forcer MkDocs à utiliser polling sur macOS/Docker.
Résout le problème inotify avec Docker for Mac.

Ce script force l'utilisation du PollingObserver de Watchdog
en remplaçant le module Observer AVANT l'importation de MkDocs.

Usage:
    python3 mkdocs-serve-polling.py serve [options]

Auteur: Claude Code
Date: 2025-10-28
"""
import os
import sys

# IMPORTANT: Forcer le polling AVANT toute importation de watchdog/mkdocs
os.environ["WATCHDOG_FORCE_POLLING"] = "true"

# Monkey-patch watchdog pour forcer PollingObserver
# Cela doit être fait AVANT l'importation de mkdocs
from watchdog import observers
from watchdog.observers.polling import PollingObserver

# Remplacer Observer par PollingObserver globalement
observers.Observer = PollingObserver

# Lancer MkDocs normalement avec tous les arguments
from mkdocs.__main__ import cli  # noqa: E402

if __name__ == "__main__":
    sys.exit(cli())
