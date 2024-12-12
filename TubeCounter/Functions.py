def meandr_caunt(len_to, mylengh, mywidth, step):
    sq_sum = 0
    while mylengh >= step and mywidth >= step:
        sq_sum += mylengh * 2 + mywidth * 2 + step * 2
        mylengh = mylengh - step * 2
        mywidth = mywidth - step * 2

    return  len_to * 2 + sq_sum

def snake_caunt (len_to, mylengh, mywidth, step):
    x = max(mylengh, mywidth)
    y = min(mylengh, mywidth)
    sq_sum = x / step * (y + step)

    return sq_sum + len_to * 2

print('the result is:')
print(meandr_caunt(13,3.7,2, 0.15))
print(snake_caunt(13,3.7,2, 0.15))

