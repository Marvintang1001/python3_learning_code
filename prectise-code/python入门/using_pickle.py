import pickle

shoplistfile='shoplist.data'
shoplist=['apple','banana','carrot']

f=open(shoplistfile,'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f=open(shoplistfile,'rb')
storelist=pickle.load(f)
print(storelist)
