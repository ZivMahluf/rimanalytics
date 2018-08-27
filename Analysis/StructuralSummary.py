# declaration of relevant fields
file = []
CNTNRlocFeat = {}
CNTNRlocFeatDQ = {}
CNTNRcontents = {}
CNTNRdeterminants = {}
CNTNRFQ = {}
CNTNRapproachSummary = []
CNTNRspecialScores = {}
CNTNRcore = {}
CNTNRideation = {}
CNTNRaffect = {}
CNTNRmediation = {}
CNTNRprocessing = {}
CNTNRinterpersonal = {}
CNTNRselfPerception = {}

def readToArr():
    array = []
    with open("table.txt","r") as f:
        for line in f:
            array.append(line)
    global file
    file = array

def printArr():
    s = ""
    for i in file:
        s+=str(i)
    return s

def locFeatFirst(arr):
    ZEstTable = [0.0, 2.5, 6.0, 10.0, 13.5, 17.0, 20.5, 24.0, 27.5, 31.0, 34.5, 38.0, 41.5,
                 45.5, 49.0, 52.5, 56.0, 59.5, 63.0, 66.5, 70.0, 73.5, 77.0, 81.0, 84.5,
                 88.0, 91.5, 95.0, 98.5, 102.5, 105.5, 109.5, 112.5, 116.5, 120.0, 123.5,
                 127.0, 130.5, 134.0, 137.5, 141.0, 144.5, 148.0, 152.0, 155.5, 159.0,
                 162.5, 166.0, 169.5, 173.0]
    Zf = 0
    ZSum = 0
    ZEst = 0

    for line in arr:
        tokens = line.split('|')

        if (tokens[8]!='EMPTY'):
            Zf +=1
            ZSum += float(tokens[8])
    ZEst = ZEstTable[Zf - 1]
    global CNTNRlocFeat
    CNTNRlocFeat ['Zf'] = Zf
    CNTNRlocFeat['ZSum'] = ZSum
    CNTNRlocFeat['ZEst'] = ZEst

def locFeatSecond(arr):
#not working
    W = 0
    D = 0
    WD = 0
    Dd = 0
    S = 0
    for line in arr:
        l = line.replace('+', '').replace('v/','').replace('o', '').split("|")
        if('W' in l[2]):
            W += 1

        if(l[2] == 'D' or l[2] == 'DS'):
            D +=1

        if('d' in l[2]):
            Dd += 1

        if ('S' in l[2]):
           S += 1

    WD = W + D
    global CNTNRlocFeat
    CNTNRlocFeat['W'] = W
    CNTNRlocFeat['D'] = D
    CNTNRlocFeat['W+D'] = WD
    CNTNRlocFeat['Dd'] = Dd
    CNTNRlocFeat['S'] = S

def locFeatDQ(arr):
    plus = 0
    o = 0
    vplus =0
    v = 0
    for line in arr:
        l = line.split('|')[2]

        if ('v/+' in l):
            vplus += 1

        elif ('+' in l):
            plus += 1

        elif ('o' in l):
            o+=1


        elif ('v' in l):
            v += 1

    global CNTNRlocFeatDQ
    CNTNRlocFeatDQ ['+'] = plus
    CNTNRlocFeatDQ ['o'] = o
    CNTNRlocFeatDQ ['v/+'] = vplus
    CNTNRlocFeatDQ ['v'] = v

def contents(arr):
    global CNTNRcontents
    keys = ['H', '(H)', 'Hd', '(Hd)', 'Hx', 'A', '(A)', 'Ad', '(Ad)',
              'An', 'Art', 'Ay', 'Bl', 'Bt', 'Cg', 'Cl', 'Ex', 'Fd',
              'Fi', 'Ge', 'Hh', 'Ls', 'Na', 'Sc', 'Sx', 'Xy', 'Idio']
    for key in keys:
        CNTNRcontents[key] = 0
    for line in arr:
        l = line.replace(',', '|').replace(' ', '').split('|')
        for token in l:

            if token == 'H':
                CNTNRcontents['H'] += 1
            if token == '(H)':
                CNTNRcontents['(H)'] += 1
            if token == 'Hd':
                CNTNRcontents['Hd'] += 1
            if token == '(Hd)':
                CNTNRcontents['(Hd)'] += 1
            if token == 'Hx':
                CNTNRcontents['Hx'] += 1
            if token == 'A':
                CNTNRcontents['A'] += 1
            if token == '(A)':
                CNTNRcontents['(A)'] += 1
            if token == 'Ad':
                CNTNRcontents['Ad'] += 1
            if token == '(Ad)':
                CNTNRcontents['(Ad)'] += 1
            if token == 'An':
                CNTNRcontents['An'] += 1
            if token == 'Art':
                CNTNRcontents['Art'] += 1
            if token == 'Ay':
                CNTNRcontents['Ay'] += 1
            if token == 'Bl':
                CNTNRcontents['Bl'] += 1
            if token == 'Bt':
                CNTNRcontents['Bt'] += 1
            if token == 'Cg':
                CNTNRcontents['Cg'] += 1
            if token == 'Cl':
                CNTNRcontents['Cl'] += 1
            if token == 'Ex':
                CNTNRcontents['Ex'] += 1
            if token == 'Fd':
                CNTNRcontents['Fd'] += 1
            if token == 'Fi':
                CNTNRcontents['Fi'] += 1
            if token == 'Ge':
                CNTNRcontents['Ge'] += 1
            if token == 'Hh':
                CNTNRcontents['Hh'] += 1
            if token == 'Ls':
                CNTNRcontents['Ls'] += 1
            if token == 'Na':
                CNTNRcontents['Na'] += 1
            if token == 'Sc':
                CNTNRcontents['Sc'] += 1
            if token == 'Sx':
                CNTNRcontents['Sx'] += 1
            if token == 'Xy':
                CNTNRcontents['Xy'] += 1
            if token == 'Idio':
                CNTNRcontents['Idio'] += 1

def determinants(arr):
    Blends = []
    Single = {}
    keys = ['M', 'FM', 'm', 'FC', 'CF', 'C', 'Cn', 'FC\'', 'C\'F', 'C\'',
              'FT', 'TF', 'T', 'FV', 'VF', 'V', 'FY', 'YF', 'Y', 'Fr',
              'rF', 'FD', 'F', '(2)']
    for key in keys:
        Single[key] = 0

    for line in arr:
        tokens = line.replace(' ', '').replace('d', '').replace('o', '').replace('-', '').\
            replace('+', '').replace('a', '').replace('u', '').replace('p', '').split('|')
        if('.' in tokens[4]):
            Blends.append(tokens[4])
        else:
            Single[tokens[4]] += 1
        if(tokens[5] == '2'):
            Single['(2)']+=1

    global CNTNRdeterminants
    CNTNRdeterminants = {'Blends':Blends, 'Single':Single}

def FQ(arr):
    FQx = {'+':0,'o':0,'u':0,'-':0,'none':0}
    MQual = {'+':0,'o':0,'u':0,'-':0,'none':0}
    WD = {'+':0,'o':0,'u':0,'-':0,'none':0}

    ##############################  FQ  ################################

    for line in arr:
        l = line.split('|')
        for c in l[4][-1:]:
            if (c =='+'):
                FQx['+']+=1

            elif (c == 'o'):
                FQx['o'] += 1

            elif (c == 'u'):
                FQx['u'] += 1

            elif (c == '-'):
                FQx['-'] += 1
            else:
                FQx['none'] += 1

    ##############################  MQual   ################################

        tempor = (l[4].replace('+', '')
                  .replace('o', '')
                  .replace('u', '')
                  .replace('a', '')
                  .replace('-', '')
                  .replace('p', ''))

        if('.M.' in tempor or
           '.M' in tempor or
             'M' == l[4][:1]):
        #the part below (235-250) should work fine
            if(l[4][-1:] == '+'):
                MQual['+'] +=1

            elif (l[4][-1:] == 'o'):
                MQual['o'] += 1

            elif (l[4][-1:] == 'u'):
                MQual['u'] += 1

            elif (l[4][-1:] == '-'):
                MQual['-'] += 1
            else:
                MQual['none'] += 1


        ##############################  W+D ################################
        c = l[2].replace('+', '').replace('o', '').replace('v/','').replace('S','').replace(' ','').replace('v','')

        if (c =='W' or c == 'D'):

            if (l[4][-1:] == '+'):
                WD['+'] += 1

            elif (l[4][-1:] == 'o'):
                WD['o'] += 1

            elif (l[4][-1:] == 'u'):
                WD['u'] += 1

            elif (l[4][-1:] == '-'):
                WD['-'] += 1
            else:
                WD['none']+=1


    global CNTNRFQ
    CNTNRFQ = {'FQx':FQx, 'MQual':MQual, 'W+D':WD}

def approachSummary(arr):
    cards = ['','','','','','','','','','']
    count = -1
    for line in arr:
        l = line.replace('+','').replace('v','').replace('/','').replace('o','').split('|')

        if (l[0] != 'EMPTY'):
            count += 1

        if(cards[count]!=''):
            cards[count] += ('.'+l[2])
        else:
            cards[count] += (l[2])


    global CNTNRapproachSummary
    CNTNRapproachSummary = {
             'I':cards[0],
             'II':cards[1],
             'III':cards[2],
              'IV':cards[3],
             'V':cards[4],
             'VI':cards[5],
             'VII':cards[6],
             'VIII':cards[7],
             'IX':cards[8],
             'X':cards[9]}

def specialScores(arr):
    lvl1 = {'DV':0,'INC':0,'DR':0,'FAB':0,'ALOG':0,'CON':0}
    lvl2 = {'DV':0,'INC':0,'DR':0,'FAB':0}
    misc = {'SUM6':0, 'WSUM6':0,
            'AB':0,'AG':0,'COP':0,'CP':0,
            'GHR':0,'PHR':0,'MOR':0,'PER':0,'PSV':0}
    for line in arr:
        l = line.split('|')
        elem = l[9].replace('1','').replace('\n','').replace(' ','').split(',')
        for e in elem:

            if e == 'DV':
                lvl1['DV'] += 1
                misc['SUM6'] += 1

            if (e == 'INC' or
                e == 'INCOM'):
                lvl1['INC'] += 1
                misc['SUM6'] += 1

            if e == 'DR':
                lvl1['DR'] += 1
                misc['SUM6'] += 1

            if (e == 'FAB'or
                e == 'FABCOM'):
                lvl1['FAB'] += 1
                misc['SUM6'] += 1

            if e == 'ALOG':
                lvl1['ALOG'] += 1
                misc['SUM6'] += 1

            if (e == 'CON'or
                e == 'CONTAM'):
                lvl1['CON'] += 1
                misc['SUM6'] += 1
        for e in elem:
            if e == 'DV2':
                lvl2['DV'] += 1
                misc['SUM6'] += 1

            if (e == 'INC2'or
                e == 'INCOM2'):
                lvl2['INC'] += 1
                misc['SUM6'] += 1

            if e == 'DR2':
                lvl2['DR'] += 1
                misc['SUM6'] += 1

            if (e == 'FAB2'or
                e == 'FABCOM2'):
                lvl2['FAB'] += 1
                misc['SUM6'] += 1


        for e in elem:

            if e == 'AB':
                misc['AB'] += 1

            elif e == 'AG':
                misc['AG'] += 1

            elif e == 'COP':
                misc['COP'] += 1

            elif e == 'CP':
                misc['CP'] += 1

            elif e == 'GHR':
                misc['GHR'] += 1

            elif e == 'PHR':
                misc['PHR'] += 1

            elif e == 'MOR':
                misc['MOR'] += 1

            elif e == 'PER':
                misc['PER'] += 1

            elif e == 'PSV':
                misc['PSV'] += 1

    misc["WSUM6"] = (1 * lvl1['DV'] + 2 * lvl2['DV'] +
               2 * lvl1['INC'] + 4 * lvl2['INC'] +
               3 * lvl1['DR'] + 6 * lvl2['DR'] +
               4 * lvl1['FAB'] + 7 * lvl2['FAB'] +
               5 * lvl1['ALOG'] + 7 * lvl1['CON'])
    global CNTNRspecialScores
    CNTNRspecialScores = {'lvl1':lvl1, 'lvl2':lvl2, 'misc':misc}

def core(arr):
    RL = [0, 0]
    EB = [0, 0]
    eb = [0, 0]
    EBPer = []
    EA = []
    es = 0
    adjes = 0
    D = 0
    adjD = 0
    misc = [0, 0, 0, 0, 0, 0]

    RL[0] = len(arr)
    temp = CNTNRdeterminants['Single']['F']
    RL[1] = float("{0:.3f}".format(temp / (RL[0] - temp)))

    ############################        EB          ###############################

    EB[0] = (CNTNRFQ['MQual']['+']+CNTNRFQ['MQual']['o']+
             CNTNRFQ['MQual']['u']+CNTNRFQ['MQual']['-']+
             CNTNRFQ['MQual']['none']) #count 'none'?

    crwldFC = 0
    crwldCF = 0
    crwldC  = 0

    for i in CNTNRdeterminants['Blends']:
        l = i.split('.')
        for token in l:
            if token == 'FC':
                crwldFC+=1
            if token == 'CF':
                crwldCF+=1
            if token == 'C':
                crwldC+=1

    EB[1] = (0.5 * (CNTNRdeterminants['Single']['FC'] + crwldFC) +
             1 * (CNTNRdeterminants['Single']['CF'] + crwldCF) +
             1.5 * (CNTNRdeterminants['Single']['C'] + crwldC))

    ############################        EA          ###############################

    EA = (EB[0] + EB[1])

    ############################        EBPer       ###############################

    if(EB[0]>=EB[1] and EB[1] != 0):
        EBPer = EB[0] / EB[1]
    elif(EB[1] != 0):
        EBPer = EB[1] / EB[0]
    else:
        EBPer = 0

    ############################        eb       ###############################
    crwldFM = 0
    crwldm = 0
    summ = [0,0,0,0]#C',T,V,Y

    for i in CNTNRdeterminants['Blends']:
        l = i.split('.')
        for token in l:
            if token == 'FM':
                crwldFM += 1
            if token == 'm':
                crwldm += 1

        if("C'" in i):
            summ[0] += 1
        if("T" in i):
            summ[1] += 1
        if("V" in i):
            summ[2]+= 1
        if("Y" in i):
            summ[3] += 1

    eb[0] = crwldFM + crwldm + CNTNRdeterminants['Single']['FM'] + CNTNRdeterminants['Single']['m']

    # all determinants with C' in Singles
    eb[1] += (summ[0] + CNTNRdeterminants['Single']['FC\''] + CNTNRdeterminants['Single']['C\'F'] + CNTNRdeterminants['Single']['C\''])
    # all determinants with T in Singles
    eb[1] += (summ[1] + CNTNRdeterminants['Single']['FT'] + CNTNRdeterminants['Single']['TF'] + CNTNRdeterminants['Single']['T'])
    # all determinants with V in Singles
    eb[1] += (summ[2] + CNTNRdeterminants['Single']['FV'] + CNTNRdeterminants['Single']['VF'] + CNTNRdeterminants['Single']['V'])
    # all determinants with Y in Singles
    eb[1] += (summ[3] + CNTNRdeterminants['Single']['FY'] + CNTNRdeterminants['Single']['YF'] + CNTNRdeterminants['Single']['Y'])

    ############################        es       ###############################
    es = eb[0] + eb[1]

    ############################        D        ###############################
    Dscore = float(EA - es)

    '''
    #
    IF ELSE statements below needs strong revision for efficiency
    #
    '''
    if(Dscore > 15):
        D += 6
    elif (Dscore >= 13 and Dscore <= 15):
        D += 5
    elif(Dscore >= 10.5 and Dscore < 13):
        D += 4
    elif (Dscore >= 8 and Dscore < 10.5):
        D += 3
    elif(Dscore >= 5.5 and Dscore < 8):
        D += 2
    elif (Dscore >= 3 and Dscore < 5.5):
        D += 1
    elif (Dscore >= -2.5 and Dscore < 3):
        D += 0
    elif (Dscore < -2.5 and Dscore >= -5):
        D += -1
    elif (Dscore < -5 and Dscore >= -7.5):
        D += -2
    elif (Dscore < -7.5 and Dscore >= -10):
        D += -3
    elif (Dscore < -10 and Dscore >= -12.5):
        D += -4
    elif (Dscore < -12.5 and Dscore >= -15):
        D += -5
    elif (Dscore < -15):
        D += -6

    ############################        adjes       ###############################
    '''
    in case of a,b 1 should be subtracted only IF a OR b not <= 0
    '''
    a = (summ[3] + CNTNRdeterminants['Single']['FY'] +
                   CNTNRdeterminants['Single']['YF'] +
                   CNTNRdeterminants['Single']['Y'])
    b = (crwldm + CNTNRdeterminants['Single']['m'])

    a = a if (a <= 0) else (a - 1)
    b = b if (b <= 0) else (b - 1)

    adjes = es - (a + b)
    ############################        adjD        ###############################
    Dscore = EA - adjes
    if (Dscore >= 13 and Dscore <= 15):
        adjD+= 5
    elif(Dscore >= 10.5 and Dscore < 13):
        adjD+= 4
    elif (Dscore >= 8 and Dscore < 10.5):
        adjD+= 3
    elif(Dscore >= 5.5 and Dscore < 8):
        adjD+= 2
    elif (Dscore >= 3 and Dscore < 5.5):
        adjD+= 1
    elif (Dscore >= -2.5 and Dscore < 3):
        adjD += 0
    elif (Dscore < -2.5 and Dscore >= -5):
        adjD+= -1
    elif (Dscore < -5 and Dscore >= -7.5):
        adjD+= -2
    elif (Dscore < -7.5 and Dscore >= -10):
        adjD+= -3
    elif (Dscore < -10 and Dscore >= -12.5):
        adjD+= -4
    elif (Dscore < -12.5 and Dscore >= -15):
        adjD+= -5
    else:
        adjD+= 'ERROR'
    ############################   misc     ###############################
    misc[0] = crwldFM + CNTNRdeterminants['Single']['FM']
    misc[1] = crwldm + CNTNRdeterminants['Single']['m']

    misc[2] = (summ[0] +
               CNTNRdeterminants['Single']['FC\''] +
               CNTNRdeterminants['Single']['C\'F'] +
               CNTNRdeterminants['Single']['C\''])   #C'
    misc[3] = (summ[1] +
               CNTNRdeterminants['Single']['FT'] +
               CNTNRdeterminants['Single']['TF'] +
               CNTNRdeterminants['Single']['T'])
    misc[4] = (summ[2] +
               CNTNRdeterminants['Single']['FV'] +
               CNTNRdeterminants['Single']['VF'] +
               CNTNRdeterminants['Single']['V'])#V
    misc[5] = (summ[3] +
               CNTNRdeterminants['Single']['FY'] +
               CNTNRdeterminants['Single']['YF'] +
               CNTNRdeterminants['Single']['Y'])#Y

    global CNTNRcore
    CNTNRcore = {'R': RL[0], 'L': RL[1],
                 'EB': EB,
                 'eb': eb,
                 'EBPer': EBPer,
                 'EA': EA,
                 'es': es,
                 'D': D,
                 'adjes': adjes,
                 'adjD': adjD,

                 'FM': misc[0], 'm': misc[1],
                 'C\'': misc[2], 'T': misc[3], 'V': misc[4], 'Y': misc[5]}

def ideation(arr):
    ap = [0,0]
    MaMp = [0,0]
    INTELL = 0
    MOR = CNTNRspecialScores['misc']['MOR']
    SUM6 = CNTNRspecialScores['misc']['SUM6']
    lvl2 = (sum(CNTNRspecialScores['lvl2'].values()))
    WSUM6 = CNTNRspecialScores['misc']['WSUM6']
    Mminus = 0
    Mnone = 0
    ############################        a:p    Ma:Mp          ###############################
    for line in arr:
        l = line.split('|')
        l4 = l[4].replace('+','').replace('-','').replace('o','').replace('u','')
        for i in l4.split('.'):
            if('a' in i):
                ap[0]+=1
            if ('p' in i):
                ap[1] += 1

        for i in l4.split('.'):
            if('Ma' == i):
                MaMp[0] += 1
            if ('Mp' == i):
                MaMp[1] += 1
            if('Map' == i):
                MaMp[0] += 1
                MaMp[1] += 1

    ############################        INTELL          ###############################

    INTELL = 2*(CNTNRspecialScores['misc']['AB'])+(CNTNRcontents['Art']+CNTNRcontents['Ay'])

    ############################        Mminus          ###############################

    for line in arr:
        l = line.split('|')[4]
        t = l.split('.')
        for z in t:
            if(z == 'Ma-' or
               z == 'Mp-' or
               z == 'Map-' or
              (z == 'Mp' and l[len(l) - 1] == '-') or
              (z == 'Ma' and l[len(l) - 1] == '-')):
                Mminus += 1
            if((z == 'Ma' or z == 'Mp' or z == 'Map') and not
                    ((l[len(l) - 1] == '+') or
                    (l[len(l) - 1] == 'o') or
                    (l[len(l) - 1] == 'u') or
                    (l[len(l) - 1] == '-'))):
                Mnone += 1

    global CNTNRideation
    CNTNRideation ={'a:p':ap, 'SUM6':SUM6, 'Ma:Mp':MaMp, 'lvl2':lvl2, 'INTELL':INTELL, 'WSUM6':WSUM6, 'MOR':MOR, 'M-':Mminus, 'Mnone':Mnone}

def affect(arr):
    FCCFC = [CNTNRdeterminants['Single']['FC'],
                CNTNRdeterminants['Single']['CF'] +
                CNTNRdeterminants['Single']['C'] +
                CNTNRdeterminants['Single']['Cn']]
    pureC = CNTNRdeterminants['Single']['C']
    SumCWSumC = [CNTNRdeterminants['Single']['FC\''] +
                 CNTNRdeterminants['Single']['C\'F'] +
                 CNTNRdeterminants['Single']['C\''], CNTNRcore['EB'][1]]
    Afr = 0.0
    S = CNTNRlocFeat['S']
    BlendsR = [len(CNTNRdeterminants['Blends']),len(arr)]
    CP = CNTNRspecialScores['misc']['CP']
    ############################        FCCFC,pureC,SumC'WSumC        ###############################
    for i in CNTNRdeterminants['Blends']:
        l = i.split('.')
        for z in l:
            if z == 'FC':
                FCCFC[0] += 1
            if (z == 'CF'or
                z == 'Cn'):
                FCCFC[1] += 1

            if (z == 'C'):
                FCCFC[1] += 1
                pureC += 1
            if ("C'" in z):
                SumCWSumC[0] += 1
    ############################       Afr          ###############################
    a,temp = 0,0
    for line in arr:
        l = line.split('|')[0]
        temp += 1
        if (l == 'VIII'):
            a = temp - 1
            temp = 1
    Afr = temp / a

    global CNTNRaffect
    CNTNRaffect = {'FC:CF+C':FCCFC, 'pureC':pureC, 'SumC\':WSumC':SumCWSumC,
                        'Afr':float("{0:.3f}".format(Afr)), 'S':S, 'Blends:R':BlendsR, 'CP':CP}

def mediation(arr):
    R = len(arr)
    XA = ((CNTNRFQ['FQx']['+']+CNTNRFQ['FQx']['o']+CNTNRFQ['FQx']['u'])/
                            R)
    WDA = ((CNTNRFQ['W+D']['+']+CNTNRFQ['W+D']['o']+CNTNRFQ['W+D']['u']) /
           CNTNRlocFeat['W+D'])
    Xminus = (CNTNRFQ['FQx']['-'] / R)
    Sminus = 0
    P = 0
    Xplus = ((CNTNRFQ['FQx']['+']+CNTNRFQ['FQx']['o']) / R)
    Xu = CNTNRFQ['FQx']['u'] / R
    ############################        Sminus and P       ###############################
    for line in arr:
        l = line.split("|")
        if(('S' in l[2]) and (l[4][len(l[4])-1]) == '-'):
            Sminus += 1
        if(l[7] == 'P'):
            P+=1
    global CNTNRmediation
    CNTNRmediation = {'XA%': float("{0:.3f}".format(XA)),
                      'WDA%':float("{0:.3f}".format(WDA)),
                       'X-%': float("{0:.3f}".format(Xminus)),
                       'S-':Sminus,
                        'P':P,
                        'X+%':float("{0:.3f}".format(Xplus)),
                        'Xu%':float("{0:.3f}".format(Xu))}

def processing(arr):
    Zf = CNTNRlocFeat['Zf']
    WDDd = [CNTNRlocFeat['W'], CNTNRlocFeat['D'], CNTNRlocFeat['Dd']]
    WM = [CNTNRlocFeat['W'], CNTNRcore['EB'][0]]
    Zd = CNTNRlocFeat['ZSum'] - CNTNRlocFeat['ZEst']
    PSV = CNTNRspecialScores['misc']['PSV']
    DQPlus = CNTNRlocFeatDQ['+']
    DQv = CNTNRlocFeatDQ['v']
    global CNTNRprocessing
    CNTNRprocessing = {'Zf':Zf, 'W:D:Dd':WDDd, 'W:M':WM, 'Zd':Zd, 'PSV':PSV, 'DQ+':DQPlus, 'DQv':DQv}

def interpersonal(arr):
    R = len(arr)
    COP = CNTNRspecialScores['misc']['COP']
    AG = CNTNRspecialScores['misc']['AG']
    GHRPHR = [CNTNRspecialScores['misc']['GHR'],CNTNRspecialScores['misc']['PHR']]
    ap = CNTNRideation['a:p']
    Food = CNTNRcontents['Fd']
    SumT = CNTNRcore['T']
    humanContent = (CNTNRcontents['H'] +
                    CNTNRcontents['(H)'] +
                    CNTNRcontents['Hd'] +
                    CNTNRcontents['(Hd)'])
    pureH = CNTNRcontents['H']
    PER = CNTNRspecialScores['misc']['PER']
    isolationIndex = ((CNTNRcontents['Bt'] + (CNTNRcontents['Cl'] * 2)+
                       CNTNRcontents['Ge'] +CNTNRcontents['Ls']+
                      (CNTNRcontents['Na']*2)) / R)
    #not sure if isolationIndex is correct
    global CNTNRinterpersonal
    CNTNRinterpersonal = {'COP':COP, 'AG':AG, 'GHR:PHR':GHRPHR, 'a:p':ap, 'Food':Food,
                          'SumT':SumT, 'H':humanContent, 'pureH':pureH, 'PER':PER, 'isol':float("{0:.3f}".format(isolationIndex))}

def selfPerception(arr):
    R = len(arr)
    egocentricityIndex = (3*
                          (CNTNRdeterminants['Single']['Fr']+CNTNRdeterminants['Single']['rF'])
                          +CNTNRdeterminants['Single']['(2)']) / R

    FrrF = (CNTNRdeterminants['Single']['Fr']+CNTNRdeterminants['Single']['rF'])
    SumV = CNTNRcore['V']
    FD = 0
    AnXy = CNTNRcontents['An'] + CNTNRcontents['Xy']
    MOR = CNTNRspecialScores['misc']['MOR']

    HHHdHd = [CNTNRcontents['H'],CNTNRcontents['(H)']+CNTNRcontents['Hd']+CNTNRcontents['(Hd)']]
    ############################        Sminus        ###############################
    for line in arr:
        if('FD' in line):
            FD+=1
    global CNTNRselfPerception
    CNTNRselfPerception = {'3r+(2)/R': float("{0:.3f}".format(egocentricityIndex)), 'Fr+rF':FrrF, 'SumV':SumV,
                           'FD':FD, 'An+Xy':AnXy, 'MOR':MOR, 'H:(H)+Hd+(Hd)':HHHdHd}

def main(file):
    '''This function basically does 2 things:
    1. Initiates all the Analysis methods, to fill global variables
    2. Returns a dictionary with analyzed scores
    '''
    #1
    approachSummary(file)
    locFeatFirst(file)
    locFeatSecond(file)
    locFeatDQ(file)
    determinants(file)
    contents(file)
    FQ(file)
    specialScores(file)
    core(file)
    ideation(file)
    affect(file)
    mediation(file)
    processing(file)
    interpersonal(file)
    selfPerception(file)
    #2
    return {'locFeat': CNTNRlocFeat,
     'locFeatDQ': CNTNRlocFeatDQ,
     'contents': CNTNRcontents,
     'determinants': CNTNRdeterminants,
     'FQ': CNTNRFQ,
     'approachSummary': CNTNRapproachSummary,
     'specialScores': CNTNRspecialScores,
     'core': CNTNRcore,
     'ideation': CNTNRideation,
     'affect': CNTNRaffect,
     'mediation': CNTNRmediation,
     'processing': CNTNRprocessing,
     'interpersonal': CNTNRinterpersonal,
     'selfPerception': CNTNRselfPerception}
