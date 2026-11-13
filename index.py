import math
import itertools
"""
siia lisame frontist aine hinded ja ainepunktid
"""
hinded = [5, 3]
ainepunktid = [6, 3]
"""
seda kasutame kui ei ole puuduvat hinnet
"""
def kaalutud_keskmine(hinded, ainepunktid):
    summa = 0
    ainepunktide_summa = 0

    for i in range(len(hinded)):
        """
        Kaalutud keskmise arvutamisel tuleb aga arvesse võtta ka ainepunktide arv (hinne x ainepunktid), mis tuleb läbi jagada ainepunktide koguarvuga.
        link: https://ut.ee/et/sisu/keskmine-hinne
        """
        #print(i)
        #print(hinded[i], 'hinded')
        #print(ainepunktid[i], 'ainepunktid')

        summa += hinded[i] * ainepunktid[i]
        ainepunktide_summa += ainepunktid[i]

    #print(summa)
    #print(ainepunktide_summa)
    """
    ei kasuta round, kuna me tahame leida ümardada 0.1 kohalt allapoole, mitte lähima ujukomaarvuni (vt: "Kaalutud Keskmine hinne" näide)
    """
    return int((summa / ainepunktide_summa) * 10) / 10

#print(kaalutud_keskmine(hinded, ainepunktid))
"""
seda kasutame kui on puuduv hinne semester vaates
"""
def ennustaja(hinded, ainepunktid, soovitud):

    summa = 0
    ainepunktide_summa = 0
    #puuduv_ainepunkt = 0
    puuduvad = []
    #puuduvate_ainepunkt = []
    sobivad = []
    
    for i in range(len(hinded)):
        if hinded[i] != '':
            """
            Kaalutud keskmise arvutamisel tuleb aga arvesse võtta ka ainepunktide arv (hinne x ainepunktid), mis tuleb läbi jagada ainepunktide koguarvuga.
                
            link: https://ut.ee/et/sisu/keskmine-hinne
            """
                #print(i)
                #print(hinded[i], 'hinded')
                #print(ainepunktid[i], 'ainepunktid')
        
            summa += hinded[i] * ainepunktid[i]
            ainepunktide_summa += ainepunktid[i]
        
            #print(summa)
            #print(ainepunktide_summa)
        else:
            """
            kui hinne on tühi, siis läheb siia
            """
            #puuduv_ainepunkt += ainepunktid[i]
            puuduvad.append(i)
            #puuduvate_ainepunkt.append(ainepunktid[i])
            #print(ainepunktid[i], 'aine')

    puuduv_ap = sum(ainepunktid[i] for i in puuduvad)
    kogu_ap = ainepunktide_summa + puuduv_ap
    #print(summa, 'summa')
    #print(ainepunktide_summa, 'ainepunktide_summa')
    #print(puuduv_ainepunkt, 'puuduv_ainepunkt')
    """
    Proovime kõiki puuduvaid hindeid vahemikus 1-5
    """
    kombinatsioonid = itertools.product(range(1, 6), repeat=len(puuduvad))

    väiksem_summa = 0
        
    for kombinatsioon in kombinatsioonid:
        #print(kombinatsioon)
        uus_summa = summa
        uus_ap = []
        """
        loopime kõik puuduvad hinded läbi, ja lisame uuele summale kombinatsioon hinne ja selle ainepunkt
        """
        for j in range(len(puuduvad)):
            uus_summa += kombinatsioon[j] * ainepunktid[puuduvad[j]]
            #print(ainepunktid[puuduvad[j]])
            uus_ap.append(ainepunktid[puuduvad[j]])
            
        keskmine = int((uus_summa / kogu_ap) * 10) / 10

        """
        Kui keskmine on suurem või võrdne kui soovitud ja "väiksem_summa" on tühi või leiame väiksem_summa abil,
        mis on kõige väiksemad hinded ja nende ainepunktid, millega saab soovitud hinnet,
        siis lisame või muudame "sobivad" väärtust
        """
        if keskmine >= soovitud:
            if väiksem_summa == 0 or uus_summa < väiksem_summa:
                #print(uus_summa, väiksem_summa, keskmine, uus_ap)
                sobivad = list(zip(kombinatsioon, uus_ap))
                #sobivad.append(kombinatsioon)
                väiksem_summa = uus_summa

    if not sobivad:
        return "soovitud hinne pole võimalik saada"

    return sobivad

    #"""
    #Leiame puuduva hinde: korrutame soovitud keskmise kõikide ainepunktide koguarvuga,
    #lahutame sellest olemasolevate hinnete kaalutud summa
    #ning jagame tulemuse puuduva aine ainepunktidega.
    #"""
    #vajalik_hinne = (soovitud * (ainepunktide_summa + puuduv_ainepunkt) - summa ) / puuduv_ainepunkt
    #"""
    #kasutan round, et leida kõrge vajalik hinne et soovitud hinde saada
    #"""
    #if math.ceil(vajalik_hinne) > 5:
    #    return "soovitud pole võimalik saada"
    #else:
    #    return math.ceil(vajalik_hinne)

"""
siia lisame frontist aine hinded, ainepunktid ja soovitud hinne
"""
hinded = [3, '', '', '']
ainepunktid = [6, 3, 3, 6]
soovitud = 4
    
print(ennustaja(hinded, ainepunktid, soovitud))
"""
seda kasutame kui on puuduv hinne oppekava vaates
"""
def üld_ennustaja(hinded_list, ainepunktid_list, soovitud):
    summa = 0
    ainepunktide_summa = 0
    #puuduv_ainepunkt = 0
    puuduvad = []
    sobivad = []
    for hinded, ainepunktid in zip(hinded_list, ainepunktid_list):
        for i in range(len(hinded)):
                if hinded[i] != '':
                    """
                    Kaalutud keskmise arvutamisel tuleb aga arvesse võtta ka ainepunktide arv (hinne x ainepunktid), mis tuleb läbi jagada ainepunktide koguarvuga.
                        
                    link: https://ut.ee/et/sisu/keskmine-hinne
                    """
                        #print(i)
                        #print(hinded[i], 'hinded')
                        #print(ainepunktid[i], 'ainepunktid')

                    summa += hinded[i] * ainepunktid[i]
                    ainepunktide_summa += ainepunktid[i]
                
                    #print(summa)
                    #print(ainepunktide_summa)
                else:
                    """
                    kui hinne on tühi, siis läheb siia
                    """
                    #puuduv_ainepunkt += ainepunktid[i]
                    puuduvad.append(ainepunktid[i])

    puuduv_ap = sum(puuduvad)
    kogu_ap = ainepunktide_summa + puuduv_ap
        #print(summa, 'summa')
        #print(ainepunktide_summa, 'ainepunktide_summa')
        #print(puuduv_ainepunkt, 'puuduv_ainepunkt')
    """
    Proovime kõiki puuduvaid hindeid vahemikus 1-5
    """
    kombinatsioonid = itertools.product(range(1, 6), repeat=len(puuduvad))

    väiksem_summa = 0
    
    for kombinatsioon in kombinatsioonid:
        #print(kombinatsioon)
        uus_summa = summa
        uus_ap = []
        """
        loopime kõik puuduvad hinded läbi, ja lisame uuele summale kombinatsioon hinne ja selle ainepunkt
        """
        for j in range(len(puuduvad)):
            uus_summa += kombinatsioon[j] * puuduvad[j]
            #print(ainepunktid[puuduvad[j]])
            uus_ap.append(puuduvad[j])
        
        keskmine = int((uus_summa / kogu_ap) * 10) / 10
        """
        Kui keskmine on suurem või võrdne kui soovitud ja "väiksem_summa" on tühi või leiame väiksem_summa abil,
        mis on kõige väiksemad hinded ja nende ainepunktid, millega saab soovitud hinnet,
        siis lisame või muudame "sobivad" väärtust
        """
        if keskmine >= soovitud:
            if väiksem_summa == 0 or uus_summa < väiksem_summa:
                #print(uus_summa, väiksem_summa, keskmine, uus_ap)
                sobivad = list(zip(kombinatsioon, uus_ap))
                #sobivad.append(kombinatsioon)
                väiksem_summa = uus_summa
        
    if not sobivad:
        return "soovitud hinne pole võimalik saada"
        
    return sobivad

hinded_list = [[5, '', ''], [5, '', ''], [5, 3, '', '']]
ainepunktid_list = [[6, 6, 6], [6, 6, 6], [6, 6, 6, 3]]
soovitud = 4

print(üld_ennustaja(hinded_list, ainepunktid_list, soovitud))