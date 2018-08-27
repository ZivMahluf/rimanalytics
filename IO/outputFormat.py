
'''
This File was used to create a .txt file as an output
not used when the date is outputed to the browser window
'''

import math
CNTNR_SS = {}
CNTNR_C = {}
CNTNR_arr = {}
CNTNR_IR = ' '
def saveTo(name, s):
    with open("session_DB/"+name+".txt","w+") as f:
        f.write(s)
    f.close()

def printlocFeatFirst():
    s = ""
    s+=("LOCATION FEATURES\n")
    s+=('Zf = ' + str(CNTNR_SS['locFeat']['Zf']) + '\n')
    s+=('ZSum = ' + str(CNTNR_SS['locFeat']['ZSum']) + '\n')
    s +=('ZEst = ' + str(CNTNR_SS['locFeat']['ZEst']) + '\n')
    return s

def printlocFeatSecond():
    s = ''
    name = ['W','D','W+D','Dd','S']
    for i in name:
        s+=(i +' = ' + str(CNTNR_SS['locFeat'][i]) + '\n')
    return s

def printlocFeatDQ():
    s = '\n'
    name = ['+','o','v/+','v']
    s+=('DQ\n')
    for i in name:
        s+=(i+' = ' + str(CNTNR_SS['locFeatDQ'][i])+'\n')
    return s
def printcontents():
    s = '\n'
    s+=('Contents\n')
    for i in CNTNR_SS['contents']:
        s+=(i+' = '+ str(CNTNR_SS['contents'][i])+'\n')
    return s
def printdeterminants():
    s = '\n'
    s+=("Determinants\n")
    s+=("Blends\n")
    for i in CNTNR_SS['determinants']['Blends']:
        s+=(str(i)+'\n')

    s+=("\nSingle\n")
    for i in (CNTNR_SS['determinants']['Single']):
        s+=(i+ ' = ' + str(CNTNR_SS['determinants']['Single'][i])+'\n')
    return s+"\n"
def printFQ():
    s = ''
    s += ('     FQx      MQual       W+D\n')
    s += ('+  =  ' + str(CNTNR_SS['FQ']['FQx']['+']) + '        ' + str(CNTNR_SS['FQ']['MQual']['+']) + '          ' + str(
        CNTNR_SS['FQ']['W+D']['+']) + '\n')
    s += ('o  =  ' + str(CNTNR_SS['FQ']['FQx']['o']) + '        ' + str(CNTNR_SS['FQ']['MQual']['o']) + '        ' + str(
        CNTNR_SS['FQ']['W+D']['o']) + '\n')
    s += ('u  =  ' + str(CNTNR_SS['FQ']['FQx']['u']) + '        ' + str(CNTNR_SS['FQ']['MQual']['u']) + '        ' + str(
        CNTNR_SS['FQ']['W+D']['u']) + '\n')
    s += ('-  =  ' + str(CNTNR_SS['FQ']['FQx']['-']) + '        ' + str(CNTNR_SS['FQ']['MQual']['-']) + '        ' + str(
        CNTNR_SS['FQ']['W+D']['-']) + '\n')
    s += ('none= ' + str(CNTNR_SS['FQ']['FQx']['none']) + '        ' + str(CNTNR_SS['FQ']['MQual']['none']) + '        ' + str(
        CNTNR_SS['FQ']['W+D']['none']) + '\n')
    return s
def printapproachSummary():
    arr =  CNTNR_SS['approachSummary']
    s=('Approach\n')
    s+=('I       '+str(arr[0])+'\n')
    s+=('II      ' + str(arr[1])+'\n')
    s+=('III     ' + str(arr[2])+'\n')
    s+=('IV      ' + str(arr[3])+'\n')
    s+=('V       ' + str(arr[4])+'\n')
    s+=('VI      ' + str(arr[5])+'\n')
    s+=('VII     ' + str(arr[6])+'\n')
    s+=('VIII    ' + str(arr[7])+'\n')
    s+=('IX      ' + str(arr[8])+'\n')
    s+=('X       ' + str(arr[9])+'\n')
    return s
def printspecialScores():
    s=("         SPECIAL SCORES\n")
    s+=('         Lv1            Lv2\n')
    s+=('DV   =  ' + str(CNTNR_SS['specialScores']['lvl1']['DV']) + ' x1           '+str(CNTNR_SS['specialScores']['lvl2']['DV']) + ' x1'+'\n')
    s+=('INC  =  ' + str(CNTNR_SS['specialScores']['lvl1']['INC']) + ' x1           '+str(CNTNR_SS['specialScores']['lvl2']['INC']) + ' x1'+'\n')
    s+=('DR   =  ' + str(CNTNR_SS['specialScores']['lvl1']['DR']) + ' x1           '+str(CNTNR_SS['specialScores']['lvl2']['DR']) + ' x1'+'\n')
    s+=('FAB  =  ' + str(CNTNR_SS['specialScores']['lvl1']['FAB']) + ' x1           '+str(CNTNR_SS['specialScores']['lvl2']['FAB']) + ' x1'+'\n')
    s+=('ALOG =  ' + str(CNTNR_SS['specialScores']['lvl1']['ALOG']) + ' x5'+'\n')
    s+=('CON  =  ' + str(CNTNR_SS['specialScores']['lvl1']['CON']) + ' x7'+'\n')
    s+=('\nRaw Sum6 = ' + str(CNTNR_SS['specialScores']['misc']['SUM6'])+'\n')
    s+=('WSum6 = ' + str(CNTNR_SS['specialScores']['misc']['WSUM6'])+'\n')
    s+=('\nAB  = ' + str(CNTNR_SS['specialScores']['misc']['AB'])+'\n')
    s+=('AG  = ' + str(CNTNR_SS['specialScores']['misc']['AG'])+'\n')
    s+=('COP = ' + str(CNTNR_SS['specialScores']['misc']['COP'])+'\n')
    s+=('CP  = ' + str(CNTNR_SS['specialScores']['misc']['CP'])+'\n')
    s+=('GHR = ' + str(CNTNR_SS['specialScores']['misc']['GHR'])+'\n')
    s+=('PHR = ' + str(CNTNR_SS['specialScores']['misc']['PHR'])+'\n')
    s+=('MOR = ' + str(CNTNR_SS['specialScores']['misc']['MOR'])+'\n')
    s+=('PER = ' + str(CNTNR_SS['specialScores']['misc']['PER'])+'\n')
    s+=('PSV = ' + str(CNTNR_SS['specialScores']['misc']['PSV'])+'\n')
    return s
def printcore():
    s = ("       R = "+str(CNTNR_SS['core']['R']) + " L = "+str(CNTNR_SS['core']['L'])+"\n")
    s +=("EB = " +str(CNTNR_SS['core']['EB'][0])+":"+str(CNTNR_SS['core']['EB'][1]))
    s += ("  EA = " +str(CNTNR_SS['core']['EA']))
    s += ("  EBPer = " +str(CNTNR_SS['core']['EBPer'])+"\n")
    s += ("eb = " + str(CNTNR_SS['core']['eb'][0]) + ":" + str(CNTNR_SS['core']['eb'][1]))
    s += ("    es = " + str(CNTNR_SS['core']['es']))
    s += ("    D = " + str(CNTNR_SS['core']['D']) + "\n")
    s += ("   Adj es = " + str(CNTNR_SS['core']['adjes']))
    s += ("  Adj D = " + str(CNTNR_SS['core']['adjD']) + "\n")
    s += ("       FM = "+str(CNTNR_SS['core']['FM']))
    s += ("   m = " + str(CNTNR_SS['core']['m'])+"\n")

    s += ("    SUM C' = " + str(CNTNR_SS['core']['C\'']))
    s += ("   SUM T = " + str(CNTNR_SS['core']['T']) + "\n")
    s += ("    SUM V  = " + str(CNTNR_SS['core']['V']))
    s += ("   SUM Y = " + str(CNTNR_SS['core']['Y']) + "\n")
    return s
def printideation():
    s = "\nIDEATION\n"
    s += 'a:p = ' + str(CNTNR_SS['ideation']['a:p'][0]) + ':' + str(CNTNR_SS['ideation']['a:p'][1])
    s += '   Sum6 = ' + str(CNTNR_SS['ideation']['SUM6']) + '\n'
    s += 'Ma:Mp = ' + str(CNTNR_SS['ideation']['Ma:Mp'][0]) + ':' + str(CNTNR_SS['ideation']['Ma:Mp'][1])
    s += '   Lvl2 = ' + str(CNTNR_SS['ideation']['lvl2']) + '\n'
    s += '2AB+(Art + Ay) = ' +str(CNTNR_SS['ideation']['INTELL'])
    s += '   WSum6 = ' + str(CNTNR_SS['ideation']['WSUM6']) + '\n'
    s += 'MOR = ' + str(CNTNR_SS['ideation']['MOR'])
    s += '   M- = '+ str(CNTNR_SS['ideation']['M-']) + '\n'
    s += 'Mnone = '+ str(CNTNR_SS['ideation']['Mnone']) + '\n'

    return s
def printaffect():
    s = '\nAFFECT\n'
    s += "FC:CF+C = {}:{}".format(CNTNR_SS['affect']['FC:CF+C'][0],CNTNR_SS['affect']['FC:CF+C'][1]) +'\n'
    s += "PureC = {}".format(CNTNR_SS['affect']['pureC'])+'\n'
    s += "SumC:WSumC = {}:{} ".format(CNTNR_SS['affect']['SumC\':WSumC'][0],CNTNR_SS['affect']['SumC\':WSumC'][1])+'\n'
    s += "Afr = {}".format(CNTNR_SS['affect']['Afr'])+'\n'
    s += "S = {}".format(CNTNR_SS['affect']['S'])+'\n'
    s +="Blends:R = {}:{}".format(CNTNR_SS['affect']['Blends:R'][0],CNTNR_SS['affect']['Blends:R'][1])+'\n'
    s +="CP = {}".format(CNTNR_SS['affect']['CP'])+'\n'
    return s
def printmediation():
    s='\n MEDIATION\n'
    s+="XA% = {}".format(CNTNR_SS['mediation']['XA%'])+'\n'
    s+="WDA% = {}".format(CNTNR_SS['mediation']['WDA%'])+'\n'
    s+="X-% = {}".format(CNTNR_SS['mediation']['X-%'])+'\n'
    s+="S- = {}".format(CNTNR_SS['mediation']['S-'])+'\n'
    s+="P = {}".format(CNTNR_SS['mediation']['P'])+'\n'
    s+="X+% ={}".format(CNTNR_SS['mediation']['X+%'])+'\n'
    s+="Xu% ={}".format(CNTNR_SS['mediation']['Xu%'])+'\n'
    return(s)
def printprocessing():
    s = "\nPROCESSING\n"
    s += "Zf = {}".format(CNTNR_SS['processing']['Zf'])+'\n'
    s += "W:D:Dd = {}:{}:{}".format(CNTNR_SS['processing']['W:D:Dd'][0], CNTNR_SS['processing']['W:D:Dd'][1], CNTNR_SS['processing']['W:D:Dd'][2])+'\n'
    s += "W:M = {}:{}".format(CNTNR_SS['processing']['W:M'][0],CNTNR_SS['processing']['W:M'][1])+'\n'
    s += "Zd = {}".format(CNTNR_SS['processing']['Zd'])+'\n'
    s += "PSV = {}".format(CNTNR_SS['processing']['PSV'])+'\n'
    s += "DQ+ = {}".format(CNTNR_SS['processing']['DQ+'])+'\n'
    s += "DQv = {}".format(CNTNR_SS['processing']['DQv'])+'\n'
    return s
def printinterpersonal():
    s = "\nINTERPERSONAL\n"
    s += "COP = {}  AG = {}\n".format(CNTNR_SS['interpersonal']['COP'],CNTNR_SS['interpersonal']['AG'])
    s += "GHR:PHR = {}:{}\n".format(CNTNR_SS['interpersonal']['GHR:PHR'][0], CNTNR_SS['interpersonal']['GHR:PHR'][1])
    s += "a:p = {}:{}\n".format(CNTNR_SS['interpersonal']['a:p'][0], CNTNR_SS['interpersonal']['a:p'][1])
    s += "Food = {}\n".format(CNTNR_SS['interpersonal']['Food'])
    s += "SumT = {}\n".format(CNTNR_SS['interpersonal']['SumT'])
    s += "Human Cont  = {}\n".format(CNTNR_SS['interpersonal']['H'])
    s += "Pure H      = {}\n".format(CNTNR_SS['interpersonal']['pureH'])
    s += "PER         = {}\n".format(CNTNR_SS['interpersonal']['PER'])
    s += "Isol Indx   = {}\n".format(CNTNR_SS['interpersonal']['isol'])
    return s
def printselfPerception():
    s= '\nSELF-PERCEPTION\n'
    s += "3r+(2)/R = {}\n".format(CNTNR_SS['selfPerception']['3r+(2)/R'])
    s += "Fr+rF = {}\n".format(CNTNR_SS['selfPerception']['Fr+rF'])
    s += "SumV = {}\n".format(CNTNR_SS['selfPerception']['SumV'])
    s += "FD = {}\n".format(CNTNR_SS['selfPerception']['FD'])
    s += "An+Xy = {}\n".format(CNTNR_SS['selfPerception']['An+Xy'])
    s += "MOR = {}\n".format(CNTNR_SS['selfPerception']['MOR'])
    s += "H:(H)+Hd+(Hd) = {}:{}\n".format(CNTNR_SS['selfPerception']['H:(H)+Hd+(Hd)'][0],
                                          CNTNR_SS['selfPerception']['H:(H)+Hd+(Hd)'][1])
    return s




'''                           CONSTELLATIONS SECTION                          '''



def printscon():
    s = ("\nS CON\n")
    s+=("Positive if 8 or more conditions are true\nNOTE: Applicable only for subjects over 14 years old.\n")
    s += ("({})FV+VF+V+FD ({}) > 2\n".format(CNTNR_C['SCON'][0],
                                             (CNTNR_arr['FV']+CNTNR_arr['VF']+
                                             CNTNR_arr['V'] +CNTNR_arr['FD'])))
    s += ("({})Col-Shd Blends ({}) > 0\n".format(CNTNR_C['SCON'][1],0))
    s += ("({})Ego({:.3f}) < .31 or > .44\n".format(CNTNR_C['SCON'][2],
                                                CNTNR_SS['selfPerception']['3r+(2)/R']))
    s += ("({})MOR({}) > 3\n".format(CNTNR_C['SCON'][3],
                                     CNTNR_SS['specialScores']['misc']['MOR']))
    s += ("({})Zd({}) > +-3.5\n".format(CNTNR_C['SCON'][4],
                                        CNTNR_SS['processing']['Zd']))
    s += ("({})es({}) > EA({})\n".format(CNTNR_C['SCON'][5],
                                         CNTNR_SS['core']['es'],
                                          CNTNR_SS['core']['EA']))
    s += ("({})CF + C({}) > FC ({})\n".format(CNTNR_C['SCON'][6],
                                              CNTNR_SS['affect']['FC:CF+C'][1],
                                              CNTNR_SS['affect']['FC:CF+C'][0]))
    s += ("({})X+%({:.3f}) < .70\n".format(CNTNR_C['SCON'][7],
                                       CNTNR_SS['mediation']['X+%']))
    s += ("({})S({}) > 3\n".format(CNTNR_C['SCON'][8],
                                   CNTNR_SS['locFeat']['S']))
    s += ("({})P({}) < 3 or > 8\n".format(CNTNR_C['SCON'][9],
                                          CNTNR_SS['mediation']['P']))
    s += ("({})Pure H({}) < 2\n".format(CNTNR_C['SCON'][10],
                                        CNTNR_SS['interpersonal']['pureH']))
    s += ("({})R({}) < 17\n".format(CNTNR_C['SCON'][11],
                                    CNTNR_SS['core']['R']))
    s += "{} Total\n".format(sum(CNTNR_C['SCON']))
    return s
def printpti():
    s = "\nPTI\n"
    s += "({})(XA%({:.3f})<0.70) and (WDA%({:.3f})]<0.75)\n".format(CNTNR_C['PTI'][0],
                                                            CNTNR_SS['mediation']['XA%'],
                                                            CNTNR_SS['mediation']['WDA%'])
    s += "({})X-%({:.3f})>0.29\n".format(CNTNR_C['PTI'][1],
                                     CNTNR_SS['mediation']['X-%'])
    s += "({})(Sum Level 2 Special Scores({}) > 2) and (FAB2({}) > 0)\n".format(CNTNR_C['PTI'][2],
                                                                                CNTNR_SS['ideation']['lvl2'],
                                                                                CNTNR_SS['specialScores']['lvl2']['FAB'])
    s +="({})((R({})<17) and (WSum6({}) > 12))\n or ((R({}) > 16) and (WSum6({}) > 17))\n".format(CNTNR_C['PTI'][3],
                                                                                                CNTNR_SS['core']['R'],
                                                                                                CNTNR_SS['ideation']['WSUM6'],
                                                                                                CNTNR_SS['core']['R'],
                                                                                                CNTNR_SS['ideation']['WSUM6'])
    s +="({})(M-({:.3f})> 1) or (X-%({:.3f}) > 0.40)\n".format(CNTNR_C['PTI'][4],
                                                       CNTNR_SS['ideation']['M-'],
                                                       CNTNR_SS['mediation']['X-%'])
    s +="{} Total\n".format(sum(CNTNR_C['PTI']))

    return s
def printdepi():
    s = "\nDEPI\n"
    s+="Positive if 5 or more conditions are true:\n"
    s += "({})(FV+VF+V({})>0) or (FD({})>2)\n".format(CNTNR_C['DEPI'][0],
                                                      CNTNR_arr['FV'] + CNTNR_arr['VF'] + CNTNR_arr['V'],
                                                      CNTNR_arr['FD'])
    s += "({})(Col-Shd Blends({})>0) or (S({})>2)\n".format(CNTNR_C['DEPI'][1],0,CNTNR_SS['locFeat']['S'])
    s += "({})(3r+(2)/R({:.3f})>0.44andFr+rF({})=0) or\n (3r+(2)/R({:.3f})<0.33)\n".format(CNTNR_C['DEPI'][2],
                                                                                   CNTNR_SS['selfPerception']['3r+(2)/R'],
                                                                                   CNTNR_SS['selfPerception']['Fr+rF'],
                                                                                   CNTNR_SS['selfPerception']['3r+(2)/R'])
    s += "({})(Afr({:.3f}) < 0.46) or (Blends({}) < 4)\n".format(CNTNR_C['DEPI'][3],
                                                             CNTNR_SS['affect']['Afr'],
                                                             len(CNTNR_SS['determinants']['Blends']))
    s += "({})(SumShading({}) > FM + m({}))or \n(SumC' ({}) > 2)\n".format(CNTNR_C['DEPI'][4],
                                                                           CNTNR_SS['core']['eb'][1],
                                                                           (CNTNR_SS['core']['FM'] + CNTNR_SS['core']['m']),
                                                                           CNTNR_SS['affect']['SumC\':WSumC'][0])
    s += "({})(MOR({}) > 2) or (INTELL)(2xAB + Art + Ay({}) > 3)\n".format(CNTNR_C['DEPI'][5],
                                                                   CNTNR_SS['specialScores']['misc']['MOR'],
                                                                   CNTNR_SS['ideation']['INTELL'])
    s += "({})(COP({}) < 2) or ([Bt + 2xCl + Ge + Ls + 2xNa] / R({:.3f}) > 0.24)\n".format(CNTNR_C['DEPI'][6],
                                                                                       CNTNR_SS['specialScores']['misc']['COP'],
                                                                                       CNTNR_SS['interpersonal']['isol'])
    s += "{} Total\n".format(sum(CNTNR_C['DEPI']))
    return s
def printcdi():
    s = "\nCDI\n"
    s += "(Positive if 4 or more conditions are true:\n"

    s += "({})(EA({}) < 6) or (AdjD({}) < 0)\n".format(CNTNR_C['CDI'][0],
                                                       CNTNR_SS['core']['EA'],
                                                       (CNTNR_SS['core']['adjD']))
    s += "({})(COP({}) < 2) and (AG({}) < 2)\n".format(CNTNR_C['CDI'][1],
                                                       CNTNR_SS['specialScores']['misc']['COP'],
                                                       CNTNR_SS['specialScores']['misc']['AG'])
    s += "({})(Weighted SumC({}) < 2.5)\n or (Afr({:.3f}) < 0.46)\n".format(CNTNR_C['CDI'][2],
                                                                        CNTNR_SS['affect']['SumC\':WSumC'][1],
                                                                        CNTNR_SS['affect']['Afr'])
    s += "({})((Passive({}) > Active + 1({})) or (PureH({}) < 2)\n".format(CNTNR_C['CDI'][3],
                                                                           CNTNR_SS['ideation']['a:p'][1],
                                                                           CNTNR_SS['ideation']['a:p'][0] + 1,
                                                                           CNTNR_SS['interpersonal']['pureH'])
    s += "({})((SumT({}) > 1)or \n(Isolate / R({:.3f}) > 0.24)or \n(Food({}) > 0)\n".format(CNTNR_C['CDI'][4],
                                                                                        CNTNR_SS['interpersonal']['SumT'],
                                                                                        CNTNR_SS['interpersonal']['isol'],
                                                                                        CNTNR_SS['interpersonal']['Food'])
    s += "{} Total\n".format(sum(CNTNR_C['CDI']))
    return s
def printhvi():
    s = "\nHVI\n"
    s += "Positive if condition 1 is true and at \nleast 4 of the others are true:\n"
    s += "({})(1)FT + TF + T({}) = 0\n".format(CNTNR_C['HVI'][0],
                                               CNTNR_arr['FT'] +
                                               CNTNR_arr['TF']+
                                               CNTNR_arr['T'])
    s += "({})(2)Zf({}) > 12\n".format(CNTNR_C['HVI'][1],
                                       CNTNR_SS['locFeat']['Zf'])
    s += "({})(3)Zd({}) > +3.5\n".format(CNTNR_C['HVI'][2],
                                         CNTNR_SS['processing']['Zd'])
    s += "({})(4)S({}) > 3\n".format(CNTNR_C['HVI'][3],
                                     CNTNR_SS['locFeat']['S'])
    s += "({})(5)H + (H) + Hd + (Hd)({}) > 6\n".format(CNTNR_C['HVI'][4],
                                                       CNTNR_SS['interpersonal']['H'])
    s += "({})(6)(H) + (A) + (Hd) + (Ad)({}) > 3\n".format(CNTNR_C['HVI'][5],
                                                           (CNTNR_SS['contents']['(H)'] +
                                                            CNTNR_SS['contents']['(A)'] +
                                                            CNTNR_SS['contents']['(Hd)'] +
                                                            CNTNR_SS['contents']['(Ad)']))
    s += "({})(7)H + A: Hd + Ad({}:{}) < 4: 1\n".format(CNTNR_C['HVI'][6],
                                                        CNTNR_SS['contents']['H'] + CNTNR_SS['contents']['A']+
                                                        CNTNR_SS['contents']['(H)'] + CNTNR_SS['contents']['(A)'],
                                                        CNTNR_SS['contents']['Hd'] + CNTNR_SS['contents']['Ad'] +
                                                        CNTNR_SS['contents']['(Hd)'] + CNTNR_SS['contents']['(Ad)'])
    s += "({})(8)Cg({}) > 3\n".format(CNTNR_C['HVI'][7],
                                      CNTNR_SS['contents']['Cg'])
    return s
def printobs():
    s = "\nOBS\n"
    s += "({})(1)Dd({})>3\n".format(CNTNR_C['OBS'][0],
                                    CNTNR_SS['locFeat']['Dd'])
    s += "({})(2)Zf({})>12\n".format(CNTNR_C['OBS'][1],
                                     CNTNR_SS['locFeat']['Zf'])
    s += "({})(3)Zd({})>+3.0\n".format(CNTNR_C['OBS'][2],
                                       CNTNR_SS['processing']['Zd'])
    s += "({})(4)Populars({})>7\n".format(CNTNR_C['OBS'][3],
                                          CNTNR_SS['mediation']['P'])
    s += "({})(5)FQ +({})>1\n".format(CNTNR_C['OBS'][4],
                                      CNTNR_SS['FQ']['FQx']['+'])
    s += "Positive if one or more is true:\n"
    s += "({})Conditions 1 to 5 are all true\n".format(CNTNR_C['OBS'][5])
    s += "({})Two or more of 1 to 4 are true and FQ+({})>3\n".format(CNTNR_C['OBS'][6],
                                                                     CNTNR_SS['FQ']['FQx']['+'])
    s += "({})3 or moreof 1 to 5 are true and X+%({:.3f})>0.89\n".format(CNTNR_C['OBS'][7],
                                                                     CNTNR_SS['mediation']['X+%'])
    s += "({})FQ+({})>3 and X+%({:.3f})>0.89\n".format(CNTNR_C['OBS'][8],
                                                   CNTNR_SS['FQ']['FQx']['+'],
                                                   CNTNR_SS['mediation']['X+%'])
    return s
def stringifyMeth():
    s =(printapproachSummary() +
        printlocFeatFirst() +
        printlocFeatSecond() +
        printlocFeatDQ() +
        printcontents() +
        printdeterminants() +
        printFQ() +
        printspecialScores() +
        printcore() +
        printideation() +
        printaffect() +
        printmediation() +
        printprocessing() +
        printinterpersonal() +
        printselfPerception() +
        "\nCONSTELLATIONS TABLE\n" +
        printscon() +
        printpti() +
        printdepi() +
        printcdi() +
        printhvi() +
        printobs() +
        "\nINTERPRETIVE REPORT\n" +
        CNTNR_IR)
    return s

def main(CNTNRStructuralSummary, CNTNRConstellationsBool, CNTNRarr, text):
    global CNTNR_SS
    CNTNR_SS = CNTNRStructuralSummary
    global CNTNR_C
    CNTNR_C = CNTNRConstellationsBool
    global CNTNR_arr
    CNTNR_arr = CNTNRarr
    global CNTNR_IR
    TEXT = text

    saveTo('out',stringifyMeth())