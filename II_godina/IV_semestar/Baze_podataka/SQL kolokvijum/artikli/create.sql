create table kupac (
    idkup integer not null,
    nazkup varchar(30) not null,
    mestkup varchar(30),
    constraint kupac_pk primary key (idkup),
    constraint kupac_uk unique (nazkup)
);

create table artikal (
    idart integer not null,
    nazart varchar(30),
    jcena integer,
    constraint artikal_pk primary key (idart),
    constraint artikal_mc check (jcena > 0)
);

create table faktura (
    brfak integer not null,
    datum date,
    idkup integer,
    constraint faktura_pk primary key (brfak),
    constraint faktura_fk_kup foreign key (idkup) references kupac (idkup)
);

create table stavka (
    brfak integer,
    rbrst integer not null,
    idart integer,
    kol integer,
    cena integer,
    constraint stavka_pk primary key (brfak, rbrst),
    constraint stavka_fk_ar foreign key (idart) references artikal (idart),
    constraint stavka_fk_fk foreign key (brfak) references faktura (brfak),
    constraint stavka_kol check (kol > 0)
);