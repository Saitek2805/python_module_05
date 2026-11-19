import sys
import os
import site


def main() -> None:
    if sys.prefix == sys.base_prefix:
        print("LABORATORY STATUS: You are working in the open")
        inside = False
    else:
        print("LABORATORY STATUS: The laboratory is sealed")
        inside = True
    print("\nCurrent python:", sys.executable)
    print("Virtual Environment: ", end="")
    if inside:
        print(os.path.basename(sys.prefix))
        print("Environment path:", sys.prefix)
        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print("\nReagent installation path:")
        print(site.getsitepackages()[0])
    else:
        print("None detected")
        print("\nWARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print("\nTo seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
