import json
import os
import sys

# Load affected packages from the file
with open("../affected-packages.txt", "r", encoding="utf-8") as f:
    affected_packages = set(line.strip().lower() for line in f if line.strip())

def scan_lock_file():
    findings = []

    if not os.path.exists("package-lock.json"):
        return ["No package-lock.json file found. Use npm ci to generate it."]

    try:
        with open("package-lock.json", "r", encoding="utf-8") as f:
            lock_data = json.load(f)
    except json.JSONDecodeError:
        return ["Failed to parse package-lock.json. It may be malformed."]

    def check_dependencies(deps, path=""):
        for name, info in deps.items():
            full_path = f"{path}/{name}" if path else name
            if name.lower() in affected_packages:
                findings.append(f"Compromised package found: {full_path}")
            if "dependencies" in info:
                check_dependencies(info["dependencies"], full_path)

    if "dependencies" in lock_data:
        check_dependencies(lock_data["dependencies"])

    return findings if findings else ["No signs of Shai-Hulud infection in package-lock.json."]

# Run scan
results = scan_lock_file()
print("Scan Results for Shai-Hulud Infection:\n")
for result in results:
    print("-", result)

# Exit with error if any compromised packages are found
if any("Compromised package" in r for r in results):
    sys.exit(1)
