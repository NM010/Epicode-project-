SELECT NomeCantante
FROM CANTANTE
JOIN ESECUZIONE ON  CANTANTE.CodiceReg=ESECUZIONE.CodiceReg                    
JOIN AUTORE ON ESECUZIONE.TitoloCanz=AUTORE.TitoloCanzone    
WHERE Nome=NomeCantante AND Nome LIKE 'D%'; 


