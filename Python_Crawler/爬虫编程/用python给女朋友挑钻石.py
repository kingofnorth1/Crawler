import seaborn as sns
import matplotlib.pyplot as plt

dia = sns.load_dataset("diamonds",data_home="seaborn-data", cache=True)

fig,ax = plt.subplots(figsize=(6.5,6.5))
sns.set_theme(style="whitegrid")
sns.despine(fig,left=True,bottom=True)
sns.scatterplot(data=dia,x="carat",y="price",style="cut",hue='cut',linewidth=0)
plt.show()