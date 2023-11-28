#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


data= pd.read_csv('strange.csv',on_bad_lines='skip')


# In[11]:


data


# In[13]:


walkie_talkie = ['datetime', 'city', 'comments', 'date posted', 'latitude', 'longitude']
data.drop(walkie_talkie, axis = 1, inplace = True)


# In[14]:


data


# In[37]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_ufo_histogram_by_country(dataframe):

    required_columns = ['datetime', 'city', 'comments', 'date posted', 'latitude', 'longitude', 'country']
    if not set(required_columns).issubset(dataframe.columns):
        raise ValueError("DataFrame должен содержать столбцы: datetime, city, comments, date posted, latitude, longitude, country")


    dataframe['datetime'] = pd.to_datetime(dataframe['datetime'], errors='coerce')
    dataframe['date posted'] = pd.to_datetime(dataframe['date posted'], errors='coerce')


    unique_countries = dataframe['country'].unique()
    colors = plt.cm.viridis(np.linspace(0, 1, len(unique_countries)))

    plt.figure(figsize=(12, 6))

    for i, country in enumerate(unique_countries):
        country_data = dataframe[dataframe['country'] == country]
        plt.hist(country_data['datetime'], bins=20, color=colors[i], alpha=0.7, label=country)


    plt.title('Гистограмма наблюдений за НЛО по странам')
    plt.xlabel('Дата и время наблюдения')
    plt.ylabel('Частота наблюдений')
    plt.legend(title='Страна')

    plt.show()


data = {'datetime': ['10/10/1949 20:30','10/10/1949 21:00', '10/10/1956 21:00', '10/10/1960 20:00', '10/10/1965 21:00', '9/9/2013 22:00'],
        'city': ['san marcos', 'lackland afb', 'edna', 'kaneohe', 'penarth (uk/wales)', 'kalispell'],
        'comments': ['This event took place in early fall around 1949', '1949 Lackland AFB&#44 TX. Lights racing acros', 'My older brother and twin sister were leaving', 'AS a Marine 1st Lt. flying an FJ4B fighter/att', 'penarth uk circle 3mins stayed 30ft above m', 'I was letting my dogs our for the night when I'],
        'date posted': ['4/27/2004', '1/21/2008', '1/17/2004', '4/27/2007', '2/14/2006', '9/30/2013'],
        'latitude': ['29.8830556', '53.2', '28.9783333', '36.5950000', '51.434722', '48.195833'],
        'longitude': ['-97.941111', '-2.916667', '-96.645833', '-82.188889', '-3.180000', '-114.311944'],
        'country': ['us', 'NaN', 'us', 'us', 'gb', 'us']
}

df = pd.DataFrame(data)
plot_ufo_histogram_by_country(df)


# In[42]:


import pandas as pd
import matplotlib.pyplot as plt

def plot_ufo_frequency_by_month(dataframe):

    required_columns = ['datetime', 'city', 'comments', 'date posted', 'latitude', 'longitude', 'country']
    if not set(required_columns).issubset(dataframe.columns):
        raise ValueError("DataFrame должен содержать столбцы: datetime, city, comments, date posted, latitude, longitude, country")

    dataframe['datetime'] = pd.to_datetime(dataframe['datetime'], errors='coerce')

    plt.figure(figsize=(12, 6))
    dataframe['month'] = dataframe['datetime'].dt.month
    dataframe['month'].value_counts().sort_index().plot(kind='bar', color='skyblue', alpha=0.7)

    plt.title('Частота появления объектов НЛО по месяцам')
    plt.xlabel('Месяц')
    plt.ylabel('Частота')
    plt.xticks(rotation=0)

    plt.show()
data = {'datetime': ['10/10/1949 20:30','10/10/1949 21:00', '10/10/1956 21:00', '10/10/1960 20:00', '10/10/1965 21:00', '9/9/2013 22:00'],
        'city': ['san marcos', 'lackland afb', 'edna', 'kaneohe', 'penarth (uk/wales)', 'kalispell'],
        'comments': ['This event took place in early fall around 1949', '1949 Lackland AFB&#44 TX. Lights racing acros', 'My older brother and twin sister were leaving', 'AS a Marine 1st Lt. flying an FJ4B fighter/att', 'penarth uk circle 3mins stayed 30ft above m', 'I was letting my dogs our for the night when I'],
        'date posted': ['4/27/2004', '1/21/2008', '1/17/2004', '4/27/2007', '2/14/2006', '9/30/2013'],
        'latitude': ['29.8830556', '53.2', '28.9783333', '36.5950000', '51.434722', '48.195833'],
        'longitude': ['-97.941111', '-2.916667', '-96.645833', '-82.188889', '-3.180000', '-114.311944'],
        'country': ['us', 'NaN', 'us', 'us', 'gb', 'us']
}
df = pd.DataFrame(data)
plot_ufo_frequency_by_month(df)


# In[46]:


import pandas as pd
import matplotlib.pyplot as plt

def plot_ufo_shapes_with_details(dataframe):

    required_columns = ['datetime', 'city', 'comments', 'date posted', 'latitude', 'longitude', 'Shape']
    if not set(required_columns).issubset(dataframe.columns):
        raise ValueError("DataFrame должен содержать столбцы: datetime, city, comments, date posted, latitude, longitude, Shape")

    plt.figure(figsize=(12, 6))

    unique_shapes = dataframe['Shape'].unique()

    for i, shape in enumerate(unique_shapes):
        shape_data = dataframe[dataframe['Shape'] == shape]
        plt.scatter(shape_data['datetime'], shape_data['longitude'], label=shape, alpha=0.7)

    plt.title('Частота различных форм объектов НЛО с полным графиком')
    plt.xlabel('Дата и время наблюдения')
    plt.ylabel('Долгота')
    plt.legend(title='Форма объекта НЛО')
    plt.show()

data = {'datetime': ['2023-01-01 10:00', '2023-02-01 15:30', '2023-03-01 20:45', '2023-03-02 22:30'],
        'city': ['CityA', 'CityB', 'CityC', 'CityD'],
        'comments': ['CommentA', 'CommentB', 'CommentC', 'CommentD'],
        'date posted': ['2023-01-02', '2023-02-02', '2023-03-02', '2023-03-03'],
        'latitude': [40.7128, 45.4215, 25.7617, 35.6895],
        'longitude': [-74.0060, -75.6919, -80.1918, 139.6917],
        'Shape': ['Triangle', 'Circle', 'Triangle', 'Square']
}

df = pd.DataFrame(data)
plot_ufo_shapes_with_details(df)


# In[ ]:




