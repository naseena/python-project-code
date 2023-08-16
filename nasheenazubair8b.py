# -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:31:17 2023

@author: hp
"""
 

vegfood=pandas.read_excel(r"C:\Users\\hp\Documents\Trainee\nasheenazubair\nashhu_friends.xlsx",sheet_name='vegfood')

vegfood
nonveg=pandas.read_excel(r"C:\Users\\hp\Documents\Trainee\nasheenazubair\nashhu_friends.xlsx",sheet_name='nonveg')
nonveg
months=pandas.read_excel(r"C:\Users\\hp\Documents\Trainee\nasheenazubair\nasheena_excel.xlsx")

months


colours=pandas.read_excel(r"C:\Users\\hp\Documents\Trainee\nasheenazubair\nasheena_excel.xlsx",sheet_name='clrnames')

colours
import pandas as pd
from pandas import read_csv,read_excel

friends=pd.read_csv(r"C:\Users\hp\Documents\Trainee\nasheenazubair\friendsname.txt",sep=",")
friends

family=pd.read_csv(r"C:\Users\hp\Documents\Trainee\nasheenazubair\familymembers.txt",sep="*")
family

vegfood=pd.read_csv(r"C:\Users\hp\Documents\Trainee\nasheenazubair\vegfooditems.txt",sep="|")
vegfood
nonvegfood=pd.read_csv(r"C:\Users\hp\Documents\Trainee\nasheenazubair\nonvegitems.txt",sep="|")
nonvegfood

months=pd.read_csv(r"C:\Users\hp\Documents\Trainee\nasheenazubair\monthsname.txt",sep="&")
months

colours=pd.read_csv(r"C:\Users\hp\Documents\Trainee\nasheenazubair\coloursname.txt",sep="^")
colours

df=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\nashhuxl2\assign9practise.xlsx",sheet_name="Sheet3")
df

df.columns
df.index
row=df.shape[1]

df.info()
df.head(5)
df.tail(5)
df.dtypes
type(df)
col=df.shape[1]
lst=list(df.columns)
lst
lst1=lst[2:]
lst1=lst[1:]

for p in lst:
    print(p)
lst1=lst[0]
lst1
df.quality.unique()
df[start:end,start:end]
df.shape
df[star:end]

df_new=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\nashhuxl2\assign9practise.xlsx",sheet_name="Sheet1")
df_new

df_new.head(4)
df_new.tail(5)
df_new.shape
df_new.info()
df_new.dtypes
type(df_new)
df_new.index
lst=list(df_new.columns)
lst
for p in lst:
    print(p)
lst1=lst[2]
lst1
lst1=lst[0:]
lst1
df_new[0:4]
df_new.iloc[0:3,0:4]

import pandas as pd
from pandas import read_csv,read_excel
seasons=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\nashhuxl2\assign9practise.xlsx",sheet_name="Sheet2")


seasons

seasons.columns
seasons.shape
seasons.head(5)
seasons.tail(5)
seasons.dtypes
type(seasons)
seasons.info
seasons.index
seasons[0:4]
seasons.iloc[0:4,0:2]








df=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment10\practise assign10.xlsx")
df
df_dep_fil=df[df['quality']=='intelligent']

df_dep_fil.quality.unique()



fd
fd.name.unique()
fd['quality'].unique()
df=fd[['name','quality']]
fd.index
fd.columns
df=fd.name
df
df_new=fd.quality

fd['name'][4]

fd.iloc[0:10,0:2]

fd.columns

df.quality.unique()
df_fil=df[df['name']=='fatima']

df_fil.name.unique()
df_nw=df[df['name']!='sabhiya']

df_nw

df_and=df[(df['name']=='fazeela') & (df['quality']=='writer')]

df_and['name'].unique()
df_and['quality'].unique()
df_nw1=df[df['quality']!='intelligent']

df_nw1.quality.unique()

df_filter=df[['name','quality']]

df_filter['quality'][1]
df_filter['name'][1]

df_filter1=[df(['name'][1]),df(['quality'][1])

df.columns

df_or=df[(df['name']=='muskaan') | (df['quality']=='anger')]

df_or
df_or.name.unique()

df_or.quality.unique()


df.name.unique()
df.quality.unique()

df_clr=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment10\practise assign10.xlsx",sheet_name='Sheet2')
df_clr


df_clr.hindi.unique()
df_clr.telugu.unique()

df_clr.quality.unique()

df
df.quality.unique()

df_fil=df[df['quality']=='funny']

df_fil


df_fil1=df[df['quality']=='intelligent']

df_fil1


df_family=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment10\practise assign10.xlsx",sheet_name='Sheet3')


df_family

df1=df_family[(df_family['relation']=='brother') & (df_family['relation']=='sister')]

df1['relation'].unique()

df_or=df_family[(df_family['relation']=='brother') | (df_family['relation']=='parents')]

df_or['relation'].unique()

df1

df2=df_family[df_family['relation']=='parents']

df2

df_not=df_family[df_family['relation']!='parents']

df_not.relation.unique()
lst=["brother","sister"]

lst

df_family[(df_family.relation.isin(lst))]

lst1=["brother"]

df_family[(~df_family.relation.isin(lst1))]

import pandas as pd

Q5> create a dataframe which contains either your brothers list or parents list.
Q5> create a dataframe which contains your brothers list and parents list.


df_family[(df_family.relation=="brother")|(df_family.relation=="parents")]

lst2=["brother","parents"]

df_d=df_family[(df_family.relation.isin(lst2))]


df_d
import pandas as pd
veg_food=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment10\vegfood.xlsx")
veg_food

# Q1>create a dataframe which are  soups items
# Q2>create a dataframe which are curry items
# Q3>create a dataframe which are fry items
# Q4>create a dataframe which contains soups and fry items
# Q5>create a dataframe which not contains soups and fry items
# Q6>create a dataframe which contains either soup or fry items


veg_food
lst3=["soup","fry"]

veg_fil=veg_food[veg_food.items.lst3)]


veg_fil=veg_food[veg_food['items']=='soup']

veg_fil


veg_fry=veg_food[veg_food['items'].isin(lst3)]

veg_fry


veg_curry=veg_food[veg_food['items']=='curry']

veg_curry
lst=["soup","fry"]

veg_food[veg_food['items'].isin(["soup","fry"])]

veg_nt=veg_food[~(veg_food['items'].isin(lst3))]

veg_nt


veg_food[(veg_food["items"]=="soup") | (veg_food["items"]=="fry")]

import pandas as pd
non_veg=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment10\nonveg.xlsx")


non_veg
4. Create a NonVegfood_items.xlsx file  (atleast 10 names, columns are NonVegFoodName*Taste)
Q1>create a dataframe which contains only chicken items
Q2>create a dataframe which contains only mutton items
Q3>create a dataframe which contains only Fry items
Q4>create a dataframe which contains only Fry and chicken items
Q5>create a dataframe which not contains Fry and chicken items
Q6>create a dataframe which contains either Fry or mutton items


non_veg[non_veg['nonveg']=='chicken']

non_veg[non_veg['nonveg']=='mutton']



non_veg[non_veg['items']=='fry']


nonveg_and=non_veg[[(non_veg['items']=='mandi')] and [(non_veg['nonveg']=='chicken')]]




nonveg_d=non_veg[(non_veg['nonveg']=='chicken')]



nonveg_d


nonveg_and

lst=['fry']
lst1=['chicken']
non_veg[~(non_veg['items'].isin(lst)) & ~(non_veg['nonveg'].isin(lst1))]


nonveg_or=non_veg[(non_veg['items']=='fry') | (non_veg['nonveg']=='chicken')]


nonveg_or

veg_nt=veg_food[~(veg_food['items'].isin(lst3))]


nonveg_and=non_veg[(non_veg['items']=='fry') & (non_veg['nonveg']=='chicken')]


lst2=['fry']
lst3=['mutton']

non_veg[(non_veg['items'].isin(lst2)) | (non_veg['nonveg'].isin(lst3))]



# 5. Create a month_names.xlsx file (atleast 12 names, columns are MonthName*Season)
# Q1>create a dataframe which contains only winter season months
# Q2>create a dataframe which contains only summer season months
# Q3>create a dataframe which contains only rainy season months
# Q4>create a dataframe which contains only winter and summer season months
# Q5>create a dataframe which not contains summer and rainy season months
# Q6>create a dataframe which contains either winter or rainy items

import pandas as pd
months_df = pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment10\months.xlsx")

months_df


months_df[months_df['seasons']=='summer']

months_df[months_df['seasons']=='raining']

months_df[months_df['seasons']=='winter']

lst=["raining","summer"]

months_df[~months_df['seasons'].isin(lst)]

months_df[(months_df['seasons']=='winter') | (months_df['seasons']=='raining')]


lst1=["winter","summer"]

months_df[months_df['seasons'].isin(lst1)]

import pandas as pd
flwrs=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment10\colours.xlsx",sheet_name='Sheet2')

flwrs

#Q1>create a dataframe which contains only red colour flower list
#Q2>create a dataframe which contains only white colour flower list
#Q3>create a dataframe which contains only pink colour flower list
#Q4>create a dataframe which contains only red and pink colour list
#Q5>create a dataframe which not contains red and white colour list
#Q6>create a dataframe which contains either red or pink colour list


flwrs[flwrs['clr names']=='red']

flwrs[flwrs['clr names']=='white']


flwrs[flwrs['clr names']=='pink']

lst=['red','pink']

flwrs[flwrs['clr names'].isin(lst)]

lst1=["red","white"]


flwrs[~flwrs['clr names'].isin(lst1)]


lst2=['red','pink']

flwrs[(flwrs['clr names'].isin(lst2)) | (flwrs['clr names'].isin(lst2))]


flwrs[(flwrs['clr names']=='red')|(flwrs['clr names']=='pink')]


flwrs.loc[3:8,'english']

flwrs.loc[[1,5],['hindi','telugu']]

flwrs.query('english =="pink rose"  | hindi =="laal gulaabi" ')


import pandas as pd

bf=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\friends b&g.xlsx")

bf

gf=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\friends b&g.xlsx",sheet_name="Sheet2")

gf


bf1=pd.DataFrame(bf)

bf1

df_append=pd.concat([bf,gf],axis=1)

df_append


fs=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\f&m.xlsx")

fs

ms=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\f&m.xlsx",sheet_name="Sheet2")

ms


df_append=pd.concat([fs,ms],axis=0,ignore_index='true')
df_append


bro_lst=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\s&b.xlsx",sheet_name="Sheet2")

bro_lst
sis_lst=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\s&b.xlsx")

sis_lst

df_append=pd.concat([bro_lst,sis_lst],axis=1)
df_append


df_append=pd.concat([bro_lst,sis_lst],axis=1,ignore_index="true")
df_append
import pandas as pd
 ws=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\seasons.xlsx")

ss=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\seasons.xlsx",sheet_name="Sheet2")
ws
ss

rs=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\seasons.xlsx",sheet_name="Sheet3")

rs

df_append=pd.concat([ws,ss,rs],axis=0,ignore_index="true")

df_append

df_append=pd.concat([ws,ss,rs],axis=1)
df_append

import pandas as pd

fc=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\flowers.xlsx")

fc
fc1=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\flowers.xlsx",sheet_name="Sheet2")


fc1
fc2=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\flowers.xlsx",sheet_name="Sheet3")

fc2
fc3=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\flowers.xlsx",sheet_name="Sheet4")

fc3
df_append=pd.concat([fc,fc1,fc2,fc3],axis=0,ignore_index='true')
df_append

df_append=pd.concat([fc,fc1,fc2,fc3],axis=1)
df_append

chk=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\nonvegitem.xlsx")
chk
mtn=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\nonvegitem.xlsx",sheet_name="Sheet2")
mtn

df_append=pd.concat([chk,mtn],axis=0,ignore_index='true')
df_append

df_append=pd.concat([chk,mtn],axis=1)
df_append

soups=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\soup&fry.xlsx")

soups

fry=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\soup&fry.xlsx",sheet_name='Sheet2')

fry

df_append=pd.concat([soups,fry],axis=0,ignore_index="true")

df_append

df_append=pd.concat([soups,fry],axis=1)
df_append

dal=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\dal&veg.xlsx")
dal
veg=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment11\dal&veg.xlsx",sheet_name="Sheet2")

veg
df_append=pd.concat([dal,veg],axis=0,ignore_index="true")
df_append


df_append=pd.concat([soups,fry],axis=1)

df_append

import pandas as pd

schlmates=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\friends merge.xlsx ")

schlmates

clgmates=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\friends merge.xlsx ",sheet_name='Sheet2')

clgmates

df_merge=clgmates.merge(schlmates,how='inner',on='friendname')

df_merge=clgmates.merge(schlmates,how='left',on='friendname')

df_merge


clgmates.merge(schlmates,how='right',on='friendname')


df_merge=clgmates.merge(schlmates,how='outer',on='friendname')
df_merge


df_f=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\family merge.xlsx ")

df_f

df_m=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\family merge.xlsx ",sheet_name="Sheet2")

df_m


df_merge=df_f.merge(df_m,how='inner',on='relation')
df_merge

df_f.merge(df_m,how='left',on='relation')

df_f.merge(df_m,how='right',on='relation')


df_f.merge(df_m,how='outer',on='relation')

dal=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\vegitems.xlsx ")
dal

veg=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\vegitems.xlsx ",sheet_name='Sheet2')
veg

veg.merge(dal,how='inner',on='taste')

veg.merge(dal,how='left',on='taste')

veg.merge(dal,how='right',on='taste')

veg.merge(dal,how='outer',on='taste')

df_s=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\soups ,fry.xlsx ")
df_s



df_f=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\soups ,fry.xlsx ",sheet_name='Sheet2')
df_f

df_s.merge(df_f,how='inner',on='taste')

df_s.merge(df_f,how='left',on='taste')

df_s.merge(df_f,how='right',on='taste')

df_s.merge(df_f,how='outer',on='taste')

df_c=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\nonveg.xlsx")
df_c

df_m=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\nonveg.xlsx",sheet_name='Sheet2')
df_m

df_m.merge(df_c,how='inner',on='taste')

df_m.merge(df_c,how='left',on='taste')

df_m.merge(df_c,how='right',on='taste')

df_m.merge(df_c,how='outer',on='taste')

#4. Do inner Merge all dataframes and print friend names. (key=season)
#5. Do left Merge all dataframes and print friend names.(key=season)
#6. Do right Merge all dataframes and print friend names.(key=season)
#7. Do outer Merge all dataframes and print friend names.(key=season)
import pandas as pd

dfw=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\seasons.xlsx")
dfw
dfs=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\seasons.xlsx",sheet_name='Sheet2')
dfs

dfr=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\seasons.xlsx",sheet_name='Sheet3')
dfr


dfs,dfr.merge(dfr,how='left',on='seasons')

dfs,dfr.merge(dfr,how='inner',on='seasons')

dfs,dfr.merge(dfr,how='right',on='seasons')

dfs,dfr.merge(dfr,how='outer',on='seasons')

import pandas as pd

dfw.merge(dfs,how='inner',on='seasons').merge(dfr,how='inner',on='seasons')


dfw.merge(dfs,how='left',on='seasons').merge(dfr,how='left',on='seasons')

dfw.merge(dfs,how='outer',on='seasons').merge(dfr,how='outer',on='seasons')

dfw.merge(dfs,how='right',on='seasons').merge(dfr,how='right',on='seasons')

#5. Do inner Merge all dataframes and print friend names. (key=color)
#6. Do left Merge all dataframes and print friend names.(key=color)
#7. Do right Merge all dataframes and print friend names.(key=color)
#8. Do outer Merge all dataframes and print friend names.(key=color)
import pandas as pd
dfr=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\flowers.xlsx ")

dfr

dfy=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\flowers.xlsx ",sheet_name='Sheet2')

dfy

dfp=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\flowers.xlsx",sheet_name='Sheet3')

dfp

dfw=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment12\flowers.xlsx",sheet_name='Sheet4')
dfw


dfr.merge(dfy,how='inner',on='colours').merge(dfp,how='inner',on='colours').merge(dfw,how='inner',on='colours')

dfr.merge(dfy,how='left',on='colours').merge(dfp,how='left',on='colours').merge(dfw,how='left',on='colours')

dfr.merge(dfy,how='right',on='colours').merge(dfp,how='right',on='colours').merge(dfw,how='right',on='colours')

dfr.merge(dfy,how='outer',on='colours').merge(dfp,how='outer',on='colours').merge(dfw,how='outer',on='colours')


pd.merge(pd.merge(dfr,dfy,dfp,on='colours'),dfw,on='colours')

import pandas as pd
df=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment13 practise\friends sum.xlsx",sheet_name='Sheet1')

df
df1=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment13 practise\friends sum.xlsx",sheet_name='Sheet3')
df1
df.groupby('quality')['friendsname'].count()

df,df1.groupby('quality').count()

df.groupby('friendsname').sum()

df2=df.merge(df1,how='inner',on='quality')

df2.groupby('quality').count()

df2.columns
df.columns

df1.columns
df2=pd.concat([df,df1],axis=0,ignore_index='true')

df2.groupby('quality')['no.of.friends'].sum()

df2.groupby('friendsname')['quality'].sum()
df2.columns

df2.columns

df2.groupby('quality')['friendsname','no.of.friends'].sum()
df2.groupby(['quality','friendsname'])['no.of.friends'].sum()

df2.groupby('quality').agg({'no.of.friends':[sum]})
df2.groupby('quality')['no.of.friends'].sum()

pd.pivot_table(df2,values='no.of.friends',index='friendsname',columns='quality',aggfunc='sum')

pd.pivot_table(df2,values='no.of.friends',columns='quality',aggfunc='sum')


import pandas as pd
df1=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment13 practise\friends sum.xlsx",sheet_name='Sheet3')

df1.groupby('quality')['friendsname'].count()


df=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment13 practise\seasons.xlsx")

df

df.groupby('seasons')['months'].count()


df1=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment13 practise\seasons.xlsx",sheet_name='Sheet2')

df1

df1.groupby('seasons')['months'].count()

df2=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment13 practise\seasons.xlsx",sheet_name='Sheet3')
df2

df2.groupby('seasons')['months'].count()

df=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment13 practise\colours sum.xlsx")

df

df.groupby('colours')['flowers'].count()

df1=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment13 practise\colours sum.xlsx",sheet_name='Sheet2')

df1

df1.groupby('colours')['flowers'].count()

df2=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment13 practise\colours sum.xlsx",sheet_name='Sheet3')

df2

df2.groupby('colours')['flowers'].count()

df3=pd.read_excel(r"C:\Users\hp\Documents\Trainee\nasheenazubair\assignment13 practise\colours sum.xlsx",sheet_name='Sheet4')

df3
df3.groupby('colours')['flowers'].count()















