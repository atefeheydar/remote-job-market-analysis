import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("top_skills.csv").head(10)

plt.figure()
plt.bar(df["skill"], df["count"])
plt.xticks(rotation=45)
plt.title("Top 10 In-Demand Skills (Remote Jobs)")
plt.tight_layout()
plt.show()
