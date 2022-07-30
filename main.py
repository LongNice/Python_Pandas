from gettext import install

import pip
import pandas as pd

excel = pd.read_excel("MemoryTable.xlsx");

print(excel);
print("==========================");
for ind in range(len(excel.index)):
    print(excel.iloc[ind]["Memory Type"]);
