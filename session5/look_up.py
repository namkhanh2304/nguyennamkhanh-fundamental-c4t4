teen_code = {
   "hc": "hoc",
   "ng" :"nguoi",
   "pt" :"biet",
   "eny" :"em nguoi yeu",
  "any" : "anh nguoi yeu",
    "ns":"noi",
    "ngta":"nguoi ta",
   "lm": "lam",
   "r" :"roi",
   "stt": "status"
}

loop = True
while loop:
    for key in teen_code.keys():
        print(key, end="\t")

    print()

    code= input("your code?")

    if code in teen_code:
        print("traslation:", teen_code[code])
    else:
        add=input("add anything?(Y/N)").lower
        if add == "y":
            trans = input("your trans:")
            teen_code[code]= trans
        else:
            break
       
