from matplotlib import pyplot as plt
from matplotlib_venn import venn3

A ={10,40,15,13}
B ={10,15,17,21}
C ={10,13,21,37}
U = {8, 10, 13, 15, 17, 21, 37}
resultado1 = set(((U-A)| B)& ((U-B)| C) & ((U-C)| A))

diagrama = venn3((1, 1, 1, 1, 1, 1, 1))
diagrama.get_label_by_id('100').set_color('blue')
diagrama.get_label_by_id('010').set_color('blue')
diagrama.get_label_by_id('001').set_color('blue')
diagrama.get_label_by_id('110').set_color('blue')
diagrama.get_label_by_id('011').set_color('blue')
diagrama.get_label_by_id('101').set_color('blue')
diagrama.get_label_by_id('111').set_color('black')


diagrama.get_label_by_id('100').set_text(A-(B | C))
diagrama.get_label_by_id('010').set_text(B-(A | C))
diagrama.get_label_by_id('001').set_text(C-(A | B))

diagrama.get_label_by_id('110').set_text((A & B)-C)
diagrama.get_label_by_id('101').set_text((A & C) - B)
diagrama.get_label_by_id('011').set_text((B & C) - A)
diagrama.get_label_by_id('111').set_text((B & C) & A)

texto = "8"
plt.suptitle(texto)

plt.show()
