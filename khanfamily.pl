mianbiwi(chotekhan,chotirani).
mianbiwi(barrekhan,barrirani).
mianbiwi(salim,kauser).
mianbiwi(nadir,nahid).
mianbiwi(asad,sumra).
mianbiwi(rizwan,sanam).
parent(chotekhan,kauser).
parent(chotirani,kauser).
parent(chotekhan,nadir).
parent(chotirani,nadir).
parent(chotekhan,asad).
parent(chotirani,asad).
parent(barrekhan,nahid).
parent(barrirani,nahid).
parent(barrekhan,sumra).
parent(barrirani,sumra).
parent(salim,rizwan).
parent(kauser,rizwan).
parent(nadir,burhan).
parent(nahid,burhan).
parent(nadir,rashid).
parent(nahid,rashid).
parent(nadir,akram).
parent(nahid,akram).
parent(asad,salima).
parent(sumra,salima).
parent(asad,sanam).
parent(sumra,sanam).
parent(rizwan,rabia).
parent(sanam,rabia).
gins(mard,chotekhan).
gins(mard,barrekhan).
gins(mard,salim).
gins(mard,nadir).
gins(mard,asad).
gins(mard,rizwan).
gins(mard,burhan).
gins(mard,rashid).
gins(mard,akram).
gins(aurat,chotirani).
gins(aurat,barrirani).
gins(aurat,kauser).
gins(aurat,nahid).
gins(aurat,sumra).
gins(aurat,salima).
gins(aurat,sanam).
gins(aurat,rabia).
maa(X,Y):-  parent(X,Y),gins(aurat,X).
beti(X,Y):- parent(Y,X),gins(aurat,X).
beta(X,Y):- parent(Y,X),gins(mard,X).
dada(X,Y):- parent(Z,Y),parent(X,Z),gins(mard,X).
nana(X,Y):- parent(Z,Y),parent(X,Z),gins(aurat,Z),gins(mard,X).
dadi(X,Y):- parent(Z,Y),parent(X,Z),gins(aurat,X).
nani(X,Y):- parent(Z,Y),parent(X,Z),gins(aurat,Z),gins(aurat,X).
sala(X,Y):- mianbiwi(Y,Z),parent(A,X),parent(A,Z),gins(mard,X),gins(aurat,Z),gins(mard,A).
bahu(X,Y):- mianbiwi(Z,X),parent(Y,Z).
pota(X,Y):- parent(Y,Z),parent(Z,X),gins(mard,X).
nawasa(X,Y):- parent(Y,Z),parent(Z,X),gins(mard,X),gins(aurat,Z).
#behan(X,Y):-parent(Z,Y),parent(Z,X),gins(mard,Z),gins(aurat).
sussar(X,Y):- mianbiwi(Z,Y),parent(X,Z),gins(mard,X).
baapdada(X,Y):- parent(B,Y),parent(A,B),parent(X,A),gins(mard,X).
khala(X,Y):- parent(A,X),parent(A,Z),parent(Z,Y),gins(aurat,Z),gins(aurat,X),not(X=Z).
chachataya(X,Y):- parent(A,X),parent(A,Z),parent(Z,Y),gins(mard,Z),gins(mard,X),not(X=Z).