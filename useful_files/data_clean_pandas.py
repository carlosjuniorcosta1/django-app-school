# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:58:09 2024

@author: carlo
"""

import pandas as pd 


df = pd.read_csv('respostas_enem.csv')


df.loc[df['has_image_alt'] == 1, 'answer_image'] = df['text']

df.loc[df['has_image_alt'] == 1, 'text' ] = ''


df.to_csv('df_answers.csv')


