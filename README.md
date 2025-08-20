# FastAPI Hello API

このリポジトリは、FastAPIを使って作成した簡単な学習用APIです。

## ✅ 機能概要

- `/hello`: クエリパラメータで名前を受け取り、挨拶を返します。
  - 例: `/hello?name=Naoya` → `{"message": "Hello, Naoya!"}`
- `/greet`: JSON形式で名前と年齢を受け取り、挨拶を返します。
  - 例: `{"name": "Naoya", "age": 28}` → `{"message": "Hello, Naoya (28)!"}`

## 🔧 使用技術

- Python 3.10
- FastAPI
- Pydantic
- Uvicorn

## 🚀 実行方法（ローカル）

```bash
uvicorn main:app --reload
