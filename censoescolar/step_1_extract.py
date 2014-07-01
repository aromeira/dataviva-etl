import csv, sys, os, argparse, time, bz2
from collections import defaultdict
from os import environ
from config import DATA_DIR
import pandas as pd
from helpers import fixed_to_csv


#python -m censoescolar.step_1_extract
def main(year):
    dirFile = DATA_DIR + "censoescolar/" + year+"/"+'TS_MATRICULA_AC.txt'
    dirCSV = DATA_DIR + "censoescolar/" + year+"/"+'TS_MATRICULA_AC.txt.csv'
    
    #
    if year=='2013':
        headers = ('ANO_CENSO','PK_COD_MATRICULA','FK_COD_ALUNO','NUM_IDADE', 'TP_SEXO', \
                   'TP_COR_RACA', 'FK_COD_ESTADO_END', 'SIGLA_END', 'FK_COD_MUNICIPIO_END', 'ID_ZONA_RESIDENCIAL', \
                   'FK_COD_MOD_ENSINO', 'FK_COD_ETAPA_ENSINO', 'PK_COD_TURMA', 'FK_COD_CURSO_PROF', 'PK_COD_ENTIDADE', \
                   'FK_COD_ESTADO_ESCOLA', 'SIGLA_ESCOLA', 'COD_MUNICIPIO_ESCOLA', 'ID_LOCALIZACAO_ESC', 'ID_DEPENDENCIA_ADM_ESC')
                      
        #Coluna começa com 0
        columns = ((0,5),(5,18),(18,32),(48,52),(70,71), \
                   (71,72),(91,94),(94,96),(96,105),(105,106), \
                   (145,148),(148,152),(152,153),(163,171),(177,186), \
                   (186,189),(189,191),(191,200),(209,210),(210,211))
    
    
    elif year=='2012':
        headers = ('ANO_CENSO','PK_COD_MATRICULA','FK_COD_ALUNO','NUM_IDADE', 'TP_SEXO', \
                   'TP_COR_RACA', 'FK_COD_ESTADO_END', 'SIGLA_END', 'FK_COD_MUNICIPIO_END', 'ID_ZONA_RESIDENCIAL', \
                   'FK_COD_MOD_ENSINO', 'FK_COD_ETAPA_ENSINO', 'PK_COD_TURMA', 'FK_COD_CURSO_PROF', 'PK_COD_ENTIDADE', \
                   'FK_COD_ESTADO_ESCOLA', 'SIGLA_ESCOLA', 'COD_MUNICIPIO_ESCOLA', 'ID_LOCALIZACAO_ESC', 'ID_DEPENDENCIA_ADM_ESC')
                      
        #Coluna começa com 0
        columns = ((0,5),(5,18),(18,32),(43,47),(65,66), \
                   (66,67),(86,89),(89,91),(91,100),(100,101), \
                   (129,132),(132,136),(136,147),(147,156),(161,170), \
                   (170,173),(173,175),(175,184),(184,193),(193,194))
    
    
    
    
    
    
    elif year=='2011':
        headers = ('ANO_CENSO','PK_COD_MATRICULA','FK_COD_ALUNO','NUM_IDADE', 'TP_SEXO', \
                   'TP_COR_RACA', 'FK_COD_ESTADO_END', 'SIGLA_END', 'FK_COD_MUNICIPIO_END', 'ID_ZONA_RESIDENCIAL', \
                   'FK_COD_MOD_ENSINO', 'FK_COD_ETAPA_ENSINO', 'PK_COD_TURMA', 'FK_COD_CURSO_PROF', 'PK_COD_ENTIDADE', \
                   'FK_COD_ESTADO_ESCOLA', 'SIGLA_ESCOLA', 'COD_MUNICIPIO_ESCOLA', 'ID_LOCALIZACAO_ESC', 'ID_DEPENDENCIA_ADM_ESC')
                      
        #Coluna começa com 0
        columns = ((0,5),(5,18),(18,32),(43,48),(57,58), \
                   (58,59),(77,80),(80,82),(82,90),(90,91), \
                   (108,111),(111,115),(115,126),(126,134),(140,149), \
                   (149,152),(152,154),(154,162),(170,171),(171,172))
    
    elif year=='2010':
        headers = ('ANO_CENSO','PK_COD_MATRICULA','FK_COD_ALUNO','NUM_IDADE', 'TP_SEXO', \
                   'TP_COR_RACA', 'FK_COD_ESTADO_END', 'SIGLA_END', 'FK_COD_MUNICIPIO_END', 'ID_ZONA_RESIDENCIAL', \
                   'FK_COD_MOD_ENSINO', 'FK_COD_ETAPA_ENSINO', 'PK_COD_TURMA', 'FK_COD_CURSO_PROF', 'PK_COD_ENTIDADE', \
                   'FK_COD_ESTADO_ESCOLA', 'SIGLA_ESCOLA', 'COD_MUNICIPIO_ESCOLA', 'ID_LOCALIZACAO_ESC', 'ID_DEPENDENCIA_ADM_ESC')
                      
        #Coluna começa com 0
        columns = ((0,5),(5,18),(18,32),(43,48),(48,49), \
                   (49,50),(68,71),(71,73),(73,81),(81,82), \
                   (99,102),(102,106),(106,117),(117,126),(131,140), \
                   (140,143),(143,145),(145,153),(153,154),(154,155))
    
    elif year=='2009':
        headers = ('ANO_CENSO','PK_COD_MATRICULA','FK_COD_ALUNO','NUM_IDADE', 'TP_SEXO', \
                   'TP_COR_RACA', 'FK_COD_ESTADO_END', 'SIGLA_END', 'FK_COD_MUNICIPIO_END', 'ID_ZONA_RESIDENCIAL', \
                   'FK_COD_MOD_ENSINO', 'FK_COD_ETAPA_ENSINO', 'PK_COD_TURMA', 'FK_COD_CURSO_PROF', 'PK_COD_ENTIDADE', \
                   'FK_COD_ESTADO_ESCOLA', 'SIGLA_ESCOLA', 'COD_MUNICIPIO_ESCOLA', 'ID_LOCALIZACAO_ESC', 'ID_DEPENDENCIA_ADM_ESC')
                      
        #Coluna começa com 0
        columns = ((0,5),(5,18),(18,32),(43,48),(48,49), \
                   (49,50),(68,71),(71,73),(73,81),(81,82), \
                   (99,102),(102,106),(106,117),(117,126),(131,140), \
                   (140,143),(143,145),(145,153),(153,154),(154,155))

    elif year=='2008':
        headers = ('ANO_CENSO','PK_COD_MATRICULA','FK_COD_ALUNO','NUM_IDADE', 'TP_SEXO', \
                   'TP_COR_RACA', 'FK_COD_ESTADO_END', 'SIGLA_END', 'FK_COD_MUNICIPIO_END', 'ID_ZONA_RESIDENCIAL', \
                   'FK_COD_MOD_ENSINO', 'FK_COD_ETAPA_ENSINO', 'PK_COD_TURMA', 'FK_COD_CURSO_PROF', 'PK_COD_ENTIDADE', \
                   'FK_COD_ESTADO_ESCOLA', 'SIGLA_ESCOLA', 'COD_MUNICIPIO_ESCOLA', 'ID_LOCALIZACAO_ESC', 'ID_DEPENDENCIA_ADM_ESC')
                      
        #Coluna começa com 0
        columns = ((0,8),(8,24),(24,40),(60,68),(68,69), \
                   (69,70),(102,108),(108,110),(110,126),(126,127), \
                   (143,149),(149,155),(169,179),(197,209),(197,209), \
                   (209,215),(215,217),(217,233),(233,234),(234,235))

    elif year=='2007':
        headers = ('ANO_CENSO','PK_COD_MATRICULA','FK_COD_ALUNO','NUM_IDADE', 'TP_SEXO', \
                   'TP_COR_RACA', 'FK_COD_ESTADO_END', 'SIGLA_END', 'FK_COD_MUNICIPIO_END', 'ID_ZONA_RESIDENCIAL', \
                   'FK_COD_MOD_ENSINO', 'FK_COD_ETAPA_ENSINO', 'PK_COD_TURMA', 'FK_COD_CURSO_PROF', 'PK_COD_ENTIDADE', \
                   'FK_COD_ESTADO_ESCOLA', 'SIGLA_ESCOLA', 'COD_MUNICIPIO_ESCOLA', 'ID_LOCALIZACAO_ESC', 'ID_DEPENDENCIA_ADM_ESC')
                      
        #Coluna começa com 0
        columns = ((0,4),(4,16),(16,29),(37,40),(40,41), \
                   (41,42),(57,59),(59,61),(61,68),(68,69), \
                   (86,87),(87,90),(90,100),(100,108),(111,119), \
                   (119,121),(121,123),(123,130),(130,131),(131,132))

    
    
    
    
    fixed_to_csv(dirFile,columns,dirCSV,headers)
    
    
def slices(s, *args):
    position = 0
    for length in args:
        yield s[position:position + length]
        position += length
        
if __name__ == "__main__":
    start = time.time()
    YEAR="2013"
    main(YEAR)
    
    total_run_time = (time.time() - start) / 60
    print; print;
    print "Total runtime: {0} minutes".format(int(total_run_time))
    print; print;