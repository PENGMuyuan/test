def HD_InMemoryADC_Search(input, precision):
    
    shape1=input.shape[0]
    shape2=input.shape[1]
    HD_value=np.zeros((shape1,shape2))

    x_values=np.loadtxt('DivisionData/{}_bit_ADC'.format(precision))
    #print(x_values)
    
    Search_mid=np.zeros((shape1,shape2,len(x_values)))
    for i in range(len(x_values)):
        for k1 in range(shape1):
            for k2 in range(shape2):
                
                Search_mid[k1][k2][i]=input[k1][k2]-x_values[i]

    Search_mid_index=np.zeros((shape1,shape2))
    for j in range(len(x_values)):
        for l1 in range(shape1):
            for l2 in range(shape2):
                if (Search_mid[l1][l2][j]>0.01):
                    Search_mid_index[l1][l2]+=1
                    #print(l1,l2,Search_mid_index[l1][l2])
    
    for m1 in range(shape1):
        for m2 in range(shape2):
            idx=0
            idx=int(Search_mid_index[m1][m2]-1)
            HD_value[m1][m2]=int(x_values[idx])
        
    return (HD_value)

def HD_ADC_Search(input, precision):
    
    shape1=input.shape[0]
    shape2=input.shape[1]
    HD_value=np.zeros((shape1,shape2))
    length=pow(2,precision)
    ADC_interval=pow(2,7-precision)
 
    
    Search_mid=np.zeros((shape1,shape2,length))
    for i in range(length):
        for k1 in range(shape1):
            for k2 in range(shape2):
                
                Search_mid[k1][k2][i]=input[k1][k2]-i*ADC_interval

    Search_mid_index=np.zeros((shape1,shape2))
    for j in range(length):
        for l1 in range(shape1):
            for l2 in range(shape2):
                if (Search_mid[l1][l2][j]>0.0001):
                    HD_value[l1][l2]+=1
    
    
        
    return HD_value