def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("\nChecking dependencies:")
    dependencies = True
    try:
        import pandas
        print("[OK] pandas (", pandas.__version__, ")",
              " - Data manipulation ready", sep="")
    except ModuleNotFoundError:
        print("[KO] pandas is missing")
        print("\nInstall dependencies with pip: pip install -r ",
              "requirements.txt", sep="")
        print("Install dependencies with Poetry: poetry install\n")
        dependencies = False

    try:
        import numpy
        print("[OK] numpy (", numpy.__version__, ")",
              " - Numerical computation ready", sep="")
    except ModuleNotFoundError:
        print("[KO] numpy is missing")
        print("\nInstall dependencies with pip: pip install -r ",
              "requirements.txt", sep="")
        print("Install dependencies with Poetry: poetry install\n")
        dependencies = False

    print("\npip vs Poetry:")
    print(" requirements.txt declares what to install;", end="")
    print(" pip resolves it at install time.")
    print(" pyproject.toml declares the same constraints,", end="")
    print(" and Poetry pins the resolved")
    print(" versions in poetry.lock so every install is identical.")

    if dependencies:
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
