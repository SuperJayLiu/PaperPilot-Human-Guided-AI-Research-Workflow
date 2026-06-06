#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def fail(message):
    print(f"Root plugin/skill check failed: {message}")
    raise SystemExit(1)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def main():
    skill_path = ROOT / "SKILL.md"
    plugin_path = ROOT / "plugin.json"
    codex_plugin_path = ROOT / ".codex-plugin" / "plugin.json"
    agent_yaml_path = ROOT / "agents" / "openai.yaml"
    marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"

    for path in [skill_path, plugin_path, codex_plugin_path, agent_yaml_path, marketplace_path]:
        if not path.exists():
            fail(f"missing {path.relative_to(ROOT)}")

    skill = skill_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", skill, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")
    frontmatter = match.group(1)
    if "name: paperpilot-research-workflow" not in frontmatter:
        fail("SKILL.md frontmatter must name paperpilot-research-workflow")
    if "AI-for-economics-and-finance" not in frontmatter:
        fail("SKILL.md description should mention companion skill routing")

    plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
    codex_plugin = json.loads(codex_plugin_path.read_text(encoding="utf-8"))
    if plugin != codex_plugin:
        fail("plugin.json and .codex-plugin/plugin.json must match")
    if plugin.get("name") != "paperpilot-research-workflow":
        fail("plugin name must be paperpilot-research-workflow")

    prompts = plugin.get("interface", {}).get("defaultPrompt", [])
    if not isinstance(prompts, list) or len(prompts) > 3:
        fail("interface.defaultPrompt must be a list of at most three prompts")

    agent_yaml = agent_yaml_path.read_text(encoding="utf-8")
    if "$paperpilot-research-workflow" not in agent_yaml:
        fail("agents/openai.yaml must include the skill invocation")

    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    entries = marketplace.get("plugins", [])
    paperpilot_entries = [entry for entry in entries if entry.get("name") == "paperpilot-research-workflow"]
    if len(paperpilot_entries) != 1:
        fail("marketplace must include exactly one paperpilot-research-workflow entry")
    if paperpilot_entries[0].get("source", {}).get("path") != "./":
        fail("marketplace source path must point to repository root")

    readme = read("README.md")
    for required in ["SKILL.md", "plugin.json", ".codex-plugin/plugin.json", "$paperpilot-research-workflow"]:
        if required not in readme:
            fail(f"README.md must mention {required}")

    print("Root plugin/skill check passed.")


if __name__ == "__main__":
    main()
