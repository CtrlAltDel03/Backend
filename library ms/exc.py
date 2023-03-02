import openpyxl
from pathlib import Path
import c1
w=Path('','data.xlsx')
wb=openpyxl.load_workbook(w)
sh=wb.active
b=[]
count=10
i=0

def populate():
    i=0
    for row in sh.iter_rows(max_row=3):
        j=0
        for cell in row:
            if(j==0):
                n=cell.value
            elif(j==1):
                p=cell.value
            else:
                q=cell.value
            j+=1
        i+=1
        bi=c1.Book(n,p,q)
        b.append(bi)
    return b

    

    

