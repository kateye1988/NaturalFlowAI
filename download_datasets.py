import os
import urllib.request

# Create necessary directories
os.makedirs("data/raw", exist_ok=True)

# Dataset URLs (replace with direct links if available)
datasets = {
    "toefl11.zip": "https://example.com/toefl11.zip",
    "icnale.zip": "http://language.sakura.ne.jp/icnale/icnale.zip",
    "lang8.zip": "http://www.phontron.com/lang8/lang8.zip",
    "icle.zip": "https://www.uclouvain.be/en/research-institutes/ilc/icle.zip",
    "esl4.zip": "https://www.nist.gov/itl/iad/mig/esl-4-corpus.zip",
    "quora.csv": "https://www.kaggle.com/qcri/corpus/download/quora.csv"
}

# Download datasets
for filename, url in datasets.items():
    filepath = os.path.join("data/raw", filename)
    if not os.path.exists(filepath):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filepath)
        print(f"Saved to {filepath}")
    else:
        print(f"{filename} already exists. Skipping.")

print("All datasets downloaded successfully!")
