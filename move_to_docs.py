import os
import shutil

root = r"d:\03-codeLearning\quant-trade-tutorial"
docs = os.path.join(root, "docs")

if not os.path.exists(docs):
    os.makedirs(docs)

targets = [
    "00_setup", "01_financial_concepts", "02_data", "03_indicators",
    "04_backtesting", "05_portfolio", "06_ml_trading", "07_fundamental",
    "08_futures", "09_hft", "10_math_methods", "datasets", "utils", "javascripts"
]

for t in targets:
    src = os.path.join(root, t)
    dst = os.path.join(docs, t)
    if os.path.exists(src):
        if os.path.exists(dst):
            print(f"Destination already exists: {dst}, skipping.")
            continue
        shutil.move(src, docs)
        print(f"Moved {t} to docs/")

readme = os.path.join(root, "README.md")
index = os.path.join(docs, "index.md")
if os.path.exists(readme):
    shutil.copy2(readme, index)
    print("Copied README.md to docs/index.md")
