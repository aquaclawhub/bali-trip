#!/usr/bin/env python3
"""
巴厘岛行程 HTML 构建脚本
用法: python3 build.py

依赖: pip install pyyaml jinja2
"""

import yaml
import jinja2
import re
import sys
import os
from pathlib import Path

# ── 路径 ──────────────────────────────────────────────
BASE = Path(__file__).parent
DATA_DIR = BASE / "data"
TEMPLATE_FILE = BASE / "templates" / "itinerary.html"
OUTPUT_FILE = BASE / "巴厘岛行程安排.html"

# ── 模板环境 ────────────────────────────────────────────
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(str(TEMPLATE_FILE.parent)),
    autoescape=False,
    keep_trailing_newline=True,
)
template = env.get_template(TEMPLATE_FILE.name)

# ── 加载数据 ────────────────────────────────────────────
def load_yaml(name: str) -> dict:
    path = DATA_DIR / f"{name}.yaml"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

meta     = load_yaml("meta")
flights  = load_yaml("flights")
days_raw = load_yaml("days")       # {"days": [...]}
days     = days_raw["days"]        # 取列表
spa_list = load_yaml("spa-list")

# ── 渲染并写文件 ────────────────────────────────────────
output = template.render(
    meta=meta,
    flights=flights,
    days=days,
    spa_list=spa_list,
)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(output)

print(f"✅ 生成: {OUTPUT_FILE}")
