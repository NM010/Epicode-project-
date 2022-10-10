SELECT citta FROM AEROPORTO WHERE NumPiste IS NULL;
SELECT TipoAereo FROM VOLO WHERE CittaPart = "Torino";
SELECT CittaPart FROM VOLO WHERE CittaArr = "Bologna";
SELECT CittaPart, CittaArr FROM VOLO WHERE IdVolo = "AZ274";
SELECT TipoAereo, GiornoSett, OraPart FROM VOLO WHERE CittaPart like "B%o%" AND CittaArr like "%e%a";
