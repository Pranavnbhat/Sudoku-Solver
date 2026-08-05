Sudoku = []
Rows=0
Columns=0

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
print(Sudoku)


def visitcells(Columns):
    pass           #temp pass so program can still run 
    
    box =0       #box here is actually row 
    count =0
    
    while count<Columns:
        count+=1
        
        
        
        for i, value in enumerate(Sudoku[box]):
            if value==0:
                solve_lines(i,Sudoku[box])
                
                if solved_output:
                    Sudoku[box][i]=solved_output
                else:	pass
                
        if count==Columns-1:
            count=0
            box+=1
	
    
def solve_lines(index,row):
    pass            #temp pass so program can still run 
    
    possible_values=[]
    
    for i in range (1,10):
        if i not in row:
            possible_values.append(i)
        
    if len(possible_values)==1:
        row[index]=possible_values[0]
    
    