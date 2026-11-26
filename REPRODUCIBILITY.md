# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay checks 24,564 geometric lower-envelope inequalities and 30 truncation distances. It independently verifies the three-atom mixture and every selected density floor by rational arithmetic. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/geometric-mixture-explorer.zip) and open index.html. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font parameters. [Build the paper](paper/BUILD.md).
