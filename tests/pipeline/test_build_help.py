import json
import re

from build_help import build_index, frontmatter, outline, script_safe_json, write_help


def test_frontmatter_reads_folded_description():
    meta, body = frontmatter("---\nname: temenos-x\ndescription: >\n  Line one\n  line two\nmetadata:\n  version: 1.2\n---\n# Title\n")
    assert meta["name"] == "temenos-x"
    assert meta["description"] == "Line one line two"
    assert meta["version"] == "1.2"
    assert body.startswith("# Title")


def test_outline_lists_headings_with_levels():
    assert outline("# A\ntext\n## B\n### C\n") == [
        {"level": 1, "title": "A"}, {"level": 2, "title": "B"}, {"level": 3, "title": "C"}]


def test_script_safe_json_cannot_close_the_script_tag():
    out = script_safe_json({"x": "</script><script>alert(1)</script>"})
    assert "</" not in out
    assert json.loads(out.replace("<\/", "</"))["x"].startswith("</script>")


def test_index_covers_skills_templates_and_golden_cases_but_not_table_schema():
    index = build_index()
    skills = {s["id"]: s for s in index["skills"]}
    assert "temenos-dev" in skills and "temenos-l3" in skills
    assert any(f["path"] == "SKILL.md" for f in skills["temenos-l3"]["files"])
    assert not any("table-schema" in f["path"] for s in index["skills"] for f in s["files"])
    assert skills["temenos-dev"]["hasTableSchema"] is True
    types = [t["id"] for lang in index["templates"] for t in lang["types"]]
    assert "jbc/validation" in types and "java/service-lifecycle" in types
    assert {c["name"] for c in index["golden"]} >= {"jbc-customer-mnemonic-vvr", "infobasic-vvr"}


def test_written_page_embeds_the_index_once(tmp_path):
    out = tmp_path / "help.html"
    write_help(out)
    html = out.read_text(encoding="utf-8")
    assert "/*__HELP_INDEX__*/" not in html and "/*__MARKED_JS__*/" not in html
    assert len(re.findall(r"</script>", html)) == 2          # inlined marked + the viewer
    assert "marked v" in html and 'class="markdown-body"' in html
    assert "<title>Temenos-Skills Help</title>" in html


def _sample(case, file, apps, inputs):
    return {"case": case, "template": "x/y", "data": {"file": file, "apps": apps, "userInputs": inputs}}


def test_sample_commands_show_generate_and_compile():
    from build_help import sample_commands
    template = {"inputs": [{"id": "APP", "kind": "app"}, {"id": "TEXT", "kind": "text"},
                           {"id": "PRODUCT", "kind": "text", "fixed": "EB"}]}
    cmds = sample_commands(_sample("s1", "V.X.b", ["CUSTOMER"], {"APP": "CUSTOMER", "TEXT": "IS MANDATORY", "PRODUCT": "EB"}), template)
    assert "t24skills sample s1\nt24skills template x/y" in cmds
    assert r"t24skills generate x/y --from-sample --release R25 --out .\work\s1" in cmds
    assert '  --set TEXT="IS MANDATORY" `' in cmds and "PRODUCT" not in cmds  # quoted; fixed inputs left out
    assert cmds.endswith(r"t24skills verify .\work\s1\V.X.b --app CUSTOMER --release R25")


def test_sample_commands_without_application():
    from build_help import sample_commands
    table = sample_commands(_sample("t", "T.b", [], {}), {"inputs": []})
    assert table.endswith(r"t24skills verify .\work\t\T.b --no-app --release R25")
    java = sample_commands(_sample("j", "J.java", [], {}), {"inputs": []})
    assert java.endswith(r"t24skills verify .\work\j\J.java --release R25")
