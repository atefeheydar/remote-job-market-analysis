import pandas as pd

# Load data
df = pd.read_csv("remoteok_jobs.csv")

print("Total jobs:", len(df))

# Clean tags
df["tags"] = df["tags"].fillna("")
all_tags = df["tags"].str.lower().str.split(", ")

# Count skills
skill_counts = {}

for tags in all_tags:
    for tag in tags:
        if tag:
            skill_counts[tag] = skill_counts.get(tag, 0) + 1

skills_df = pd.DataFrame(
    skill_counts.items(),
    columns=["skill", "count"]
).sort_values(by="count", ascending=False)

skills_df.to_csv("top_skills.csv", index=False)

print("Top skills saved to top_skills.csv")
