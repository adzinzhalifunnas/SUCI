def to_rupiah(value):
    str_value = str(value)
    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    
    reverse = after_decimal[::-1]
    temp_reverse_value = ""
    
    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val
    
    temp_result = temp_reverse_value[::-1]
    
    return "Rp. " + temp_result