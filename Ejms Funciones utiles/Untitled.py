def find_sums (numbers: list, target: int) -> list:
    def find_sum (start: int, target:int, combination: int):
    # Solucion encontrada
        if target == 0:
            return
        
        #no solucion
        if target < 0 or start== len(numbers):
            return
        
        #busqueda
        for index in range(start, len(numbers)):
            if numbers[index] == numbers[index - 1]:
                continue
            
            combination.append(numbers[index])
            find_sum(index + 1, target - numbers[index], combination)
        
    numbers.sort()
    result=[]
    find_sum (0,target,[])
    return result
    
        
