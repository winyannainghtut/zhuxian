# Zhu Xian Novel Reader

Static web reader for reading markdown chapters from:

- `eng/`
- `burmese/`

## Run Locally

From the repo root:

```powershell
powershell -ExecutionPolicy Bypass -File .\reader\run_reader.ps1
```

Then open `http://localhost:8000/reader/`.

## Refresh Index Only

```powershell
python .\reader\generate_manifest.py
```

Run this whenever new chapters are added or modified.
