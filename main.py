Sudoku = []
Rows=0
Columns=0

def input_sudoku(Sudoku,x,y):
    
    x= int(input('Enter Rows '))
    y= int(input('Enter Columns'))
    
    input_list=list(map(int, input('Enter the values of the sudoku from left to right row by row with a space in between each number. Replace empty spaces with 0').split())) 
    temp_row=[]
    i=0
    
    while len(input_list)!=0:
          
        temp_row.append(input_list.pop(0))
        i+=1
            
        if i==y:
            Sudoku.append(temp_row)
            temp_row=[]
            i=0
    
input_sudoku(Sudoku, Rows, Columns) 
print(Sudoku)


def visitcells():
    pass
    # box =0
    # count =0
        
        
        
        
    # while count<y:
        # count+=1
        
        
        
        # for i, value in enumerate(Sudoku[box]):
            # if value==0:
                # solve_lines(i,Sudoku[box])
                
                # if solved_output:
                    # Sudoku[box][i]=solved_output
                # else:	pass
                
        # if count==y-1:
            # count=0
            # box+=1
	
    
def solve_lines(x,list[box]):
    pass
     