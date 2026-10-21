def lum(h):
    h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def cr(a,b):
    la,lb=sorted([lum(a),lum(b)],reverse=True); return (la+0.05)/(lb+0.05)
P={'paper':'#E7E1D1','paper2':'#DCD5C2','paper3':'#F3EEDF','kraft':'#CFC6B4'}
F={'ink':'#121212','ink-soft':'#3A3835','red':'#D3261F','red-dark':'#A81914','blue':'#1D3FA8','blue-dark':'#142C7A'}
for pn,pv in P.items():
    print(pn, ' '.join(f"{fn}={cr(pv,fv):.2f}" for fn,fv in F.items()))
print('white/red',round(cr('#FFFFFF','#D3261F'),2),'paperink/red',round(cr('#F7F3E8','#D3261F'),2),'paperink/ink',round(cr('#F7F3E8','#121212'),2),'red/ink',round(cr('#D3261F','#121212'),2),'paperink/red-dark',round(cr('#F7F3E8','#A81914'),2))
