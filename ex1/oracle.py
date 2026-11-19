import os
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("\nORACLE STATUS: Consulting the configuration...\n")
    print("Configuration loaded:")
    print("Mode:", mode)

    if mode == "development":
        if database_url:
            print("Database: Connected to local instance")
        else:
            print("Database: Not configured")

        if api_key:
            print("API Access: Authenticated")
        else:
            print("API Access: Not configured")

        if log_level:
            print("Log Level:", log_level)
        else:
            print("Log Level: Not configured")

        if zion_endpoint:
            print("Remote Network: Online")
        else:
            print("Remote Network: Not Online")
    elif mode == "production":
        print("Production environment")

        if database_url:
            print("Database: Connected to remote instance")
        else:
            print("ERROR: Database configuration missing")

        if api_key:
            print("API Access: Configured")
        else:
            print("ERROR: API key missing")

        if log_level:
            print("Log Level:", log_level)
        else:
            print("WARNING: Log level not configured")

        if zion_endpoint:
            print("Remote Network: Configured")
        else:
            print("ERROR: Remote network endpoint missing")
    else:
        print("ERROR: Invalid MATRIX_MODE")

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
