from matplotlib import pyplot as plt
from matplotlib import patches as ptc
from matplotlib import colors as pcl


def make_rectangle(x, y, w, h, c='blue', f=True):
    return ptc.Rectangle((x - w / 2, y - h / 2), w, h, color=c, fill=f)


def make_hline(x, y, w, c='blue'):
    plt.hlines(y,
               x - w / 2,
               x + w / 2,
               colors=c,
               linestyle='dashed',
               linewidth=0.7)


fig = plt.figure()
ax = fig.add_subplot(111)

# c0,c2:color for isopin-0;c1:isospin-1;c3:color of text
# c0, c1, c2 = (1, 0, 0, 0.5), (0, 1, 0, 0.5), (0, 0, 1, 0.5)
# c00, c11, c22, c3 = (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), 'black'
c0, c1, c2 = (*pcl.to_rgb('red'), 0.7), (*pcl.to_rgb('green'),
                                         0.7), (*pcl.to_rgb('blue'), 0.7)
c00, c11, c22, c3 = (*pcl.to_rgb('red'), 1.0), (*pcl.to_rgb('green'),
                                                1.0), (*pcl.to_rgb('blue'),
                                                       1.0), 'black'
tf = False

# make_hline(100, 1712.5, 40, c=c00)
# make_hline(100, 1855, 40, c=c00)
# make_hline(200, 1718, 40, c=c11)
# make_hline(300, 1661, 40, c=c22)
make_hline(100, 1712.5, 40, c='black')
make_hline(100, 1855, 40, c='black')
make_hline(200, 1718, 40, c='black')
make_hline(300, 1661, 40, c='black')

r1 = make_rectangle(100, 1712.5, 40, 8.7 * 2, c=c0)
r2 = make_rectangle(100, 1855, 40, 9 * 2, c=c0)
r3 = make_rectangle(200, 1718, 40, 18 * 2, c=c1)
r4 = make_rectangle(300, 1661, 40, 13 * 2, c=c2)

ax.add_patch(r1)
ax.add_patch(r2)
ax.add_patch(r3)
ax.add_patch(r4)

plt.text(40, 1712.5 - 5, r'$\eta_1(1710)$', color=c00 if tf else c3)
plt.text(40, 1855 - 5, r'$\eta_1(1855)$', color=c00 if tf else c3)
plt.text(140 - 3, 1718 - 5, r'$K^*(1680)$', color=c11 if tf else c3)
plt.text(240, 1661 - 5, r'$\pi_1(1600)$', color=c22 if tf else c3)

plt.xlim([30, 330])
plt.ylim([1630, 1880])

plt.xticks([100, 200, 300], [r'$I=0$', r'$I=\frac{1}{2}$', r'$I=1$'],
           fontsize=14)
# plt.xlabel("Quantum Number", **{
#     'fontname': 'serif',
#     'weight': 'normal',
#     'size': 15
# })
plt.ylabel("Mass with uncertainty(MeV)", **{
    'fontname': 'serif',
    'weight': 'normal',
    'size': 14
})
# plt.show()
plt.savefig("./images/mass_specturm.png", format='png')
# plt.savefig("./images/mass_specturm.eps", format='eps')
# plt.savefig("./images/mass_specturm.pdf", format='pdf')
