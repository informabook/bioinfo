 
def is_adn(s):

    s = s.lower()

    count = 0
    lettre_a_verifier = ['a','t','c','g']

    for i in s:

        for lettre in lettre_a_verifier:

            if i == lettre :
                
                count += 1

    if count == len(s):
        print(f"{s} is adn")
        return True
    else : 
        print(f"{s} is not adn")
        return False

def positions(s,p):
    s = s.lower()
    p = p.lower()
    liste_s =[]
    liste_p = []

    for i in s :
        liste_s.append(i)

    for i in p:
        liste_p.append(i)

    size_patern = len(liste_p)
    occurences = []
    occurences_1 = []

    count = 0

    for x in liste_s:
        if x == liste_p[0] :
           occurences_1.append(count)

        count += 1

    for x in occurences_1 :
        try:
            for i in range(1,size_patern):
                if liste_p[i] == liste_s[x+i]:
                    print(f"une occurence trouvée en {x}")
                    occurences.append(x)
        except:
            print("fin de liste")




    print(f"occurences trouvées en : {occurences}")
    return(occurences)

def distance_h(t1,t2):
    if len(t1) != len(t2):
        return None

    t1 = t1.lower()
    t2 = t2.lower()

    t1_list = []
    t2_list = []

    count = 0

    for i in t1 :
        t1_list.append(i)
    for i in t2:
        t2_list.append(i)

    for x in range(len(t1)):
        if t1_list[x] == t2_list[x]:
            pass
        else : 
            count += 1

    print(f"distance de {count} trouvée")
    return count


def distances_matrices(l):
    M = []
    for x in l:
        element = []
        for i in l:

            result = distance_h(x,i)
            element.append(result)

        M.append(element)    

    print(M)
    return M


text = "acgac"
is_adn(text)

positions("ACGACCG", "cg")

distance_h("AT","AG")

liste = ["AG", "AT", "GT", "ACG", "ACT" ]

distances_matrices(liste)