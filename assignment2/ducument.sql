
SELECT d1.docid, d2.docid, sum(d1.count*d2.count)
FROM Frequency d1, Frequency d2
WHERE d1.term=d2.term AND d1.docid < d2.docid
GROUP BY d1.docid, d2.docid;

/*

SELECT docid1, docid2, max(sim) FROM
(
        SELECT d1.docid as docid1, d2.docid as docid2, sum(d1.count*d2.count) as sim
        FROM Frequency d1,
        (
                SELECT 'q' as docid, 'washington' as term, 1 as count
                UNION
                SELECT 'q' as docid, 'taxes' as term, 1 as count
                UNION
                SELECT 'q' as docid, 'treasury' as term, 1 as count
        ) d2
        WHERE d1.term=d2.term AND d1.docid < d2.docid
        GROUP BY d1.docid, d2.docid
);
*x/
