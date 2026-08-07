Sudoku = []
Rows=0
Columns=0
Box_size=0

def input_sudoku(Sudoku,Rows,Columns):
    
    Rows= int(input('Enter Rows '))
    Columns= int(input('Enter Columns'))
    
    
    input_list=list(map(int, input('Enter the values of the sudoku from left to right row by row with a space in between each number. Replace empty spaces with 0').split())) 
    temp_row=[]
    i=0
    
    while len(input_list)!=0:
          
        temp_row.append(input_list.pop(0))
        i+=1
            
        if i==Columns:
            Sudoku.append(temp_row)
            temp_row=[]
            i=0
            
    return Sudoku, Rows, Columns         
    
Sudoku, Rows, Columns=input_sudoku(Sudoku, Rows, Columns) 
Box_size=int(Rows**0.5)
print(Sudoku)


def visitcells(Columns):
    while True:
        changed_cell=False
        box =0          #box here is actually row i called it box as one row looks like a box in the array too late to chnage now , might at the end for readablity 
        count =0
        
        while count<Columns:
            count+=1
            
            for i, value in enumerate(Sudoku[box]):
                if value==0:
                    if solve_cell(i, box, Box_size, Rows, Sudoku):
                        changed_cell = True                              # this is pretty scuffed just remember the changed_cell here and in the solve_cell function arent the same thats why the loop can restart 

            if count==Columns-1:
                count=0
                if box!=Rows-1: box+=1
                else: break
                
        if not changed_cell:    break
    
def solve_rows(index,row):    
    possible_values=[]
    
    for i in range (1,10):
        if i not in row:
            possible_values.append(i)
    return possible_values     


def solve_columns(index,Sudoku,row,total_rows):
    
    possible_values=[]
    count=0
    temp_list=[]
    
    while count<total_rows:
        temp_list.append(Sudoku[count][index])
        count+=1
    
    for i in range (1,10):
        if i not in temp_list:
            possible_values.append(i)    
    return possible_values 
    
    
    
def solve_box(Box_size,row,index,Sudoku):
    temp_row=row
    temp_index=index
    temp_list=[]
    possible_values=[]
    
    while (temp_index%Box_size)!=0:
        temp_index-=1
    
    
    while (temp_row%Box_size)!=0:
        temp_row-=1
    
    
    for i in range (0,Box_size):
        temp_list.extend(Sudoku[temp_row][temp_index : temp_index + Box_size])
        temp_row+=1
    
    for i in range (1,10):
        if i not in temp_list:
            possible_values.append(i)     
    return possible_values  



def solve_cell(i,box,Box_size,Rows,Sudoku):
    
    column_possible=solve_columns(i,Sudoku,box,Rows)
    box_possible=solve_box(Box_size,box,i,Sudoku)
    row_possible=solve_rows(i,Sudoku[box])
    
    changed_cell=False
    
    common=list(set(row_possible) & set(column_possible) & set(box_possible))
    
    if len(common)==1:                     
        Sudoku[box][i]=common[0]
        changed_cell=True
      
    
    return changed_cell    

visitcells(Columns)
print(Sudoku)    