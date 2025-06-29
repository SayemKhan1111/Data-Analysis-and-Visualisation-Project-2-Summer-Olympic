# Step 1: Load & Explore the Data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
url = r"C:\Users\sayem\Downloads\archive (4)\summer.csv"
df = pd.read_csv(url)

# Basic Checks
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(f"Shape: {df.shape}")

# Step 2: Clean the Data
print(df.isnull().sum())  # Null check

# Clean text columns
df['Athlete'] = df['Athlete'].str.strip()
df['Sport'] = df['Sport'].str.strip()
df['Country'] = df['Country'].str.strip()

# Drop duplicates
df.drop_duplicates(inplace=True)

# Step 3: Basic Insights
print("Unique Sports:", df['Sport'].nunique())
print("Unique Countries:", df['Country'].nunique())
print("Olympic Years:", df['Year'].nunique())
print("Unique Athletes:", df['Athlete'].nunique())
print("Unique Medals:", df['Medal'].value_counts())
print("Gender Distribution:", df['Gender'].value_counts())

# Grouped Counts
print(df.groupby('Sport')['Medal'].count())
print(df.groupby('Country')['Medal'].count())

# Step 4: Visualizations

# 1 Line Chart – Total medals over the years
df.groupby('Year')['Medal'].count().plot(kind='line', marker='o', color='green')
plt.title("Total Medals Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Medals")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2️ Line Chart – USA medals over years
df[df['Country'] == 'USA'].groupby('Year')['Medal'].count().plot(kind='line', marker='o', color='blue')
plt.title("USA Medal Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Medals")
plt.grid(True)
plt.tight_layout()
plt.show()

# 3️ Line Chart – Male vs Female Participation
df.groupby(['Year', 'Gender'])['Athlete'].nunique().unstack().plot(kind='line', marker='o')
plt.title("Gender Participation Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Unique Athletes")
plt.legend(title="Gender")
plt.grid(True)
plt.tight_layout()
plt.show()

# 4️ Bar Charts – Top 10
fig, axs = plt.subplots(1, 3, figsize=(20, 6))

df.groupby('Country')['Medal'].count().sort_values(ascending=False).head(10).plot.bar(ax=axs[0], color='skyblue')
axs[0].set_title("Top 10 Countries")
axs[0].set_xlabel("Country")
axs[0].set_ylabel("Medals")

df.groupby('Sport')['Medal'].count().sort_values(ascending=False).head(10).plot.bar(ax=axs[1], color='orange')
axs[1].set_title("Top 10 Sports")
axs[1].set_xlabel("Sport")
axs[1].set_ylabel("Medals")

df.groupby('Athlete')['Medal'].count().sort_values(ascending=False).head(10).plot.bar(ax=axs[2], color='salmon')
axs[2].set_title("Top 10 Athletes")
axs[2].set_xlabel("Athlete")
axs[2].set_ylabel("Medals")

plt.tight_layout()
plt.show()

# 5️ Pie Charts – Medal & Gender Distribution
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

df['Medal'].value_counts().plot.pie(ax=axs[0], autopct='%1.1f%%', startangle=90)
axs[0].set_title("Medal Distribution")
axs[0].set_ylabel("")

df['Gender'].value_counts().plot.pie(ax=axs[1], autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightblue'])
axs[1].set_title("Gender Distribution")
axs[1].set_ylabel("")

plt.tight_layout()
plt.show()

# 6️ Heatmap – Correlation of Age, Height, Weight
if set(['Age', 'Height', 'Weight']).issubset(df.columns):
    sns.heatmap(df[['Age', 'Height', 'Weight']].corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation between Age, Height & Weight")
    plt.tight_layout()
    plt.show()
    
# 7️ Countplot – Gender-wise Sport Participation
plt.figure(figsize=(14, 6))
sns.countplot(data=df, x='Sport', hue='Gender')
plt.title("Sport Participation by Gender")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 8️ Stacked Bar – Medal Types for Top 5 Countries
top_5_countries = df['Country'].value_counts().head(5).index
df[df['Country'].isin(top_5_countries)].groupby(['Country', 'Medal']).size().unstack().plot(kind='bar', stacked=True)
plt.title("Medal Types for Top 5 Countries")
plt.ylabel("Medal Count")
plt.tight_layout()
plt.show()

# 9️ Boxplot – Age Distribution per Medal Type
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Medal', y='Age')
plt.title("Age Distribution by Medal Type")
plt.tight_layout()
plt.show()

# 10 Histogram – Age Distribution
plt.figure(figsize=(8, 6))
df['Age'].dropna().hist(bins=20)
plt.title("Age Distribution of Athletes")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 10 Violin Plot – Age vs Sport (Top 5 Sports)
top_5_sports = df['Sport'].value_counts().head(5).index
plt.figure(figsize=(10, 6))
sns.violinplot(data=df[df['Sport'].isin(top_5_sports)], x='Sport', y='Age')
plt.title("Age Distribution in Top 5 Sports")
plt.tight_layout()
plt.show()


