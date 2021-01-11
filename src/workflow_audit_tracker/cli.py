import argparse
from workflow_audit_tracker.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Traceability utilities for pipeline runs, parameters, and audit checkpoints.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
