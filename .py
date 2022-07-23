OneOnethousand=list(range(300,400))     #kelimenin sonundaki sayı aralığını yazılır. ve değiştirilebilir.
a=10                                    #kaç kelime grubu yapacaksanız buradan a sayısını değiştiriniz.
for i in OneOnethousand:                #ekrana yazılacak kelimelerin sonundaki sayı 
    n=i%a                               #burada sayıyı modlayarak kaç sayılık grubların ayarlar
    if n==1:
        k=i
        print("")        
        for u in list(range(a)):      
            k=k+u
            print('""',',','#',k)
            k=k-u
        print("")
        print("**********************************************")
    print('""',',','#',i)

 
 """
***************************************
"sore throat",#91
"sore eye",#92
"quiet",#93
"sore hand",#94
"flu",#95
"medicine",#96
"living room",#97
"dining room",#98
"kitchen",#99
"basement",#100

"boğaz ağrısı",#91
"göz ağrısı",#92
"sessiz",#93
"el ağrısı",#94
"grip",#95
"ilaç",#96
"salon",#97
"yemek odası",#98
"mutfak",#99
"bodrum",#100


******************************************
"""
