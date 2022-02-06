male(Kavish).
male(Pankaj).
male(Ramesh).
male(Sundeep).
male(Jayant).

female(Seema).
female(Sonali).
female(Sunita).
female(Esha).
female(Sanya).

father(Pankaj,Kavish).
father(Pankaj,Sonali).
father(Sundeep,Sanya).
father(Sundeep,Sanya).
father(Ramesh,Sundeep).
father(Ramesh,Seema).

mother(Sunita,Seema).
mother(Sunita,Sundeep).
mother(Seema,Sonali).
mother(Seema,Kavish).
mother(Esha,Sanya).
mother(Esha,Jayant).

wife(Seema,Pankaj).
wife(Esha,Sundeep).
wife(Sunita,Ramesh).


parent(Pankaj,Seema,Kavish).
parent(Pankaj,Seema,Sonali).
parent(Ramesh,Sunita,Sundeep).
parent(Ramesh,Sunita,Seema).
parent(Sundeep,Esha,Jayant).
parent(Sundeep,Esha,Sanya).


sister(X,Y) :- parent(A,B,X), parent(A,B,Y), female(X), X\==Y.
brother(X,Y) :- parent(A,B,X), parent(A,B,Y), male(X), X\==Y.
siblings(X,Y) :- parent(A,B,X), parent(A,B,Y), X\==Y.

husband(X,Y) :- wife(Y,X).

son(X,Y) :- father(Y,X);mother(Y,X), male(X).
daughter(X,Y) :- father(Y,X); mother(Y,X), female(X).
grandfather(X,Y) :- father(X,Z), father(Z,Y).
grandmother(X,Y) :- mother(X,Z), mother(Z,Y).
uncle(X,Y) :- brother(Z,X),father(Z,Y).
aunt(X,Y) :- husband(Z,X), uncle(Z,Y).
cousin(X,Y) :- uncle(Z,X),father(Z,Y).

