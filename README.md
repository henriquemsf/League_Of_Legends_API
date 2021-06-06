# League_Of_Legends_API
Airflow project that uses Riot Games API to retrieve the data from the recent matches that the player has played

# Riot Games API

In this project, 3 APIs were used:

- ACCOUNT-V1 - Get account by puuid
  - https://developer.riotgames.com/apis#account-v1/GET_getByPuuid

- MATCH-V5 - Get a list of match ids by puuid
  - https://developer.riotgames.com/apis#match-v5/GET_getMatchIdsByPUUID
- MATCH-V5 - Get a match by match id
  - https://developer.riotgames.com/apis#match-v5/GET_getMatch

# Result

This is an example of what the data generated should look like:

|    | GameMode   |   Duration |     Timestamp | Win   | Champion     |   Kills |   Deaths |   Assists |   Vision_Score |   Pink_Wards |
|---:|:-----------|-----------:|--------------:|:------|:-------------|--------:|---------:|----------:|---------------:|-------------:|
|  0 | ARAM       |     844562 | 1622947243708 | True  | Lucian       |      14 |        5 |        21 |              0 |            0 |
|  1 | CLASSIC    |    1837802 | 1622944769945 | True  | Nami         |       1 |        2 |        28 |             65 |            9 |
|  2 | CLASSIC    |    1710255 | 1622938698659 | True  | Rakan        |       3 |        1 |         9 |             58 |            6 |
|  3 | CLASSIC    |    1674367 | 1622930940408 | False | Nami         |       1 |        4 |        11 |             54 |            5 |
|  4 | ARAM       |    1288984 | 1622924821815 | False | Kennen       |      14 |        8 |        20 |              0 |            0 |
|  5 | CLASSIC    |    1647799 | 1622858339807 | True  | Lulu         |       0 |        4 |        15 |             59 |           10 |
|  6 | CLASSIC    |    1231121 | 1622855684031 | False | Nami         |       2 |        3 |         5 |             24 |            5 |
|  7 | ARAM       |    1040932 | 1622838182009 | False | Veigar       |       7 |       12 |        14 |              0 |            0 |
|  8 | ARAM       |    1368623 | 1622836577634 | False | Kayle        |      11 |       13 |        25 |              0 |            0 |
|  9 | ARAM       |    1372445 | 1622769806407 | False | Jayce        |       7 |       11 |        29 |              0 |            0 |
| 10 | CLASSIC    |    2309165 | 1622693644327 | False | Rakan        |       2 |        4 |        15 |             88 |           12 |
| 11 | ARAM       |     760216 | 1622691949169 | True  | Nami         |       3 |        3 |        20 |              0 |            0 |
| 12 | ARAM       |    1461981 | 1622667066752 | False | Taliyah      |      14 |        9 |        23 |              0 |            0 |
| 13 | CLASSIC    |    2308269 | 1622266137769 | False | Lucian       |       4 |        7 |        11 |             28 |            2 |
| 14 | CLASSIC    |    2022437 | 1622263621638 | True  | Lulu         |       3 |        3 |        21 |             84 |            7 |
| 15 | CLASSIC    |    1564352 | 1622261641843 | True  | Nami         |       6 |        1 |        22 |             53 |            8 |
| 16 | CLASSIC    |     942547 | 1622260327801 | True  | Thresh       |       1 |        0 |         9 |             17 |            4 |
| 17 | CLASSIC    |    1805789 | 1622258119405 | True  | Rakan        |       3 |        2 |        21 |             71 |           10 |
| 18 | ARAM       |    1523999 | 1622255192822 | True  | Elise        |      15 |       11 |        21 |              0 |            0 |
| 19 | ARAM       |    1403994 | 1622252878943 | True  | Taliyah      |      13 |       11 |        19 |              0 |            0 |
| 20 | NEXUSBLITZ |     700288 | 1622251787473 | True  | Kayn         |       2 |        0 |        11 |              2 |            0 |
| 21 | ARAM       |    1096204 | 1622250271601 | True  | Velkoz       |       4 |        9 |        22 |              0 |            0 |
| 22 | ARAM       |    1406603 | 1622164016560 | True  | Bard         |      19 |       11 |        25 |              0 |            0 |
| 23 | ARAM       |    1114160 | 1622162506577 | True  | Nautilus     |       4 |        9 |        30 |              0 |            0 |
| 24 | ARAM       |    1162193 | 1622161166326 | True  | Bard         |       2 |        7 |        40 |              0 |            0 |
| 25 | ARAM       |     943698 | 1622079693711 | True  | Annie        |       8 |        7 |        26 |              0 |            0 |
| 26 | ARAM       |     981599 | 1622078443346 | False | Gangplank    |       4 |        6 |        20 |              0 |            0 |
| 27 | ARAM       |    1558917 | 1621994223600 | True  | Varus        |      19 |       12 |        34 |              0 |            0 |
| 28 | ARAM       |    1064479 | 1621993009432 | True  | Ahri         |       7 |        8 |        20 |              0 |            0 |
| 29 | ARAM       |    1096545 | 1621903978775 | True  | Nidalee      |      11 |        9 |        22 |              0 |            0 |
| 30 | ARAM       |     992515 | 1621902822952 | True  | Renekton     |       6 |        7 |        15 |              0 |            0 |
| 31 | ARAM       |    2093742 | 1621897575216 | False | Elise        |       6 |       13 |        19 |              0 |            0 |
| 32 | ARAM       |    1318359 | 1621896053236 | False | Pantheon     |       6 |       14 |        23 |              0 |            0 |
| 33 | ARAM       |    1522684 | 1621799332618 | False | Zyra         |       0 |       11 |        28 |              0 |            0 |
| 34 | ARAM       |     649921 | 1621798507491 | False | Jayce        |       8 |        7 |        13 |              0 |            0 |
| 35 | CLASSIC    |    1365259 | 1621661179892 | True  | Bard         |       4 |        0 |         8 |             35 |            4 |
| 36 | CLASSIC    |    2732821 | 1621658016980 | False | Senna        |      12 |        7 |        19 |             99 |            6 |
| 37 | CLASSIC    |    1990527 | 1621655529768 | True  | Senna        |       7 |        6 |        18 |             75 |            5 |
| 38 | CLASSIC    |    1691796 | 1621653326744 | True  | Nami         |       2 |        4 |        14 |             56 |            5 |
| 39 | CLASSIC    |    1322561 | 1621651553857 | False | Senna        |       2 |        1 |         5 |             40 |            2 |
| 40 | CLASSIC    |    2120189 | 1621556847557 | True  | Nami         |       5 |        5 |        21 |             95 |           12 |
| 41 | CLASSIC    |    2245973 | 1621553916425 | True  | Rakan        |       1 |        6 |        16 |            106 |           11 |
| 42 | CLASSIC    |    1963138 | 1621476287268 | False | Senna        |       4 |        6 |         8 |             70 |            8 |
| 43 | CLASSIC    |    1748280 | 1621472727044 | True  | Rakan        |       3 |        8 |        17 |             60 |            7 |
| 44 | CLASSIC    |    1892894 | 1621459658554 | True  | Senna        |       3 |        3 |        23 |             76 |            6 |
| 45 | CLASSIC    |     915858 | 1621138470825 | False | Nami         |       2 |        3 |         3 |             18 |            2 |
| 46 | ARAM       |     941226 | 1621131784488 | True  | Lux          |      11 |        5 |        43 |              0 |            0 |
| 47 | ARAM       |    1574519 | 1621129934715 | True  | Nunu         |       6 |       14 |        45 |              0 |            0 |
| 48 | CLASSIC    |    2127529 | 1621056517385 | True  | Bard         |       4 |        9 |        11 |             86 |            8 |
| 49 | CLASSIC    |    1268998 | 1621054594885 | False | Rakan        |       5 |        4 |         5 |             26 |            5 |
| 50 | CLASSIC    |    1354959 | 1621052122761 | True  | Thresh       |       0 |        1 |        10 |             35 |            2 |
| 51 | CLASSIC    |    2081769 | 1621049074016 | True  | Senna        |       9 |        3 |         9 |             88 |            6 |
| 52 | CLASSIC    |    1922667 | 1621045868144 | True  | Senna        |       7 |        7 |        14 |             68 |            3 |
| 53 | CLASSIC    |    1199940 | 1621043916442 | True  | Senna        |       3 |        3 |        14 |             32 |            2 |
| 54 | ARAM       |    1087533 | 1621038957245 | True  | Pantheon     |       9 |        8 |        11 |              0 |            0 |
| 55 | CLASSIC    |    2465748 | 1620951461026 | True  | Rakan        |       1 |        6 |        26 |             96 |           12 |
| 56 | ARAM       |    1667090 | 1620948926773 | False | Diana        |       7 |       16 |        36 |              0 |            0 |
| 57 | ARAM       |    1230639 | 1620947376600 | False | Illaoi       |       9 |       11 |         9 |              0 |            0 |
| 58 | ARAM       |     874970 | 1620869776351 | True  | Vladimir     |       3 |        5 |        10 |              0 |            0 |
| 59 | ARAM       |     936912 | 1620868453948 | False | Darius       |       7 |        8 |         9 |              0 |            0 |
| 60 | ARAM       |    1342212 | 1620866891795 | False | Vi           |       7 |        7 |        14 |              0 |            0 |
| 61 | ARAM       |    1562799 | 1620865082110 | False | Swain        |       3 |       14 |        38 |              0 |            0 |
| 62 | ARAM       |     972965 | 1620785201535 | False | Karma        |       0 |        9 |        11 |              0 |            0 |
| 63 | ARAM       |     740741 | 1620784072943 | True  | Amumu        |       3 |        4 |        19 |              0 |            0 |
| 64 | ARAM       |     993244 | 1620782771064 | False | Urgot        |       1 |       11 |        12 |              0 |            0 |
| 65 | ARAM       |     975449 | 1620697642393 | False | Orianna      |       4 |        7 |        22 |              0 |            0 |
| 66 | ARAM       |    1753369 | 1620695575177 | False | Karma        |       2 |       11 |        32 |              0 |            0 |
| 67 | ARAM       |    1254730 | 1620442508077 | True  | Renekton     |       7 |        6 |        11 |              0 |            0 |
| 68 | ARAM       |    1213144 | 1620441075847 | True  | Karthus      |       5 |       12 |        38 |              0 |            0 |
| 69 | ARAM       |    1198235 | 1620439555339 | True  | Khazix       |      12 |        9 |         9 |              0 |            0 |
| 70 | ARAM       |    1336418 | 1620438051999 | True  | Diana        |      11 |       10 |        28 |              0 |            0 |
| 71 | ARAM       |    1366274 | 1620436400844 | True  | Corki        |      10 |        8 |        18 |              0 |            0 |
| 72 | ARAM       |    1052062 | 1620435128633 | True  | Annie        |       7 |        6 |        30 |              0 |            0 |
| 73 | ARAM       |    1187519 | 1620350881692 | False | Hecarim      |      11 |       14 |        27 |              0 |            0 |
| 74 | ARAM       |    1978447 | 1620348639649 | True  | Malzahar     |       8 |       10 |        21 |              0 |            0 |
| 75 | ARAM       |    1221794 | 1620347035810 | False | Kennen       |       4 |        8 |        16 |              0 |            0 |
| 76 | ARAM       |     993316 | 1618632978728 | True  | Elise        |      12 |        7 |        18 |              0 |            0 |
| 77 | ARAM       |    1017441 | 1618631702600 | False | FiddleSticks |       6 |       10 |        13 |              3 |            0 |
| 78 | CLASSIC    |    1979738 | 1618018186381 | False | Leona        |       2 |        5 |        16 |             72 |            6 |
| 79 | CLASSIC    |    2126664 | 1618015646079 | False | Lulu         |       2 |        4 |        12 |             73 |            4 |
| 80 | CLASSIC    |    1537111 | 1618013518218 | True  | Rakan        |       0 |        0 |        11 |             53 |            4 |
| 81 | ARAM       |    1172389 | 1617847167062 | False | Corki        |       8 |        9 |        19 |              0 |            0 |
| 82 | ARAM       |    2198994 | 1617844676508 | True  | Urgot        |      17 |       15 |        33 |              0 |            0 |
| 83 | ARAM       |    1016445 | 1617418640509 | False | Gangplank    |       5 |        6 |         4 |              0 |            0 |
| 84 | ARAM       |    1181265 | 1617414310052 | True  | Annie        |       5 |        8 |        20 |              0 |            0 |
| 85 | ARAM       |    1026207 | 1617412907914 | True  | Irelia       |      15 |        5 |         8 |              0 |            0 |
| 86 | ARAM       |    1759359 | 1617410939275 | False | Ziggs        |      12 |       10 |        28 |              0 |            0 |
