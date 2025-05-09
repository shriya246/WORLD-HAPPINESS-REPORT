import pandas as pd
import plotly.express as px
import preswald

df = pd.read_csv("sample1.csv")
Filter_df = df.sort_values(by="Score", ascending=False).head(20)
fig = px.bar(
    Filter_df,
    x="Country or region",
    y="Score",
    color="Score",
    title="Top 20 Happiest Countries (2019)",
    labels={"Score": "Happiness Score", "Country or region": "Country"},
)

fig.update_layout(xaxis_tickangle=-45, template="plotly_white")
preswald.text("2019_World's_HappinessReport")
preswald.text("The top 20 happier nations according to the 2019 World Happiness Report are displayed in this animated graphic.")

top_country = Filter_df.iloc[0]
preswald.text(f"*Happier_Country:* {top_country['Country or region']} with a score of {top_country['Score']}")

preswald.plotly(fig)
preswald.table(Filter_df, title="Top 20 Happiest Countries (2019)")
