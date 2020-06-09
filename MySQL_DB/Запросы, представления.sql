
Представление:
Список всех закупок
create VIEW all_procedures AS select n.`number`, pt.`type` as 'Тип процедуры', s.`type` as "Имя площадки",
n.name as "Название", st.`type` as "Статус", c.name as "Заказчик", n.end_date, 
n.first_part_date, n.auction_date,n.second_parts_time,n.price,n.finance,icode, n.application_pledge, 
	n.contract_pledge, n.guarantee_pledge, rt.name as "Ограничения"  from notices as n
	join procedure_types as pt on n.procedure_type_id =pt.id
	join sites as s on n.site_id=s.id
	left join restricts as r on r.notice_id=n.id
	left join restricts_types as rt on r.restrict_types_id=rt.id
	join stages as st on st.id=n.stage_id
	join customers as c on c.id=n.customer_id;

Типичные запросы:
Список всех аукционов 
SELECT * FROM notices where procedure_type_id=1  ORDER BY end_date DESC ;
Список всех закупок для СМП
SELECT * FROM notices where id in ( SELECT notice_id from restricts where restrict_types_id=1);



Процедура определения общего количества процедур у заказчика и кол-ва закупок у СМП.

DROP PROCEDURE IF EXISTS total_procedures;
CREATE PROCEDURE total_procedures (IN val INT)
BEGIN
  	SELECT  COUNT(*) as total from notices where customer_id= val GROUP by customer_id
union
SELECT COUNT(*) FROM notices as n
	join restricts as r on n.id=r.notice_id where r.restrict_types_id = 1 and customer_id=val;
END;
