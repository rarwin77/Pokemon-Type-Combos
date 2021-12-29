bug = [['psychic','grass','dark'],['fight','grass','ground'],['fight','fire','flying','ghost','poison','steel','fairy'],
           ['fire','flying','rock'],['none'],['none'],['bug']]
    
electric = [['flying','water'],['electric','flying','steel'],['dragon','electric','grass'],['ground'],['ground'],['none'],['electric']]

fire = [['bug','grass','ice','steel'],['bug','fairy','fire','grass','ice','steel'],['dragon','fire','rock','water'],
            ['ground','rock','water'],['none'],['none'],['fire']]

grass = [['ground','rock','water'],['electric','grass','ground','water'],['bug','dragon','fire','flying','grass','poison',
            'steel'],['bug','fire','flying','ice','poison'],['none'],['none'],['grass']]

normal = [[''],[''],['rock','steel'],['fight'],['ghost'],['ghost'],['normal']]

rock = [['bug','fire','flying','ice'],['fire','flying','normal','poison'],['fight','ground','steel'],['fight','grass','ground',
            'steel','water'],['none'],['none'],['rock']]

dark = [['ghost','psychic'],['dark','ghost'],['dark','fight','fairy'],['bug','fight','fairy'],['none'],['psychic'],['dark']]

fairy = [['dark','dragon','fight'],['bug','dark','fight'],['fire','poison','steel'],['poison','steel'],['none'],['dragon'],['fairy']]

flying = [['bug','fight','grass'],['bug','fight','grass'],['electric','rock','steel'],['electric','ice','rock'],['none'],['ground'],['flying']]

ground = [['electric','fire','poison','rock','steel'],['poison','rock'],['bug','grass'],['grass','ice','water'],['flying'],['electric'],['ground']]

poison = [['grass','fairy'],['bug','fairy','fight','grass','poison'],['ghost','ground','poison','rock'],['ground','psychic'],
              ['steel'],['none'],['poison']]

steel = [['fairy','ice','rock'],['bug','dragon','fairy','flying','grass','ice','normal','psychic','rock','steel'],
             ['electric','fire','steel','water'],['fight','fire','ground'],['none'],['poison'],['steel']]

dragon = [['dragon'],['electric','fire','grass','water'],['steel'],['dragon','ice','fairy'],['fairy'],['none'],['dragon']]

fighting = [['dark','ice','normal','rock','steel'],['bug','dark','rock'],['bug','fairy','flying','poison','psychic'],
                ['fairy','flying','psychic'],['ghost'],['none'],['fighting']]

ghost = [['ghost','psychic'],['bug','posion'],['dark'],['ghost','dark'],['normal'],['normal','fight'],['ghost']]

ice = [['dragon','flying','grass','ground'],['ice'],['fire','ice','steel','water'],['fight','fire','rock','steel'],['none'],['none'],['ice']]

psychic = [['fight','poison'],['fight','psychic'],['psychic','steel'],['bug','dark','ghost'],['dark'],['none'],['psychic']]

water = [['fire','ground','rock'],['fire','ice','steel','water'],['dragon','grass','water'],['electric','grass'],['none'],['none'],['water']]
#types data

def TypeAnalyzer(type1,type2):
    print('Type combo of:',type1[6],type2[6],'\n')
    from collections import Counter
    double_damage_to = []
    half_damage_from = []
    fourth_damage_from = []
    half_damage_to = []
    double_damage_from = []
    quadruple_damage_from = []
    cant_damage1 = []
    cant_damage2 = []
    immune_to = []
    


    c1 = Counter(type2[0])
    c2 = Counter(type2[1])
    c3 = Counter(type2[2])
    c4 = Counter(type2[3])
    c5 = Counter(type2[4])
    c6 = Counter(type2[5])

    type1c4 = Counter(type1[3])
    type1c2 = Counter(type1[1])

    #Don't 100% understand counter, but it seems to work

    print(str(type1[6]) + ' attacks deal 2x damage to:', str(type1[0]),'\n'+
          'and deal half damage to:',str(type1[2])+'\n'+"and can't damage:",
          str(type1[4])+'\n')
    print(str(type2[6]) + ' attacks deal 2x damage to:', str(type2[0]),'\n'+
          'and deal half damage to:',str(type2[2])+'\n'+"and can't damage:",
          str(type2[4])+'\n')
    
    for types in type1[1]:
        if (c2.get(types,0)) != 1:
            half_damage_from.append(types)
    for types in type2[1]:
        if (type1c2.get(types,0)) != 1:
            half_damage_from.append(types)
    if fourth_damage_from == []:
        fourth_damage_from.append('none')
    print('Half damage from:',half_damage_from,'\n'+
          'Fourth damage from:',fourth_damage_from)

    for types in type1[5]:
        if (c6.get(types,0)) != 1:
            if types != 'none':
                immune_to.append(types)
            else:
                pass
    for types in type2[5]:
        if types == 'none' and immune_to != 'none':
            pass
        if types == 'none' and immune_to == 'none':
            pass
        else:
            immune_to.append(types)
    print('Immune to:',immune_to,'\n')
    

    for types in type1[3]:
        if (c4.get(types,0)) == 1:
            quadruple_damage_from.append(types)
        if (c4.get(types,0)) != 1:
            double_damage_from.append(types)
    for types in type2[3]:
        if (type1c4.get(types,0)) != 1:
            double_damage_from.append(types)
    if quadruple_damage_from == []:
        quadruple_damage_from.append('none')
    print('Double damage from:',double_damage_from,'\n'+
          'Quadruple damage from:',quadruple_damage_from)

    


        

    
TypeAnalyzer(fighting,grass)
