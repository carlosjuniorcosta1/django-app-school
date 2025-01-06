# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:58:09 2024

@author: carlo
"""

import pandas as pd


df = pd.read_csv('questoes_enem.csv')

import re

cols = ['question_cod',  'question', 'all_alternatives', 'correct_alt', 'year' ]

df_portugues = pd.read_csv('questoesPortuguesCespe.csv', header=None, )

df_portugues.columns = cols

df_portugues['context'] = ''

df_portugues['wrong_correct'] = int

df_portugues['wrong_correct'] = df_portugues['all_alternatives'].apply(lambda x: len(re.findall(r'Errado\s|\sCerto|Certo\s|\sErrado', x)))

df_portugues_cespe = df_portugues.loc[df_portugues['wrong_correct'] > 0]
df_portugues_cespe['wrong_alternative'] = 'Errado'
df_portugues_cespe['correct_alternative'] = 'Certo'

df_answer_enem = pd.read_csv('df_answers.csv')



df_portugues_all = df_portugues.loc[df_portugues['wrong_correct'] == 0]


df_portugues_all['alt_a'] = df_portugues_all['all_alternatives'].apply(lambda x: ''.join(re.findall(r'a\)[^|]+', x)))
df_portugues_all['alt_b'] = df_portugues_all['all_alternatives'].apply(lambda x: ''.join(re.findall(r'b\)[^|]+', x)))
df_portugues_all['alt_c'] = df_portugues_all['all_alternatives'].apply(lambda x: ''.join(re.findall(r'c\)[^|]+', x)))
df_portugues_all['alt_d'] = df_portugues_all['all_alternatives'].apply(lambda x: ''.join(re.findall(r'd\)[^|]+', x)))
df_portugues_all['alt_e'] = df_portugues_all['all_alternatives'].apply(lambda x: ''.join(re.findall(r'e\)[^|]+', x)))

df_portugues_all['has_e'] = df_portugues_all['alt_e'].apply(lambda x: len(x))

df_portugues_all_has_e = df_portugues_all.loc[df_portugues_all['has_e'] > 0]


new_df = pd.DataFrame({
    "question_cod": df_portugues_all_has_e["question_cod"].repeat(5).reset_index(drop=True),
    "text": df_portugues_all_has_e.loc[:, ["alt_a", "alt_b", "alt_c", "alt_d", "alt_e"]].values.flatten(),
    "correct_alt": df_portugues_all_has_e["correct_alt"].repeat(5).reset_index(drop=True),
    "alternative": ['a', 'b', 'c', 'd', 'e'] * len(df_portugues_all_has_e)


})

new_df['is_correct'] = (new_df["correct_alt"] == new_df["alternative"]).astype(int)

start_value = 2303
num_questions = len(new_df) // 5  # Número de questões únicas
new_df["question_cod"] = [
    start_value + (i // 5) for i in range(len(new_df))
]

new_df.columns = ['question_id', 'text', 'correct_alt', 'alternative', 'is_correct']


df_portugues_all_has_e['question_cod']

df_portugues_all_has_e["question_cod"] = range(start_value, start_value + len(df_portugues_all_has_e))

df_portugues_all_has_e.columns = ['question_id', 'question', 'all_alternatives', 'correct_alt', 'year',
       'context', 'wrong_correct', 'alt_a', 'alt_b', 'alt_c', 'alt_d', 'alt_e',
       'has_e']

df_portugues_all_has_e['quiz_subject'] = 5

df_portugues_all_has_e['question_image'] = ''
df_portugues_all_has_e['context'] = ''
df_portugues_all_has_e['has_image'] = 0

df_portugues_all_has_e['number'] = 0
df_portugues_all_has_e['examining_board'] = 'cespe'

df_portugues_all_has_e['id'] = range(start_value, start_value + len(df_portugues_all_has_e))

"""['id', 'context', 'question', 'quiz_subject_id', 'question_image',
       'year', 'number', 'has_image']"""

"""df_portugues_all_has_e.columns = ['question_id', 'question', 'all_alternatives', 'correct_alt', 'year',
       'context', 'wrong_correct', 'alt_a', 'alt_b', 'alt_c', 'alt_d', 'alt_e',
       'has_e', 'quiz_subject', 'question_image', 'has_image', 'number',
       'examining_board', 'id']"""

df_portugues_all_has_e.columns =  ['question_id', 'question', 'all_alternatives', 'correct_alt', 'year',
       'context', 'wrong_correct', 'alt_a', 'alt_b', 'alt_c', 'alt_d', 'alt_e',
       'has_e', 'quiz_subject_id', 'question_image', 'has_image', 'number',
       'examining_board', 'id']

df_portugues_all_has_e = df_portugues_all_has_e[['id', 'context', 'question', 'quiz_subject_id', 'question_image', 'year', 
                        'number', 'has_image', 'examining_board']]
df['examining_board'] = 'enem'
df_portugues_all_has_e['examining_board'] = 'cespe'

df_questions = pd.concat([df, df_portugues_all_has_e])

df_questions = df_questions.dropna(subset=['question'])


df_questions.to_csv('df_questions_new.csv')


df_answer_enem.columns = ['Unnamed: 0', 'id', 'text', 'question_id', 'is_correct',
       'has_image_alt', 'alternative', 'answer_image']

new_df.columns = ['question_id', 'text', 'correct_alt', 'alternative', 'is_correct']

new_df['id'] = 0

new_df['has_image_alt'] = 0
new_df['answer_image'] = ''

new_df = new_df[['id', 'text', 'question_id', 'is_correct', 'has_image_alt', 'alternative', 
        'answer_image']]
      
df_answer_enem.drop('Unnamed: 0', axis = 1, inplace=True)

new_df['text'] = new_df['text'].apply(lambda x: x[2:].strip())

new_df.to_csv('df_answers_new.csv')

df_answers_new = pd.concat([df_answer_enem, new_df])

df_answers_new.to_csv('df_answers_new.csv')

df_portugues_cespe.to_csv('df_portugues_cespe.csv')



df_cespe = pd.read_csv('df_portugues_cespe.csv')
df_questions_enem = pd.read_csv('df_questions_new.csv')

df_answers_enem = pd.read_csv('df_answers_new.csv')


df_answers_cespe = df_cespe[['question_cod', 'correct_alt']]

df_answers_cespe = df_answers_cespe.loc[df_answers_cespe.index.repeat(2)].reset_index(drop=True)

df_answers_cespe['text'] = ['c', 'e'] * (len(df_answers_cespe) // 2)

df_answers_cespe['is_correct'] = (df_answers_cespe['text'] == df_answers_cespe['correct_alt']).astype(int)


start_value = 3172
num_questions = len(df_answers_cespe)
df_answers_cespe['question_cod'] = [
    start_value + (i // 2) for i in range(len(df_answers_cespe))
]


df_answers_cespe['text'] = df_answers_cespe['text'].map({'c': 'Certo', 'e': 'Errado'})

df_cespe['id'] = range(3172, 3172 + len(df_cespe))

"""df_questions_enem.columns 'Unnamed: 0', 'id', 'context', 'question', 'quiz_subject_id',
       'question_image', 'year', 'number', 'has_image', 'examining_board'"""

"""df_cespe.columns 'Unnamed: 0', 'question_cod', 'question', 'all_alternatives',
       'correct_alt', 'year', 'context', 'wrong_correct',
       'correct_alternative', 'wrong_alternative'"""


df_cespe['id'] = 0

df_cespe['context'] = ''
df_cespe['number'] = 0
df_cespe['question_image'] = ''
df_cespe['quiz_subject_id'] = 5
df_cespe['has_image'] = ''
df_cespe['examining_board'] = 'cespe'


df_cespe = df_cespe[['id', 'context', 'question', 'quiz_subject_id', 'question_image', 'year', 'number', 'has_image', 'examining_board']]
          

df_questions_enem.drop('Unnamed: 0', axis=1, inplace=True)

df_questions_new = pd.concat([df_questions_enem, df_cespe], ignore_index=True)

df_questions_new.to_csv('df_questions_new.csv')

"""df_answers_enem.columns 'Unnamed: 0', 'id', 'text', 'question_id', 'is_correct',
       'has_image_alt', 'alternative', 'answer_image'"""


"""df_answers_cespe.columns 'question_cod', 'correct_alt', 'text', 'is_correct'"""

df_answers_cespe['has_image_alt'] = ''
df_answers_cespe['alternative'] = ''
df_answers_cespe['answer_image'] = ''

df_answers_cespe.drop('alternative', axis=1, inplace=True)

df_answers_cespe.columns = ['question_id', 'alternative', 'text', 'is_correct', 'has_image_alt',
       'answer_image']

df_answers_enem.drop('Unnamed: 0', axis=1, inplace=True)

df_answers_enem.drop('id', axis=1, inplace=True)

df_answers_cespe = df_answers_cespe[['text', 'question_id', 'is_correct', 'has_image_alt', 'alternative', 'answer_image']]

df_answers_new = pd.concat([df_answers_enem, df_answers_cespe], ignore_index=True)

df_answers_new.to_csv('df_answers_new.csv')

df_questions_new.columns = ['question_id', 'context', 'question', 'quiz_subject_id', 'question_image',
       'year', 'number', 'has_image', 'examining_board']


df_answers_new['has_image_alt'].apply(lambda x: '0' if len(x) == 0 else 1)

df_answers_new['has_image_alt'] = df_answers_new['has_image_alt'].replace('', '0')

df_answers_new['has_image_alt'] = df_answers_new['has_image_alt'].astype('int')











