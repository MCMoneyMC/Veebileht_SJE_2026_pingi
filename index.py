import math
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

print(kaalutud_keskmine(hinded, ainepunktid))
"""
siia lisame frontist aine hinded, ainepunktid ja soovitud hinne
"""
hinded = [5, 3, '']
ainepunktid = [6, 3, 6]
soovitud = 4
"""
seda kasutame kui on puuduv hinne
"""
def ennustaja(hinded, ainepunktid, soovitud):

    summa = 0
    ainepunktide_summa = 0
    puuduv_ainepunkt = 0
    
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
            puuduv_ainepunkt += ainepunktid[i]

    #print(summa, 'summa')
    #print(ainepunktide_summa, 'ainepunktide_summa')
    #print(puuduv_ainepunkt, 'puuduv_ainepunkt')
    """
    Leiame puuduva hinde: korrutame soovitud keskmise kõikide ainepunktide koguarvuga,
    lahutame sellest olemasolevate hinnete kaalutud summa
    ning jagame tulemuse puuduva aine ainepunktidega.
    """
    vajalik_hinne = (soovitud *
                      (ainepunktide_summa + puuduv_ainepunkt) - summa
                    ) / puuduv_ainepunkt
    """
    kasutan round, et leida kõrge vajalik hinne et soovitud hinde saada
    """
    if math.ceil(vajalik_hinne) > 5:
        return "soovitud pole võimalik saada"
    else:
        return math.ceil(vajalik_hinne)
    
print('ennustaja', ennustaja(hinded, ainepunktid, soovitud))