def main():
    data=[[2,2,2,2],[2,2,2,2],[2,2,2,2]]
    matrix = []
    empty_cell = ['']
    for ele in data:
        ele = empty_cell + ele    
        matrix.append(ele)
        empty_cell = ['']    
    return matrix
    
if __name__=="__main__":
    main()


