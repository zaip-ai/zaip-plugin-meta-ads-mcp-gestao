"""Gere o ZIP portátil que o Plugin Creator recebe no ChatGPT Work."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    root = Path(__file__).resolve().parents[1]
    plugin = root / "plugins" / "meta-ads-gestao"
    dest = root / "dist" / "meta-ads-gestao.zip"
    dest.parent.mkdir(exist_ok=True)
    manifests = [plugin / "plugin.json", plugin / "mcp.json"]
    skills = sorted((plugin / "skills").rglob("*"))
    assets = sorted((plugin / "assets").glob("*"))
    with ZipFile(dest, "w") as archive:
        for path in [*manifests, *skills, *assets]:
            if path.is_file():
                entry = ZipInfo(path.relative_to(plugin).as_posix())
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = 0o100644 << 16
                data = path.read_bytes()
                if path.suffix in {".json", ".md", ".yaml"}:
                    data = data.replace(b"\r\n", b"\n")
                archive.writestr(entry, data)


if __name__ == "__main__":
    main()
