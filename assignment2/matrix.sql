SELECT a.row_num, b.col_num, sum(a.value*b.value) FROM a, b
WHERE a.col_num=b.row_num
GROUP BY a.row_num, b.col_num
ORDER BY a.row_num;
