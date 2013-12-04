import string


mapA = "abcdefghijklmnopqrstuvwxyz"
mapB = "cdefghijklmnopqrstuvwxyzab"
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "www.pythonchallenge.com/pc/def/map.html"
hint = "dmslb afypyarcpq rfyr maasppcb mljw mlc rgkc"

 
transText = string.maketrans(mapA, mapB)
transBack = string.maketrans(mapB, mapA)
#print text.translate(transText);
#print url.translate(transText);
#print hint.translate(transBack);
print hint.translate(transText);

