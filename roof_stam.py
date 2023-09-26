import streamlit as st
def roof_vent(key1, key2="Н"):
    stam_addons = {}
    KroStamRazmer = {'035':'35',
                     '040':'40',
                     '045':'45',
                     '050':'51',
                     '056':'56',
                     '063':'63',
                     '071':'71',
                     '080':'88',
                     '090':'90',
                     '100':'109',
                     '112':'112',
                     '125':'136'
                    }
    KroStamVent = {'Н':'Н',
                'В':'Н',
                'ВС':'Н',
                'К1':'К1',
                'ВК1':'К1',
                'ВСК1':'К1',
                }
    StamKlapanTypeVent = {'Н':'Н',
                    'В':'В',
                    'ВС':'В',
                    'К1':'К',
                    'ВК1':'КВ',
                    'ВСК1':'КВ'
                    }
    type_privod = {'Н':'',
                'В':'ЭПВ',
                'К':'',
                'КВ':'ЭПВ'
                }
    nmklapanregular = {'35':'350',
                '40':['LF','S'],
                '45':['LF','S'],
                '51':['LF','S'],
                '56':['LF','S'],
                '63':['LF','S'],
                '71':['NF','S2'],
                '88':['NF','S2'],
                '90':['NF','S2'],
                '109':['NF','S2'],
                '112':['NF','S2'],
                '136':['SF','S2']
                }
    nmklapangermik = {'35':'350',
                '40':['LF','S'],
                '45':['LF','S'],
                '51':['LF','S'],
                '56':['LF','S'],
                '63':['LF','S'],
                '71':['LF','S'],
                '88':['NF','S2'],
                '90':['NF','S2'],
                '109':['NF','S2'],
                '112':['SF','S2'],
                '136':['SF','S2']
                }


    KlapanVent = {'Н':'Н',
                'К1':'К',
                }
    KlapanStam = {'35':'350',
                '40':'400',
                '45':'450',
                '51':'500',
                '56':'550',
                '63':'600',
                '71':'700',
                '88':'850',
                '90':'900',
                '109':'1050',
                '112':'1100',
                '136':'1350'
                }

    POD = {'35':'50',
        '40':'50',
        '45':'50',
        '51':'84',
        '56':'84',
        '63':'84',
        '71':'93',
        '88':'93',
        '90':'93',
        '109':'137',
        '112':'137',
        '136':'137',
        }

    type_razmer = KroStamRazmer[key1]
    type_vent   = KroStamVent[key2]

    KroStams = [f'СТАМ-100-{type_razmer}-{type_vent}',
                    f'СТАМ-102-{type_razmer}-{type_vent}',
                    f'СТАМ-110-{type_razmer}-{type_vent}',
                    f'СТАМ-112-{type_razmer}-{type_vent}',
                    f'СТАМ-200-{type_razmer}-{type_vent}',
                    f'СТАМ-202-{type_razmer}-{type_vent}',
                    f'СТАМ-210-{type_razmer}-{type_vent}',
                    f'СТАМ-211-{type_razmer}-{type_vent}',
                    f'СТАМ-212-{type_razmer}-{type_vent}',
                    f'СТАМ-400-{type_razmer}-{type_vent}',
                    f'СТАМ-401-{type_razmer}-{type_vent}',
                    f'СТАМ-402-{type_razmer}-{type_vent}',
                    f'СТАМ-404-{type_razmer}-{type_vent}',
                    f'СТАМ-405-{type_razmer}-{type_vent}',
                    f'СТАМ-410-{type_razmer}-{type_vent}',
                    f'СТАМ-411-{type_razmer}-{type_vent}',
                    f'СТАМ-412-{type_razmer}-{type_vent}',
                    f'СТАМ-414-{type_razmer}-{type_vent}',
                    f'СТАМ-415-{type_razmer}-{type_vent}',
                    f'СТАМ-500-{type_razmer}-{type_vent}',
                    f'СТАМ-502-{type_razmer}-{type_vent}',
                    f'СТАМ-610-{type_razmer}-{type_vent}',
                    f'СТАМ-700-{type_razmer}-{type_vent}',
                    f'СТАМ-710-{type_razmer}-{type_vent}']

    stam_addons[KroStams[0]] = stam_addons[KroStams[4]] = [f'Поддон ПОД-{POD[type_razmer]}-Ц',
    f'Поддон ПОД-{POD[type_razmer]}-Н',
    'Сетка антивандальная',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Ц',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Н',
    f'ДЕФЛЕКТОР-{type_razmer}-Ц',
    f'ДЕФЛЕКТОР-{type_razmer}-Н',
    'Клапан ГЕРМИК/РЕГУЛЯР/ТЮЛЬПАН']


    stam_addons[KroStams[2]] = stam_addons[KroStams[1]] = stam_addons[KroStams[3]] = stam_addons[KroStams[5]] = stam_addons[KroStams[6]] = stam_addons[KroStams[8]] = [f'Поддон ПОД-{POD[type_razmer]}-Ц',
    f'Поддон ПОД-{POD[type_razmer]}-Н',
    'Сетка антивандальная',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Ц',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Н',
    f'ДЕФЛЕКТОР-{type_razmer}-Ц',
    f'ДЕФЛЕКТОР-{type_razmer}-Н']


    stam_addons[KroStams[9]] = [f'Поддон ПОД-{POD[type_razmer]}-Ц',
    f'Поддон ПОД-{POD[type_razmer]}-Н',
    'Сетка антивандальная',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Ц',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Н',
    f'ДЕФЛЕКТОР-{type_razmer}-Ц',
    f'ДЕФЛЕКТОР-{type_razmer}-Н',
    'Клапан КПУ/ГЕРМИК-ДУ/ПРОК']

    stam_addons[KroStams[10]] = stam_addons[KroStams[11]] = stam_addons[KroStams[12]] = stam_addons[KroStams[13]] = stam_addons[KroStams[14]] = stam_addons[KroStams[15]] = stam_addons[KroStams[16]] = stam_addons[KroStams[17]] = stam_addons[KroStams[18]] = [f'Поддон ПОД-{POD[type_razmer]}-Ц',
    f'Поддон ПОД-{POD[type_razmer]}-Н',
    'Сетка антивандальная',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Ц',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Н',
    f'ДЕФЛЕКТОР-{type_razmer}-Ц',
    f'ДЕФЛЕКТОР-{type_razmer}-Н']

    stam_addons[KroStams[19]] = [f'Поддон ПОД-{POD[type_razmer]}-Ц',
    f'Поддон ПОД-{POD[type_razmer]}-Н',
    'Сетка антивандальная',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Ц',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Н',
    f'ДЕФЛЕКТОР-{type_razmer}-Ц',
    f'ДЕФЛЕКТОР-{type_razmer}-Н',
    'Клапан КПУ/ГЕРМИК-ДУ/ПРОК']

    stam_addons[KroStams[20]] = [f'Поддон ПОД-{POD[type_razmer]}-Ц',
    f'Поддон ПОД-{POD[type_razmer]}-Н',
    'Сетка антивандальная',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Ц',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Н',
    f'ДЕФЛЕКТОР-{type_razmer}-Ц',
    f'ДЕФЛЕКТОР-{type_razmer}-Н']

    stam_addons[KroStams[21]] = [f'Поддон ПОД-{POD[type_razmer]}-Ц',
                    f'Поддон ПОД-{POD[type_razmer]}-Н',
    'Сетка антивандальная',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Ц',
    f'Защита ЗОНТ-СТАМ-{type_razmer}-Н',
    f'ДЕФЛЕКТОР-{type_razmer}-Ц',
    f'ДЕФЛЕКТОР-{type_razmer}-Н',
    'Клапан ГЕРМИК/РЕГУЛЯР/ТЮЛЬПАН']



    klapan = [f'РЕГУЛЯР-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapanregular[type_razmer][0]}230-{nmklapanregular[type_razmer][1]}-V-УХЛ2-0', 
            f'РЕГУЛЯР-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapanregular[type_razmer][0]}230-{nmklapanregular[type_razmer][1]}-V-К-УХЛ2-0', 
            f'РЕГУЛЯР-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapanregular[type_razmer][0]}24-{nmklapanregular[type_razmer][1]}-V-УХЛ2-0', 
            f'РЕГУЛЯР-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapanregular[type_razmer][0]}24-{nmklapanregular[type_razmer][1]}-V-К-УХЛ2-0',

            f'ГЕРМИК-П-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}230-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',
            f'ГЕРМИК-П-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}230-{nmklapangermik[type_razmer][1]}-V-К-УХЛ2-0',
            f'ГЕРМИК-П-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}24-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',
            f'ГЕРМИК-П-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}24-{nmklapangermik[type_razmer][1]}-V-К-УХЛ2-0',

            f'ГЕРМИК-П-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-Ц-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}230-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',
            f'ГЕРМИК-П-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-Ц-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}24-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',

            f'ГЕРМИК-П-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-ВЦ-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}230-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',
            f'ГЕРМИК-П-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-ВЦ-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}24-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',

            f'ГЕРМИК-П-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-ВЦ-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}230-{nmklapangermik[type_razmer][1]}-V-К-УХЛ2-0',
            f'ГЕРМИК-П-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-ВЦ-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}24-{nmklapangermik[type_razmer][1]}-V-К-УХЛ2-0',

            f'ГЕРМИК-С-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}230-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',
            f'ГЕРМИК-С-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}230-{nmklapangermik[type_razmer][1]}-V-К-УХЛ2-0',
            f'ГЕРМИК-С-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}24-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',
            f'ГЕРМИК-С-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}24-{nmklapangermik[type_razmer][1]}-V-К-УХЛ2-0',

            f'ГЕРМИК-С-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-Ц-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}230-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',
            f'ГЕРМИК-С-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-Ц-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}24-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',

            f'ГЕРМИК-С-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-ВЦ-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}230-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',
            f'ГЕРМИК-С-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-ВЦ-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}24-{nmklapangermik[type_razmer][1]}-V-УХЛ2-0',

            f'ГЕРМИК-С-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-ВЦ-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}230-{nmklapangermik[type_razmer][1]}-V-К-УХЛ2-0',
            f'ГЕРМИК-С-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-ВЦ-1*{type_privod[StamKlapanTypeVent[key2]]}{nmklapangermik[type_razmer][0]}24-{nmklapangermik[type_razmer][1]}-V-К-УХЛ2-0',

            f'ТЮЛЬПАН-2-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-{StamKlapanTypeVent[key2]}-0']
    klapanDY = [f'ГЕРМИК-ДУ-З-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-2*Ф-MV220-СН-0-0-0-0',
                f'ПРОК-2-{KlapanVent[type_vent]}-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-0',
                f'КПУ-1Н-З-{KlapanVent[type_vent]}-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-2*Ф-MV220-СН-0-0-0-0-0-0',
                f'КПУ-2Н-З-{KlapanVent[type_vent]}-{KlapanStam[type_razmer]}*{KlapanStam[type_razmer]}-2*Ф-MV220-СН-0-0-0-0-0-0']

    if type_privod[StamKlapanTypeVent[key2]] == '':
        klapan = [klapan[i] for i in range(len(klapan)) if not i in [1,3,5,7,10,11,12,13,15,17,20,21,22,23]]
    elif type_privod[StamKlapanTypeVent[key2]] != '':
        klapan = [klapan[i] for i in range(len(klapan)) if not i in [8,9,18,19]]

    KroStams = {item: {} for item in KroStams}
    import streamlit as st
    for key in stam_addons.keys():
        n_adds = []
        for item in stam_addons[key]:
            if item == "Клапан КПУ/ГЕРМИК-ДУ/ПРОК":
                n_adds.append(klapanDY)
            elif item == "Клапан ГЕРМИК/РЕГУЛЯР/ТЮЛЬПАН":
                n_adds.append(klapan)
            else:
                n_adds.append(item)
        KroStams[key] = n_adds
    return {"стакан монтажный": KroStams}

a = st.selectbox("Выберите типоразмер колеса", options=('035','040','045','050','056','063','071','080','090','100','112','125'))
st.write('Варианты стаканов')
st.table({"Номенклатура": list(roof_vent(a)['стакан монтажный'].keys())})