CNTNR_SS = {}
arr = {}

Boolscon = []
Boolpti = []
Booldepi = []
Boolcdi = []
Boolhvi = []
Boolobs = []

pos = {}
def scon():
    global arr
    global Boolscon
    global pos
    Boolscon = [False for x in range(12)]

    ############################     FV+VF+V+FD>2      ###############################
    arr['FV'] = CNTNR_SS['determinants']['Single']['FV']
    arr['VF'] = CNTNR_SS['determinants']['Single']['VF']
    arr['V'] = CNTNR_SS['determinants']['Single']['V']
    arr['FD'] = CNTNR_SS['determinants']['Single']['FD']

    for line in CNTNR_SS['determinants']['Blends']:
        for l in line.split('.'):
            if('FV' == l):
                arr['FV']+=1
            elif ('VF' == l):
                arr['VF']+=1
            elif ('V' == l):
                arr['V'] += 1
            elif ('FD' == l):
                arr['FD'] += 1

    if(arr['FV']+arr['VF']+
      arr['V'] +arr['FD']>2):
        Boolscon[0] = True

    ############################     Col-Shd Blends  >0   ###############################
    blends = CNTNR_SS['determinants']['Blends']
    arr["Col-Shd"] = 1
    arr["LIST_Col-Shd"] = []
    for b in blends:
        for i in b.split("."):
            if((i =="FC'" or
                    i =="C'" or
                        i =="C'F") and
                ("Y" in b or
                    "T" in b or
                        "V" in b)):
                arr["Col-Shd"] += 1
                arr['LIST_Col-Shd'].append(b)
                arr['LIST_Col-Shd'].append(b)
    if(arr["Col-Shd"] > 0):
        Boolscon[1] = True

    ############################     Ego    ###############################
    arr['ego'] = CNTNR_SS['selfPerception']['3r+(2)/R']
    if(arr['ego'] < 0.31 or
       arr['ego'] > 0.44):
        Boolscon[2] = True

    ############################     MOR    ###############################
    arr['MOR'] = CNTNR_SS['specialScores']['misc']['MOR']
    if(arr['MOR']>3):
        Boolscon[3] = True

    ############################     Zd    ###############################
    arr['Zd'] = CNTNR_SS['processing']['Zd']
    if (arr['Zd'] > 3.5 or arr['Zd'] < -3.5):
        Boolscon[4] = True

    ############################     es>EA    ###############################
    arr['es>EA'] = [CNTNR_SS['core']['es'], CNTNR_SS['core']['EA']]
    if (arr['es>EA'][0] > arr['es>EA'][1]):
        Boolscon[5] = True

    ############################     CF+C>FC    ###############################
    arr['CF+C>FC'] = [CNTNR_SS['affect']['FC:CF+C'][1], CNTNR_SS['affect']['FC:CF+C'][0]]

    if(arr['CF+C>FC'][0] > arr['CF+C>FC'][1]):
        Boolscon[6] = True

    ############################     X+%    ###############################
    arr['X+%'] = CNTNR_SS['mediation']['X+%']
    if(arr['X+%'] < 0.70):
        Boolscon[7] = True

    ############################     S    ###############################
    arr['S'] = CNTNR_SS['locFeat']['S']
    if(arr['S'] > 3):
        Boolscon[8] = True

    ############################     P    ###############################
    arr['P'] = CNTNR_SS['mediation']['P']
    if(arr['P'] < 3 or
       arr['P'] > 8):
        Boolscon[9] = True
    ############################  pureH   ###############################
    arr['pureH'] = CNTNR_SS['interpersonal']['pureH']
    if(arr['pureH'] < 2):
        Boolscon[10] = True
    ############################     R    ###############################
    arr['R'] = CNTNR_SS['core']['R']
    if(arr['R']<17):
        Boolscon[11] = True

def pti():
    global Boolpti
    Boolpti = [False for x in range(5)]
    ############################     XA% and WDA%    ###############################
    if(CNTNR_SS['mediation']['XA%']<0.7 and
       CNTNR_SS['mediation']['WDA%']<0.75):
        Boolpti[0] = True
    ############################     X-%>0.29    ###############################
    if(CNTNR_SS['mediation']['X-%'] > 0.29):
        Boolpti[1] = True
    ####################         SumLvl2>2 and FAB2 > 0     ####################
    if(CNTNR_SS['ideation']['lvl2'] > 2 and
       CNTNR_SS['specialScores']['lvl2']['FAB'] > 0):
        Boolpti[2] = True
    ###################(R<17 and WSum6>12) or  (R>16 and WSum6>17)  ###############################
    if((CNTNR_SS['core']['R'] < 17 and CNTNR_SS['ideation']['WSUM6'] > 12)or
        (CNTNR_SS['core']['R'] > 16 and CNTNR_SS['ideation']['WSUM6'] > 17)):
        Boolpti[3] = True
    ############################     M->1 or X-%>0.40    ###############################
    if(CNTNR_SS['ideation']['M-'] > 1 or
       CNTNR_SS['mediation']['X-%'] > 0.40):
        Boolpti[4] = True

def depi():
    global Booldepi
    global pos
    Booldepi = [False for x in range(7)]

    ####################### FV+VF+V>0 or FD>2  ############################
    if((arr['FV']+arr['VF']+arr['V'])>0 or arr['FD']>2):
        Booldepi[0] = True
    ####################### (Col-Shd Blends>0) or S>2  ############################
        #REV
        if(arr["Col-Shd"] > 0 or CNTNR_SS['locFeat']['S'] > 2):
            Booldepi[1] = True
    ####################### (3r+2/R>0.44 and Fr+rF=0) or (3r+2/R>0.33 ) ############################
    if((CNTNR_SS['selfPerception']['3r+(2)/R']>0.44 and CNTNR_SS['selfPerception']['Fr+rF']==0)
                            or
       (CNTNR_SS['selfPerception']['3r+(2)/R']<0.33)):
        Booldepi[2] = True
    #######################  Afr<0.46 or Blends<4  ############################
    if(CNTNR_SS['affect']['Afr']<0.46
                    or
       len(CNTNR_SS['determinants']['Blends'])<4):
        Booldepi[3] = True

    #######################  SumShd>FM+M  or  SumC'>2############################
    if(CNTNR_SS['core']['eb'][1] > (CNTNR_SS['core']['FM'] + CNTNR_SS['core']['m']) or
       CNTNR_SS['affect']['SumC\':WSumC'][0] > 2):
        Booldepi[4] = True
    #######################  (MOR > 2) or (2*AB+Art+Ay >3)  ############################
    if(CNTNR_SS['specialScores']['misc']['MOR']>2
                        or
       CNTNR_SS['ideation']['INTELL']>3):
        Booldepi[5] = True
    #######################  COP > 2 or (Bt+ 2*Cl+Ge+Ls+2*Na)>0.24  ############################
    if(CNTNR_SS['specialScores']['misc']['COP'] < 2
                        or
           CNTNR_SS['interpersonal']['isol'] > 0.24):
        Booldepi[6] = True

def cdi():
    global Boolcdi

    Boolcdi = [False for x in range(5)]
    #######################  EA<6 or adjD<0  ############################
    if(CNTNR_SS['core']['EA']<6
                or
       int(CNTNR_SS['core']['adjD'])<0):
        Boolcdi[0] = True

    #######################  COP<2 and AG<2  ############################
    if(CNTNR_SS['specialScores']['misc']['COP']<2
                        and
       CNTNR_SS['specialScores']['misc']['AG']<2):
        Boolcdi[1] = True

    #######################  WSumC<2.5 Afr<0.46  ########################
    if(CNTNR_SS['affect']['SumC\':WSumC'][1]<2.5
                    or
           CNTNR_SS['affect']['Afr']<0.46):
        Boolcdi[2] = True

    #######################  passive>active+1 or PureH<2  ########################
    if(CNTNR_SS['ideation']['a:p'][1] > CNTNR_SS['ideation']['a:p'][0]+1
                                or
       CNTNR_SS['interpersonal']['pureH'] < 2):
        Boolcdi[3] = True

    #######################  SumT>2 or Isol/R>0.24 or Food>0  ########################
    if(CNTNR_SS['interpersonal']['SumT'] > 1
                    or
      (CNTNR_SS['interpersonal']['isol'] / CNTNR_SS['core']['R'] > 0.24)
                    or
       CNTNR_SS['interpersonal']['Food'] > 0):
        Boolcdi[4] = True

def hvi():
    global Boolhvi
    global pos
    Boolhvi = [False for x in range(8)]
    '''Postitive if condition 1 is True
        and at least 4 others are True also'''
    ####################### FT+TF+T == 0 ########################
    arr['FT'] = CNTNR_SS['determinants']['Single']['FT']
    arr['TF'] = CNTNR_SS['determinants']['Single']['TF']
    arr['T'] = CNTNR_SS['determinants']['Single']['T']

    for line in CNTNR_SS['determinants']['Blends']:
        if ('FT' in line):
            arr['FT'] += 1
        if ('TF' in line):
            arr['TF'] += 1
        if ('T' in line):
            arr['T'] += 1

    if (arr['FT'] + arr['TF'] +
            arr['T'] == 0):
        Boolhvi[0] = True
    ####################### Zf > 12  ######## #################
    if(CNTNR_SS['locFeat']['Zf'] > 12):
        Boolhvi[1] = True
    ####################### Zd > +3.5  ########################
    if(CNTNR_SS['processing']['Zd']>3.5):
        Boolhvi[2] = True
    ####################### S > 3  ########################
    if(CNTNR_SS['locFeat']['S'] > 3):
        Boolhvi[3] = True
    ####################### H+(H)+Hd+(Hd) > 6   ########################
    if(CNTNR_SS['interpersonal']['H'] > 6):
        Boolhvi[4] = True
    ####################### H+(A)+(Hd)+(Ad) > 3  ########################
        if((CNTNR_SS['contents']['(H)'] + CNTNR_SS['contents']['(A)']+
           CNTNR_SS['contents']['(Hd)'] + CNTNR_SS['contents']['(Ad)']) > 3):
            Boolhvi[5] = True
    ####################### H+A:Hd+Ad < 4:1    ########################
    a = (CNTNR_SS['contents']['H'] + CNTNR_SS['contents']['A'] +
        CNTNR_SS['contents']['(H)'] + CNTNR_SS['contents']['(A)'])
    b = (CNTNR_SS['contents']['Hd'] + CNTNR_SS['contents']['Ad'] +
         CNTNR_SS['contents']['(Hd)'] + CNTNR_SS['contents']['(Ad)'])

    if(b == 0):
        pass
    elif ((a/b) < (4/1)):
        Boolhvi[6] = True

    ####################### Cg>3   ########################
    if(CNTNR_SS['contents']['Cg'] > 3):
        Boolhvi[7] = True

def obs():
    global Boolobs
    Boolobs = [False for x in range(9)]
    ####################### Dd > 3 ########################
    if(CNTNR_SS['locFeat']['Dd'] > 3):
        Boolobs[0] = True
    ####################### Zf > 12 ########################
    if(CNTNR_SS['locFeat']['Zf'] > 12):
        Boolobs[1] = True
    ####################### Zd > +3.0 ########################
    if(CNTNR_SS['processing']['Zd'] > 3.0):
        Boolobs[2] = True
    ####################### Pop > 7 ########################
    if(CNTNR_SS['mediation']['P'] > 7):
        Boolobs[3] = True
    ####################### FQ+ > 1 ########################
    if(CNTNR_SS['FQ']['FQx']['+'] > 1):
        Boolobs[4] = True


    ####################### Conditions 1 to 5 are True ########################


    if(sum(Boolobs[0:5]) == 5):
        Boolobs[5] = True
    ####################### (Two or more of 1 to 4 are True) and (FQ+ > 3)########################
    if (sum(Boolobs[0:4]) > 1 and
        CNTNR_SS['FQ']['FQx']['+'] > 3):
        Boolobs[6] = True
    ####################### (3 or more of 1 to 5 are True) and (X+% > 0.89)########################
    if (sum(Boolobs[0:5]) > 2 and
        (CNTNR_SS['mediation']['X+%'] > 0.89)):
        Boolobs[7] = True
    ####################### (FQ+ > 3) and (X+% > 0.89) ########################
    if(CNTNR_SS['FQ']['FQx']['+'] > 3 and
       CNTNR_SS['mediation']['X+%'] > 0.89):
        Boolobs[8] = True

def main(CNTNRin):
    global CNTNR_SS
    CNTNR_SS = CNTNRin

    scon()
    pti()
    depi()
    cdi()
    hvi()
    obs()
    return\
          {'SCON':Boolscon,
                'SUM_SCON':sum(Boolscon),
                    'POS_SCON':True if sum(Boolscon) > 7 else False,
           'PTI':Boolpti,
                'SUM_PTI':sum(Boolpti),
           'DEPI':Booldepi,
                'SUM_DEPI':sum(Booldepi),
                    'POS_DEPI': True if sum(Booldepi) > 4 else False,
           'CDI':Boolcdi,
                'SUM_CDI':sum(Boolcdi),
                    'POS_CDI': True if sum(Boolcdi) > 3 else False,
           'HVI':Boolhvi,
                'POS_HVI':True if Boolhvi[0] and sum(Boolhvi) - 1 > 3 else False,
           'OBS':Boolobs,
                'POS_OBS': True if (sum(Boolobs[0:5])>0)  else False,
           'FV+VF+V+FD':(arr['FV']+arr['VF']+arr['V'] +arr['FD']),
           'FV+VF+V':(arr['FV']+arr['VF']+arr['V']),
           'FD':arr['FD'],
           'Col-Shd':arr["Col-Shd"],
                'LIST_Col-Shd':arr["LIST_Col-Shd"],
           'FT+TF+T':arr['FT']+arr['TF']+arr['T'],
            'SUM_Blends':len(CNTNR_SS['determinants']['Blends'])
           }, arr

