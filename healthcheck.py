"""Container health probe that does not call the model provider."""

from pathlib import Path


def main() -> None:
    if not Path("app.py").exists():
        raise SystemExit("application files are missing")
    print("ok")


if __name__ == "__main__":
    main()
