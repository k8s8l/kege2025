for n in range(1,100):
    st=n*'0'
    while '10' in st or '1' in st:
        if '10' in st:
            st=st.replace('10','0001',1)
            
