from pandas import DataFrame



def calc(archive, sieve):
    sieve_list = []
    a, b, c, d, e, f, g, h, I, j, k, l, m, n, o, p, q, r, s, t, u, v, x, w, y, z = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] 
    index_list = 'A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'X:', 'Y:', 'W:', 'Z:' 
    index_list_number = ['0:', '5:', '10:', '15:', '20:', '25:', '30:', '35:', '40:', '45:', '50:', '55:', '60:', '65:', '70:', '75:', '80:', '85:', '90:', '95:', '100:', '105:', '110:', '115:', '120:', '125:', '130:', '135:', '140:', '145:', '150:', '155:', '160:', '165:', '170:', '175:', '180:', '185:', '190:', '195:', '200:', '205:', '210:', '215:', '220:', '225:', '230:', '235:', '240:', '245:', '250:', '255:', '260:', '265:', '270:', '275:', '280:', '285:', '290:', '295:']
    index_match = ''
    start_date = ''
    for i in sieve:
        sieve_list.append(i.split())

    for i in archive:
        
        if "File" in i:
            i  = i.replace('C:\\', '')
        temp = i.split()
        print(temp)
        if len(temp) == 3:
            if 'Start' == temp[0] and 'Date:' == temp[1]:
                start_date = temp[2]

        if len(temp) > 1:
            if temp[0] in index_list:
                index_match = temp[0]
        elif temp == []:
            continue
        elif temp[0][0:2] in index_list:
            index_match = temp[0][0:2]
        

        for ii in temp: 
            if ii in index_list:
                continue
            elif ii in index_list_number:
                continue
            match index_match:
                case 'A:':
                    a.append(ii)
                case 'B:':
                    b.append(ii)
                case 'C:':
                    c.append(ii)
                case 'D:':
                    d.append(ii)
                case 'E:':
                    e.append(ii)
                case 'F:':
                    f.append(ii)
                case 'G:':
                    g.append(ii)
                case 'H:':
                    h.append(ii)
                case 'I:':
                    I.append(ii)
                case 'J:':
                    j.append(ii)
                case 'K:':
                    k.append(ii)
                case 'L:':
                    l.append(ii)
                case 'M:':
                    m.append(ii)
                case 'N:':
                    n.append(ii)
                case 'O:':
                    o.append(ii)
                case 'P:':
                    p.append(ii)
                case 'Q:':
                    q.append(ii)
                case 'R:':
                    r.append(ii)

    #print(c)
    data_dict =  {'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'g':g, 'h':h, 'i':I, 'j':j, 'k':k, 'l':l, 'm':m, 'n':n, 'o':o, 'p':p, 'q':q, 'r':r, 's':s, 't':t, 'u':u, 'v':v, 'x':x, 'w':w, 'y':y, 'z':z} 
    data = []
    for i in sieve_list:
        if i != []:
            temp = i[0].split('-')
            data.append(data_dict[temp[0].lower()][int(temp[1])].replace('.', ','))
    result = DataFrame({start_date: data})
    result.to_clipboard(excel=True, index=False)


    # Resetando todas as variáveis
    sieve_list = []
    a, b, c, d, e, f, g, h, I, j, k, l, m, n, o, p, q, r, s, t, u, v, x, w, y, z = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] 
    index_list = 'A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'X:', 'Y:', 'W:', 'Z:' 
    index_list_number = ['0:', '5:', '10:', '15:', '20:', '25:', '30:', '35:', '40:', '45:', '50:', '55:', '60:', '65:', '70:', '75:', '80:', '85:', '90:', '95:', '100:', '105:', '110:', '115:', '120:', '125:', '130:', '135:', '140:', '145:', '150:', '155:', '160:', '165:', '170:', '175:', '180:', '185:', '190:', '195:', '200:', '205:', '210:', '215:', '220:', '225:', '230:', '235:', '240:', '245:', '250:', '255:', '260:', '265:', '270:', '275:', '280:', '285:', '290:', '295:']
    index_match = ''
    start_date = ''
    return 'Copied'
