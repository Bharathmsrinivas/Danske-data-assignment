
##3.1 

select 
c.customer_id, 
c.country, 
count(a.agreement_id) as active_agreements,
sum(a.monthly_payment) as total_monthly_exposure
from customers as c
left join agreements as a
on c.customer_id = a.customer_id

where c.segment in ('CORPORATE')
and a.status = 'ACTIVE'
and a.currency = 'EUR'

group by c.customer_id, c.country
having count(a.agreement_id) >= 2
order by total_monthly_exposure desc;

##3.2

select 
a.asset_type,
round(((sum(case when is_late then 1 else 0 end) / count(p.payment_id))*100 ),2) as late_payment_rate


from agreements as a
left join payemnts as p
on a.agreement_id = p.agreement_id
group by a.asset_type
having count(p.payment_id) > 100


##3.3

select 

c.customer_id,
c.segment,
max(p.payment_date) as last_payment_date

from customers as c
left join agreements as a
on c.customer_id = a.customer_id
left join payments as p
on a.agreement_id = p.agreement_id 

where a.status = 'ACTIVE'
group by c.customer_id,c.segment
having max(p.payment_date) is null or max(p.payment_date) < current_date - interval '90' day

##3.4

1.The Original query is a corelated subquery and it is not efficient because it needs to execute the subquery for each row in the agreements table.

SELECT *
FROM agreements a
WHERE (SELECT COUNT(*) 
       FROM payments p 
       WHERE p.agreement_id = a.agreement_id) > 5
  AND UPPER(a.status) = 'ACTIVE'
  AND YEAR(a.start_date) = 2023;

  The functions Upper and Year are applied to the columns in the where clause, which can prevent the database from using indexes and can lead to slower performance.

  The optimized query is rewritten using a join.

select a.*
from agreements a
join (
    select agreement_id, count(*) as payment_count
    from payments
    group by agreement_id
    having count(*) > 5
) p 
on a.agreement_id = p.agreement_id
where (a.status) = 'ACTIVE'
and a.start_date >= '2023-01-01' and a.start_date <= '2023-12-31';      