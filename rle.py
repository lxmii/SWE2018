
import sys
def rle_encoder(txt):
    """ RLE encoder modetager en streng og returner en streng
        med så gentagne bogstaver bilver erstattet med bogstavet og
         antallet af gentagelser

         "bbbkkk" bliver "b3k3"
         """
    c = txt[0]
    i = 1
    res = []
    for x in txt[1:]:
        if x == c:
            i += 1
        else: 
            res.append(f'{c}{i}')
            c=x
            i=1
    res.append(f'{c}{i}')
            
    return ''.join(res)

def rle_decoder(txt):
    # 'l'*3 ->'lll'
    
    c = txt[0]
    res = []
    for x in txt[1:]:
        if  x.isdigit():
            res.append(c*int (x))
            
        else:
            c=x        
    return ''.join(res)

if __name__=="__main__":
    args= sys.argv
    print(args)
    if argv[1]=='-d':
        rle_decoder(args[2])
    else:
        rle_encoder(args[2])
