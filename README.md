## 🔍 `npm_verify`

Shai-Hulud scanner integration to verify suspicious dependencies before commits.

### 📦 Update `package.json`

Add the following script to your `package.json`:

```js
"scripts": {
  "verify": "python ../shai_hulud_scanner.py"
}
```
- You can now run `npm run verify` to scan and validate your dependencies.

### 🛡️ Git Pre-Commit Hook Setup

Prevent commits if suspicious packages are detected by the Shai-Hulud scanner.

#### 1. Create the hook file

```sh
mkdir -p .git/hooks
touch .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
#### 2. Add the following to .git/hooks/pre-commit

```sh
#!/bin/bash

echo "Running Shai-Hulud scanner before commit..."

python scripts/shai_hulud_scanner.py > /tmp/shai_scan_result.txt

if grep -q "Suspicious" /tmp/shai_scan_result.txt; then
  echo "⚠️ Potential Shai-Hulud infection detected:"
  cat /tmp/shai_scan_result.txt
  echo "❌ Commit blocked. Please investigate."
  exit 1
else
  echo "✅ No issues found. Proceeding with commit."
fi

```

## 📄 License
 MIT
