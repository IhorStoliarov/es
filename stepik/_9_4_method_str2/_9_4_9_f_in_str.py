st = input()
ct = 0

if st.count('f') == 1:
    print(st.find('f'))
if st.count('f') > 1:
    print(st.find('f'), end=' ')
    print(st.rfind('f'))
if st.count('f') == 0:
    print('NO')


