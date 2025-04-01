for n in range(3,2000):
    st='3'*n +'5'
    while '23' in st or '5333' in st or '33333' in st:
        if '23' in st:
            st=st.replace('23','3',1)
        if '5333' in st:
            st=st.replace('5333','32',1)
        if '33333' in st:
            st=st.replace('33333','55',1)

