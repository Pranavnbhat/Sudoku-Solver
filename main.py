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
    pass           #temp pass so program can still run 
    
    box =0          #box here is actually row 
    count =0
    
    while count<Columns:
        count+=1
        
        
        
        for i, value in enumerate(Sudoku[box]):
            if value==0:
                solve_box(Box_size,box,i,Sudoku)
                solve_columns(i,Sudoku,box,Rows)
                solve_rows(i,Sudoku[box])
                
                # if solved_output:                     #solved_outpput can be ignored now this whole if statement can be ignored for now btw this is prolly not needed 
                    # Sudoku[box][i]=solved_output
                # else:	pass
                
        if count==Columns-1:
            count=0
            box+=1
	
    
def solve_rows(index,row):
    pass            #temp pass so program can still run 
    
    possible_values=[]
    
    for i in range (1,10):
        if i not in row:
            possible_values.append(i)
        
    if len(possible_values)==1:
        row[index]=possible_values[0]
        
        
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
   
   
    if len(possible_values)==1:
        Sudoku[row][index]=possible_values[0]

def solve_box(Box_size,row,index,Sudoku):
    temp_row=row
    temp_index=index
    temp_list=[]
    possible_values=[]
    
    while (temp_index%Box_size)!=0:
        temp_index-=1
    temp_index+=1                    # it is off by one number 
    
    while (temp_row%Box_size)!=0:
        temp_row-=1
    temp_row+=1                    # it is off by one number    
    
    for i in range (0,Box_size):
        temp_list.extend(Sudoku[temp_row][temp_index : temp_index + Box_size])
        temp_row+=1
    
    for i in range (1,10):
        if i not in temp_list:
            possible_values.append(i)     

    if len(possible_values)==1:
        Sudoku[row][index]=possible_values[0]



