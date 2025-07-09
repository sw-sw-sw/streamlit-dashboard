import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# ページ設定
st.set_page_config(
    page_title="データ可視化ダッシュボード",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# タイトルとヘッダー
st.title("📊 データ可視化ダッシュボード")
st.markdown("---")

# サイドバー
st.sidebar.header("設定パネル")
st.sidebar.markdown("このアプリは学習用のサンプルです")

# データ生成関数
@st.cache_data
def generate_sample_data():
    """サンプルデータを生成"""
    np.random.seed(42)
    
    # 売上データ
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    sales_data = pd.DataFrame({
        'date': dates,
        'sales': np.random.normal(10000, 2000, len(dates)),
        'category': np.random.choice(['A', 'B', 'C'], len(dates)),
        'region': np.random.choice(['東京', '大阪', '名古屋'], len(dates))
    })
    
    # 累積売上計算
    sales_data['cumulative_sales'] = sales_data['sales'].cumsum()
    
    return sales_data

# メイン処理
def main():
    # データ読み込み
    with st.spinner('データを読み込み中...'):
        data = generate_sample_data()
    
    # サイドバーでフィルタリング
    st.sidebar.subheader("データフィルタ")
    
    # 日付範囲選択
    date_range = st.sidebar.date_input(
        "日付範囲を選択",
        value=(data['date'].min(), data['date'].max()),
        min_value=data['date'].min(),
        max_value=data['date'].max()
    )
    
    # カテゴリ選択
    categories = st.sidebar.multiselect(
        "カテゴリを選択",
        options=data['category'].unique(),
        default=data['category'].unique()
    )
    
    # 地域選択
    regions = st.sidebar.multiselect(
        "地域を選択",
        options=data['region'].unique(),
        default=data['region'].unique()
    )
    
    # データフィルタリング
    filtered_data = data[
        (data['date'] >= pd.Timestamp(date_range[0])) &
        (data['date'] <= pd.Timestamp(date_range[1])) &
        (data['category'].isin(categories)) &
        (data['region'].isin(regions))
    ]
    
    # メトリクス表示
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="総売上",
            value=f"¥{filtered_data['sales'].sum():,.0f}",
            delta=f"¥{filtered_data['sales'].sum() - data['sales'].mean() * len(filtered_data):,.0f}"
        )
    
    with col2:
        st.metric(
            label="平均売上",
            value=f"¥{filtered_data['sales'].mean():,.0f}",
            delta=f"¥{filtered_data['sales'].mean() - data['sales'].mean():,.0f}"
        )
    
    with col3:
        st.metric(
            label="データ期間",
            value=f"{len(filtered_data)}日",
            delta=f"{len(filtered_data) - len(data)}日"
        )
    
    with col4:
        st.metric(
            label="選択中の地域",
            value=len(regions),
            delta=f"{len(regions) - len(data['region'].unique())}"
        )
    
    st.markdown("---")
    
    # チャート表示
    tab1, tab2, tab3 = st.tabs(["📈 時系列分析", "📊 カテゴリ別分析", "🗺️ 地域別分析"])
    
    with tab1:
        st.subheader("売上推移")
        
        # 時系列チャート
        fig_timeseries = px.line(
            filtered_data,
            x='date',
            y='sales',
            title='日別売上推移',
            labels={'sales': '売上 (¥)', 'date': '日付'}
        )
        fig_timeseries.update_layout(height=400)
        st.plotly_chart(fig_timeseries, use_container_width=True)
        
        # 累積売上チャート
        fig_cumulative = px.line(
            filtered_data,
            x='date',
            y='cumulative_sales',
            title='累積売上推移',
            labels={'cumulative_sales': '累積売上 (¥)', 'date': '日付'}
        )
        fig_cumulative.update_layout(height=400)
        st.plotly_chart(fig_cumulative, use_container_width=True)
    
    with tab2:
        st.subheader("カテゴリ別分析")
        
        # カテゴリ別売上
        category_sales = filtered_data.groupby('category')['sales'].agg(['sum', 'mean', 'count']).reset_index()
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_pie = px.pie(
                category_sales,
                values='sum',
                names='category',
                title='カテゴリ別売上比率'
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            fig_bar = px.bar(
                category_sales,
                x='category',
                y='sum',
                title='カテゴリ別総売上',
                labels={'sum': '総売上 (¥)', 'category': 'カテゴリ'}
            )
            st.plotly_chart(fig_bar, use_container_width=True)
    
    with tab3:
        st.subheader("地域別分析")
        
        # 地域別売上
        region_sales = filtered_data.groupby('region')['sales'].agg(['sum', 'mean', 'count']).reset_index()
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_region_bar = px.bar(
                region_sales,
                x='region',
                y='sum',
                title='地域別総売上',
                labels={'sum': '総売上 (¥)', 'region': '地域'}
            )
            st.plotly_chart(fig_region_bar, use_container_width=True)
        
        with col2:
            fig_region_scatter = px.scatter(
                region_sales,
                x='count',
                y='sum',
                size='mean',
                hover_name='region',
                title='地域別売上分析（データ数 vs 総売上）',
                labels={'count': 'データ数', 'sum': '総売上 (¥)'}
            )
            st.plotly_chart(fig_region_scatter, use_container_width=True)
    
    # データテーブル表示
    st.markdown("---")
    st.subheader("📋 データテーブル")
    
    # 表示オプション
    show_raw_data = st.checkbox("生データを表示", value=False)
    
    if show_raw_data:
        st.dataframe(
            filtered_data.head(100),
            use_container_width=True,
            hide_index=True
        )
    
    # 統計情報
    st.subheader("📊 統計情報")
    st.dataframe(
        filtered_data[['sales']].describe(),
        use_container_width=True
    )

# アプリケーション実行
if __name__ == "__main__":
    main()