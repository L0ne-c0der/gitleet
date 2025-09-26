# Write your MySQL query statement below
#quality = AVG(rating/position) So, create a column rating/position ?
#poor qual % = (no of things less than 3 / total ) * 100

select
query_name,
round(avg(cast(rating as decimal) / position), 2) as quality,
round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
from
queries
group by
query_name;