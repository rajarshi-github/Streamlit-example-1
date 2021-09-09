
import streamlit as st
import pandas as pd
import numpy as np
import random

'''

# Streamlit allows markdown ... 

6 markdown levels in streamlit (Above was level 1)

## __Heading level 2__

To make it bold follow it with __("\_\_", double-underscore)__ before and after the text.

You can as well write it like \*\***double-underscore**\*\*

### Heading level 3

Just keep writing in a new paragraph

#### _Heading level 4_

To make it italics follow it with _("\_", single-underscore)_ before and after the text

You can as well write it like \**double-underscore*\*


##### Heading level 5

Yet another paragraph

###### ___Heading level 6___

To make it bold as well as italics follow it with ___("\_\_\_", triple-underscore)___ before and after the text

You can as well write it like \*\*\****double-underscore***\*\*\*


'''

st.title ('Python datatypes');

st.write('This is a text');

st.header ('Int');

x = 10
'x: ', x

st.header ('List');

list1 = [ random.randint(10,30) for i in range(10) ]
'list1:', list1

'''
## Dictionary
'''

dict1 = { 1: 'a',
          2: 'b',
          3: 'c',
          4: 'd'}
'dict1:', dict1

'''
### :one: Enumerate a dictionary [you already did it :ok::heavy_exclamation_mark:]
'''

for i, item in enumerate(dict1.items()):
    st.write(i , ':', item)

st.write('This is super cool :sunglasses: I :heart: it :heavy_exclamation_mark:');

with st.echo():
    st.write('This code will be printed')

'''
### :two: Write a fibonacci sequence function :sparkles::sparkles:
see below
'''
with st.echo():

    def fib(n):
        lis = [0,1]
        i = 2
        if n > 2:
            while i <= n:
                newitem = lis[-1] + lis[-2]
                lis.append(newitem)
                i += 1
        elif n == 1:
            return (lis[-2])
        return (lis[-1])

    st.write('Output:')
    
    i = 1
    while i < 10:
        st.write( 'fib(',i,'): ', fib(i) )
        i+=1


'''
### :three: Let's load a dataframe 
'''
url1 = 'https://github.com/rajarshi-github/Streamlit-example-1/blob/main/stoshops.csv'

st.text ('Dataset : ', url1)

df = pd.read_csv(url1)
with st.echo():
    st.write(df)
    st.write('Info: ', df.info())
    st.write('Shape: ' , df.shape)
    st.write(df.describe().transpose())
    


'''
### :four: Let's put an image :camera_with_flash: 
'''

from PIL import Image

image = Image.open('/Users/rpghosh/Desktop/python/car.png')
st.image(image)



'''
### :five: Let's put a map of :flag-au: :earth_asia:
'''
with st.echo():
    
    map_df = df[['Latitude','Longitude']]
    map_df.rename(columns = {'Latitude':'lat', 'Longitude':'lon'} , inplace = True)
    st.write(map_df)
    st.map(map_df, zoom = 5)



'''
### :six: Let's put a map of :flag-in: 
'''
url2 = 'https://github.com/rajarshi-github/Streamlit-example-1/blob/main/india.csv'
st.text ('Dataset : ', url2)
with st.echo():
    ind = pd.read_csv(url2)

    st.write(ind.head())
    map_ind = ind[['lat','lng']]
    map_ind.rename(columns = { 'lng':'lon'} , inplace = True)
    
    st.map(map_ind, zoom = 4)


