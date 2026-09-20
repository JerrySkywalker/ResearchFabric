#!/usr/bin/env python3
"""Validate ResearchFabric's bilingual portal shape and local references."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT = (
    "README.md",
    "README.zh-CN.md",
    "MANIFESTO.md",
    "MANIFESTO.zh-CN.md",
    "AGENTS.md",
    "AGENTS.zh-CN.md",
    "CONTRIBUTING.md",
    "CONTRIBUTING.zh-CN.md",
    "SECURITY.md",
    "SECURITY.zh-CN.md",
    "LICENSE",
    "LICENSE.zh-CN.md",
)
REQUIRED_DOCS = (
    "docs/README.md",
    "docs/architecture/overview.md",
    "docs/architecture/product-topology.md",
    "docs/architecture/repository-model.md",
    "docs/philosophy/README.md",
    "docs/philosophy/why-research-fabric-exists.md",
    "docs/philosophy/ai4s-and-agent-native-research.md",
    "docs/philosophy/knowledge-vs-evidence.md",
    "docs/philosophy/humans-agents-and-authority.md",
    "docs/philosophy/git-native-research.md",
    "docs/philosophy/provider-machine-independence.md",
    "docs/philosophy/non-goals.md",
)
REQUIRED_BRAND = (
    "docs/assets/brand/research-fabric-logo.svg",
    "docs/assets/brand/research-fabric-mark.svg",
    "docs/assets/brand/research-fabric-banner.svg",
    "docs/assets/brand/research-fabric-banner.zh-CN.svg",
)
REQUIRED_DATA = (
    "components/manifest.yaml",
    "compatibility/release-set.example.yaml",
)
MARKDOWN_LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")


def chinese_peer(path: Path) -> Path:
    return path.with_name(path.stem + ".zh-CN.md")


def english_peer(path: Path) -> Path:
    return path.with_name(path.name.replace(".zh-CN.md", ".md"))


def validate_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for raw in MARKDOWN_LINK.findall(text):
        target = raw.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        local = unquote(target.split("#", 1)[0])
        if local and not (path.parent / local).resolve().exists():
            errors.append(f"broken local link in {path.relative_to(ROOT)}: {target}")


def main() -> int:
    errors: list[str] = []
    required = REQUIRED_ROOT + REQUIRED_DOCS + REQUIRED_BRAND + REQUIRED_DATA
    for relative in required:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    markdown = sorted(ROOT.rglob("*.md"))
    for path in markdown:
        if path.name == "LICENSE.zh-CN.md":
            counterpart = ROOT / "LICENSE"
        elif path.name.endswith(".zh-CN.md"):
            counterpart = english_peer(path)
        else:
            counterpart = chinese_peer(path)
        if not counterpart.is_file():
            errors.append(f"missing bilingual counterpart for {path.relative_to(ROOT)}")
        validate_links(path, errors)

    for relative in REQUIRED_BRAND:
        path = ROOT / relative
        if path.is_file():
            try:
                ET.parse(path)
            except ET.ParseError as exc:
                errors.append(f"invalid SVG XML {relative}: {exc}")

    english = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
    chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8") if (ROOT / "README.zh-CN.md").is_file() else ""
    if "README.zh-CN.md" not in english:
        errors.append("English README lacks Simplified-Chinese link")
    if "README.md" not in chinese:
        errors.append("Simplified-Chinese README lacks English link")
    if (ROOT / ".gitmodules").exists():
        errors.append(".gitmodules must not exist")

    if errors:
        print("PORTAL_DOCS=FAIL")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        "PORTAL_DOCS=PASS "
        f"markdown_documents={len(markdown)} brand_assets={len(REQUIRED_BRAND)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

