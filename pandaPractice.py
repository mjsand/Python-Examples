import pandas as pd
df = pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})
print(df['b'])
print(df[df['b'] < 23])