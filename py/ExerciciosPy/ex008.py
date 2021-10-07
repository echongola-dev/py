medida = float(input('Uma Distancia em metros: '))
mm = medida * 1000
cm = medida * 100
dam = medida * 10
dm = medida / 10
hm = medida / 100
km = medida / 1000

print(' A medida de {}m corresponde a {}mm, {}cm, {}dam, {}dm, {}hm e {}km.'.format(medida, mm, cm, dam, dm, hm, km))