/*
SELECT count(*) from Frequency
WHERE docid='10398_txt_earn';


SELECT count(term) from Frequency
WHERE docid='10398_txt_earn' AND count=1;


SELECT count(*) from (
SELECT term from Frequency
WHERE docid='10398_txt_earn' AND count=1
UNION
SELECT term from Frequency
WHERE docid='925_txt_trade' AND count=1
);


SELECT count(distinct docid) from Frequency
WHERE term='parliament';
*/

select count(docid) from (
SELECT docid from Frequency
GROUP by docid
HAVING sum(count) > 300
) x;


SELECT count(*) from (
SELECT f1.docid FROM Frequency f1, Frequency f2
WHERE f1.docid=f2.docid AND f1.term='transactions' AND f2.term='world'
) x;
