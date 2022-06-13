
from audioop import reverse


redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
def tandembike():
    blueAndRed = redShirtSpeeds + blueShirtSpeeds
    list2 = sorted(blueAndRed)
    reverse(list2)
    list3 = list2[5] + list2[6] + list2[7] + list2[8] + list2[9]
    print(list3)
print(tandembike())