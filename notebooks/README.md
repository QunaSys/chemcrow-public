# Jupyter Notebook 環境セットアップ

## ブランチのクローン

```bash
git clone -b notebook_branch --single-branch --depth 1 git@github.com:QunaSys/chemcrow-public.git

```


## 環境構築手順

1. notebooksディレクトリに移動

```bash
cd  chemcrow-public/notebooks
```


2. Python仮想環境を作成

```bash
python -m venv .venv
```


3. 仮想環境を有効化

```bash

Linux/Macの場合
source .venv/bin/activate

Windowsの場合
.venv\Scripts\activate
```

4. 仮想環境に必要なライブラリをインストール

```bash
pip install -e ..
```

5. Jupyter Notebookを起動

```bash
jupyter notebook
```