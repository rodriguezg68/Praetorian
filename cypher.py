from string import maketrans

while True:
  input = raw_input()
  if int(input) >= 0 and int(input) <= 25:
    break

intab = "abcdefghijklmnopqrstuvwxyz"
array = []

for letter in intab:
  array.append(letter)

for count in range(int(input)):
  array.insert(25, array.pop(0))

outtab = ''.join(array)
split = outtab.split('"')
outtab = ' '.join(split)

trantab = maketrans(intab, outtab)

title = "Mpyza johsslunl"
message = "ZWXY, Zluhabz Wvwbsbzxbl Yvthubz (Aol Zluhal huk Wlvwsl vm Yvtl), aolzl hyl aol budhclypun hsslnphujlz vm Aol Wyhlavyphu Nbhyk, luaybzalk if Jhlzhy av wyvcpkl aolpy lspal zljbypaf zlycpjlz huk luzbyl aol zhmlaf vm aol nsvihs Yvthu Ltwpyl. Hz aol zhfpun nvlz, 'Hss Yvhkz Slhk av Yvtl', ovdlcly aol whao vm h Wyhlavyphu pz ulpaoly zayhpnoa uvy klalytpuhal. Aolyl hyl zlclyhs whaoz av qvpupun aol Wyhlavyphu Nbhyk, iba aol whao dlss-mvbuklk pu tlypa pz aol tvza ovuvyhisl. Pa pz mvy aopz ylhzvu aoha Jhlzhy ohz klcpzlk aopz zlyplz vm johsslunlz av qbknl aol tlypa vm wvaluaphs Wyhlavyphu yljybpaz. Fvb ohcl wyvclu fvbyzlsm ylzvbyjlmbs, iba kvu'a sla fvby nbhyk kvdu hz mhy tvyl kpmmpjbsa johsslunlz spl holhk. Av hjjlwa fvby ulea johsslunl, fvb dpss ullk av zluk tl h tlzzhnl vu Zrfwl. Av hkk tl hz h jvuahja, zluk h jvuahja ylxblza jvuahpupun aol alea 'Zluhabz Wvwbsbzxbl Yvthubz' av 'wyhlmljabz.jhzayvybt', aolu zluk tl h joha tlzzhnl av sla tl ruvd fvb'yl aolyl. Zll fvb vu aol ihaaslmplsk. - Wyhlmljabz Jhzayvybt"

print title.lower().translate(trantab)
print message.lower().translate(trantab)
