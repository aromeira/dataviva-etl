load data local infile 'H:/secex/Dados/Importacao/IMP_1998_MUN.csv'
into table SECEX_1998_IMP
character set 'latin1'
fields terminated by ';'
enclosed by '"'
lines terminated by '\n';