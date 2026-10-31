# SPDX-License-Identifier: AGPL-3.0-or-later
# Commercial license available
# © Concepts 1996–2026 Miroslav Šotek. All rights reserved.
# © Code 2020–2026 Miroslav Šotek. All rights reserved.
# ORCID: 0009-0009-3560-0851
# Contact: www.anulum.li | protoscience@anulum.li
# SCPN Muon Fusion Core — repository-level truth tests

"""Repository-level contract tests: the scaffold stays truthful."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from manifest_io import load_json_object

REPO = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = (
    ".editorconfig",
    ".gitattributes",
    ".github/CODEOWNERS",
    ".github/FUNDING.yml",
    ".github/dependabot.yml",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/workflow-inventory.json",
    ".github/workflows/ci.yml",
    ".github/workflows/reusable-static-policy.yml",
    ".github/workflows/reusable-tests.yml",
    ".gitignore",
    ".pre-commit-config.yaml",
    ".zenodo.json",
    "ARCHITECTURE.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "CONTRIBUTORS.md",
    "GOVERNANCE.md",
    "LICENSE",
    "Makefile",
    "NOTICE.md",
    "README.md",
    "REUSE.toml",
    "ROADMAP.md",
    "SECURITY.md",
    "SUPPORT.md",
    "VALIDATION.md",
    "_typos.toml",
    "capability-inventory.json",
    "conftest.py",
    "docs/ARCHITECTURE.md",
    "docs/CONTROL_ADAPTER_SPECIFICATION.md",
    "docs/THREAT_MODEL.md",
    "docs/adr/0001-repository-boundary.md",
    "papers/README.md",
    "papers/submissions/README.md",
    "pyproject.toml",
    "reactor-domain.json",
    "requirements-dev.txt",
    "studio/portfolio-descriptor.json",
    "studio/portfolio-descriptor.schema.json",
    "tools/audit_workflows.py",
    "tools/check_commit_trailers.py",
    "tools/derive_studio_descriptor.py",
    "tools/generate_capability_inventory.py",
    "tools/manifest_io.py",
    "tools/preflight.py",
    "tools/validate_reactor_domain.py",
)

REQUIRED_IGNORE_LINES = (
    "/BACKUP/",
    "/ARCHIVE/",
    "/.coordination/",
    "/04_ARCANE_SAPIENCE/",
)

FORBIDDEN_BADGE_MARKERS = (
    "api.reuse.software/badge/",
    "api.scorecard.dev/projects/",
    "bestpractices.dev/projects/",
    "pypi.org/project/",
)

WORKFLOW_BADGES = {
    "CI": "ci.yml",
    "CodeQL": "codeql.yml",
    "Pre-commit": "pre-commit.yml",
    "Security audit": "security-audit.yml",
    "Docs": "docs.yml",
}
STATIC_BADGES = {
    "License: AGPL-3.0-or-later": (
        "https://img.shields.io/badge/License-AGPL--3.0--or--later-blue.svg",
        "LICENSE",
    ),
    "Commercial license available": (
        "https://img.shields.io/badge/Commercial_license-available-success.svg",
        "mailto:protoscience@anulum.li?subject=SCPN%20Muon%20Fusion%20Core%20Commercial%20License",
    ),
    "Sponsor": (
        (
            "https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa"
            "?logo=githubsponsors&logoColor=white"
        ),
        "https://github.com/sponsors/anulum",
    ),
}
WORKFLOW_ROOT = "https://github.com/anulum/scpn-muon-fusion-core/actions/workflows/"
BADGE = re.compile(r"\[!\[([^\]]+)\]\(([^)\s]+)\)\]\(([^)\s]+)\)")


@pytest.mark.parametrize("relative", REQUIRED_PATHS)
def test_required_path_exists_and_is_not_empty(relative: str) -> None:
    """Every Tier-0 and reactor-standard surface exists with content."""
    path = REPO / relative
    assert path.is_file(), relative
    assert path.stat().st_size > 0, relative


def test_gitignore_carries_defensive_lines() -> None:
    """The ignore rules keep agent-state and backup trees out."""
    lines = {
        line.strip()
        for line in (REPO / ".gitignore").read_text(encoding="utf-8").splitlines()
    }
    for required in REQUIRED_IGNORE_LINES:
        assert required in lines, required


def test_readme_carries_no_unearned_badge() -> None:
    """No badge appears before its live evidence exists."""
    readme = (REPO / "README.md").read_text(encoding="utf-8")
    for marker in FORBIDDEN_BADGE_MARKERS:
        assert marker not in readme, marker


def earned_badge_findings(readme: str) -> list[str]:
    """Report every README badge that is not bound to earned evidence.

    Parameters
    ----------
    readme
        README source.

    Returns
    -------
    list[str]
        Findings for unknown badges, badges bound to the wrong object,
        workflow badges without a workflow file, and a missing earned
        badge; empty when the block is exactly the qualified set.
    """
    findings: list[str] = []
    seen: set[str] = set()
    for label, image, target in BADGE.findall(readme):
        seen.add(label)
        if label in WORKFLOW_BADGES:
            workflow = WORKFLOW_BADGES[label]
            expected = (
                f"{WORKFLOW_ROOT}{workflow}/badge.svg?branch=main",
                f"{WORKFLOW_ROOT}{workflow}",
            )
            if not (REPO / ".github" / "workflows" / workflow).is_file():
                findings.append(f"{label}: workflow {workflow} does not exist")
        elif label in STATIC_BADGES:
            expected = STATIC_BADGES[label]
        else:
            findings.append(f"{label}: badge is not in the qualified set")
            continue
        if (image, target) != expected:
            findings.append(f"{label}: bound to {image} -> {target}")
    missing = (set(WORKFLOW_BADGES) | set(STATIC_BADGES)) - seen
    findings.extend(f"{label}: earned badge missing" for label in sorted(missing))
    return findings


def test_readme_badges_are_exactly_the_earned_set() -> None:
    """Every badge is bound to this repository's earned evidence."""
    readme = (REPO / "README.md").read_text(encoding="utf-8")
    assert earned_badge_findings(readme) == []


@pytest.mark.parametrize(
    ("before", "after", "expected"),
    [
        ("workflows/ci.yml/badge.svg", "workflows/ci2.yml/badge.svg", "CI: bound"),
        ("scpn-muon-fusion-core/actions", "scpn-fusion-core/actions", "CI: bound"),
        ("[![Docs]", "[![Coverage]", "Coverage: badge is not"),
        ("[![Sponsor]", "[![Sponsors]", "Sponsor: earned badge missing"),
    ],
    ids=["wrong-workflow", "foreign-repository", "unknown-badge", "dropped-badge"],
)
def test_unbound_badge_is_detected(before: str, after: str, expected: str) -> None:
    """A badge bound to anything but the earned evidence is a finding."""
    readme = (REPO / "README.md").read_text(encoding="utf-8")
    assert before in readme
    findings = earned_badge_findings(readme.replace(before, after, 1))
    assert any(finding.startswith(expected) for finding in findings), findings


def test_changelog_starts_unreleased() -> None:
    """The changelog carries an Unreleased section and no invented release."""
    changelog = (REPO / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "[Unreleased]" in changelog


def test_manifest_declares_exact_configuration_assignment() -> None:
    """The manifest owns exactly its mapped registry configurations."""
    manifest = load_json_object(REPO / "reactor-domain.json")
    assert manifest["project"] == "SCPN-MUON-FUSION-CORE"
    assert manifest["configurations"] == [
        "scpn.reactor_systems:muon_catalysed_fusion",
    ]
    assert manifest["evidence_maturity"] == "architecture_only"
    assert manifest["capabilities"] == []
    assert manifest["claims"] == []
    assert manifest["spo_registry"]["version"] == "1.1.0"


def test_descriptor_and_inventory_embed_current_manifest_digest() -> None:
    """Derived artefacts point at the exact committed manifest bytes."""
    from manifest_io import sha256_of_file

    digest = sha256_of_file(REPO / "reactor-domain.json")
    descriptor = load_json_object(REPO / "studio" / "portfolio-descriptor.json")
    inventory = load_json_object(REPO / "capability-inventory.json")
    assert descriptor["source"]["manifest_sha256"] == digest
    assert inventory["source"]["manifest_sha256"] == digest
    assert descriptor["lifecycle"]["state"] == "not_federated"
    assert inventory["implemented_capability_count"] == 0


def test_no_agent_state_trees_exist() -> None:
    """Forbidden agent-state paths are absent from the repository."""
    for forbidden in (
        ".coordination",
        "04_ARCANE_SAPIENCE",
        "BACKUP",
        "ARCHIVE",
    ):
        assert not (REPO / forbidden).exists(), forbidden


def test_descriptor_matches_ratified_schema() -> None:
    """The committed descriptor matches the ratified 1.1.0 schema shape."""
    schema = load_json_object(REPO / "studio" / "portfolio-descriptor.schema.json")
    descriptor = load_json_object(REPO / "studio" / "portfolio-descriptor.json")
    assert schema["$id"].endswith("/studio-portfolio-descriptor/1.1.0")
    assert schema["additionalProperties"] is False
    assert sorted(schema["required"]) == sorted(descriptor)
    assert sorted(schema["properties"]) == sorted(descriptor)
    assert descriptor["schema_version"] == "1.1.0"
