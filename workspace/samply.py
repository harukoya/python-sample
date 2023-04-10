import pandas as pd

df = pd.read_csv("./sample.csv")

print(df)
print("-----")

def sample_method(row):
  comment = str(row['comment']).rjust(7, '0')
  master = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  ary = []
  for index, char in enumerate(comment):
    if char == '1':
      ary.append(master[index])
  row['comment'] = ','.join(ary)

  return row

df = df.apply(sample_method, axis=1)
print(df)
