import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("winequality-white.csv", sep=";")

df_features = df.drop(columns='quality')
'''
plt.figure(figsize=(14,5))
plt.subplot(1,2,1)
ax = sns.kdeplot(df_features['alcohol'],shade=True,color='#d1aa00')
plt.ylabel('alcohol')
plt.xlabel('% distribution per category')
plt.subplot(1,2,2)
df_features['alcohol'].plot.box()
plt.tight_layout()
plt.show()

num_columns = df_features.columns.tolist()

result_df = pd.DataFrame(data=[df[num_columns].skew(),df[num_columns].kurtosis()],index=['skewness','kurtosis'])
pd.set_option('display.max_columns', None)
print(result_df)
'''


'''
plt.figure(figsize=(18,40))
for i,col in enumerate(num_columns,1): # 1 = optional starting number
     plt.subplot(8,4,i)
     sns.kdeplot(df[col],color='#d1aa00',fill=True)
     plt.subplot(8,4,i+11)
     df[col].plot.box()
plt.tight_layout()
plt.show()


plt.figure(figsize=(16,6))
sns.violinplot(data=df, x='quality', y='sulphates')
plt.show()


plt.figure(figsize=(16,6))
sns.swarmplot(x="quality", y="total sulfur dioxide", data=df)
plt.show()

quality_cat = df.quality.unique()
quality_cat.sort()
qual_TSD = []
for i,quality in enumerate(quality_cat):
  qual_TSD.append([quality, df['total sulfur dioxide'].loc[df['quality'] == quality].mean()])

df_qual_TSD = pd.DataFrame(qual_TSD, columns =['Quality', 'Mean TSD'])

plt.figure(figsize=(10,5))
sns.barplot(x="Quality", y="Mean TSD", data=df_qual_TSD)
plt.show()
'''
def alcohol_cat(alcohol):
    if alcohol <= 9.5:
        return "Low"
    elif alcohol <= 11:
        return "Moderate"
    elif alcohol <= 12.5:
        return "High"
    else:
        return "Very High"
 
df['alcohol_category'] = df['alcohol'].apply(alcohol_cat)
# print(df.sample(frac=1).head())

# import numpy as np το βάζουμε πάνω - πάνω
 
plt.figure(figsize=(15,30))
 
cross = pd.crosstab(index=df['quality'],columns=df['alcohol_category'],normalize='index')
cross.plot.barh(stacked=True,rot=40,cmap='crest_r').legend(bbox_to_anchor=(1.0, 1.0))
plt.xlabel('% distribution per category')
plt.xticks(np.arange(0,1.1,0.1))
plt.title("Wine Quality each {}".format('alcohol_category'))
plt.show()

