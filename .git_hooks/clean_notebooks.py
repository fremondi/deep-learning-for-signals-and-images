from pathlib import Path
import nbformat as nbf

for path in Path(".").rglob("*.ipynb"):
    nb = nbf.read(path, as_version=4)
    nb.metadata.pop("widgets", None)
    for cell in nb.cells:
        md = cell.get("metadata", {})
        md.pop("widgets", None)
        md.pop("widget_state", None)
    nbf.write(nb, path)
    print("cleaned", path)
