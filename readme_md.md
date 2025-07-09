# 📊 Streamlit データ可視化ダッシュボード

学習用のシンプルなStreamlitアプリケーションです。データ分析とWebアプリケーションデプロイの基本的な流れを体験できます。

## 🎯 学習目的

- Streamlitの基本的な使い方
- インタラクティブなデータ可視化
- Webアプリケーションのデプロイプロセス

## 📋 機能概要

### 主な機能
- **時系列データ可視化**: 日別売上推移と累積売上の表示
- **カテゴリ別分析**: 円グラフと棒グラフによる比較
- **地域別分析**: 散布図と棒グラフによる地域比較
- **インタラクティブフィルタ**: 日付範囲、カテゴリ、地域での絞り込み
- **リアルタイムメトリクス**: 総売上、平均売上などの指標表示

### 使用技術
- **Streamlit**: Webアプリケーションフレームワーク
- **Pandas**: データ操作・分析
- **Plotly**: インタラクティブグラフ作成
- **NumPy**: 数値計算

## 🚀 ローカル環境での実行

### 1. 環境準備
```bash
# リポジトリをクローン
git clone <your-repository-url>
cd streamlit-dashboard

# 仮想環境作成（推奨）
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate

# 依存関係をインストール
pip install -r requirements.txt
```

### 2. アプリケーション実行
```bash
streamlit run app.py
```

ブラウザで `http://localhost:8501` にアクセスしてアプリを確認できます。

## 🌐 デプロイ方法

### Streamlit Cloud でのデプロイ

1. **GitHubリポジトリ準備**
   - GitHub上にリポジトリを作成
   - `app.py`、`requirements.txt`、`README.md`をpush

2. **Streamlit Cloudでデプロイ**
   - [Streamlit Cloud](https://streamlit.io/cloud)にアクセス
   - GitHubアカウントでログイン
   - 「New app」→「Deploy a public app from GitHub」
   - リポジトリとブランチを選択
   - `app.py`をメインファイルとして指定
   - 「Deploy!」をクリック

### Herokuでのデプロイ

1. **追加ファイル作成**
   ```bash
   # setup.shの作成
   echo "mkdir -p ~/.streamlit/
   echo \"[server]
   headless = true
   port = \$PORT
   enableCORS = false
   \" > ~/.streamlit/config.toml" > setup.sh
   
   # Procfileの作成
   echo "web: sh setup.sh && streamlit run app.py" > Procfile
   ```

2. **Herokuデプロイ**
   ```bash
   # Heroku CLI インストール後
   heroku create your-app-name
   git push heroku main
   ```

### Railway/Renderでのデプロイ

- **Railway**: GitHubリポジトリ接続後、自動でStreamlitアプリを認識
- **Render**: Web Serviceとして作成、Build Command: `pip install -r requirements.txt`、Start Command: `streamlit run app.py --server.port $PORT`

## 📁 ファイル構成

```
streamlit-dashboard/
├── app.py              # メインアプリケーション
├── requirements.txt    # 依存関係
├── README.md          # プロジェクト説明
├── setup.sh           # Heroku用設定（必要に応じて）
└── Procfile           # Heroku用プロセス定義（必要に応じて）
```

## 🔧 カスタマイズポイント

### データソースの変更
```python
# app.py の generate_sample_data() 関数を修正
# CSVファイルやAPIからのデータ取得に変更可能
```

### 新しい可視化の追加
```python
# 新しいタブを追加
tab4 = st.tabs(["📈 時系列分析", "📊 カテゴリ別分析", "🗺️ 地域別分析", "🆕 新機能"])
```

### スタイルのカスタマイズ
```python
# CSSでのスタイル調整
st.markdown("""
<style>
.main-header {
    color: #1f77b4;
    font-size: 2rem;
}
</style>
""", unsafe_allow_html=True)
```

## 🎓 学習のポイント

1. **段階的な理解**: まずローカルで動作確認
2. **インタラクティブ機能**: サイドバーやタブの活用
3. **データフロー**: フィルタリング→可視化→表示の流れ
4. **デプロイ体験**: 複数のプラットフォームで試行
5. **エラーハンドリング**: 実際のデプロイで遭遇する問題の対処

## 📚 参考資料

- [Streamlit公式ドキュメント](https://docs.streamlit.io/)
- [Plotly公式ドキュメント](https://plotly.com/python/)
- [Pandas公式ドキュメント](https://pandas.pydata.org/)

---

**Note**: このプロジェクトは学習目的で作成されており、本番環境での使用には適切なセキュリティ対策とパフォーマンス最適化が必要です。