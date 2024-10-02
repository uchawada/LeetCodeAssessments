CREATE PROCEDURE solution
AS
BEGIN

with person_request as
(
    select
    person_id,
    max(request) as max_request
    from requests
    group by person_id
),
first_request as
(
    select c.*,
    min(c.request_id) over (partition by c.seat_no) as first_request_id
    from
    (
        select a.*,b.max_request 
        from requests as a
        JOIN person_request as b on a.person_id = b.person_id
    ) as c
    where c.max_request = c.request
),
seat_reservation as
(
    select 
     a.seat_no,
     a.status,
     a.person_id as base_person_id,
     coalesce(b.max_request,0) as request,
     coalesce(b.person_id,0) as request_person_id,
     coalesce(b.request_id,0) as request_id
    from seats as a
    left join first_request as b 
    on a.seat_no = b.seat_no and b.first_request_id = b.request_id
),
base as
(
    select
    c.seat_no,
    case 
    when c.status = 0 and c.request > 0
    then c.request
    when c.status = 1 and c.base_person_id = c.request_person_id
    then c.request
    when c.status = 2
    then c.status
    else c.status 
    end as status,
    case 
    when c.status = 0 and c.request > 0
    then c.request_person_id
    when c.status = 1 and c.base_person_id = c.request_person_id
    then c.request_person_id
    when c.status = 2
    then c.base_person_id
    else c.base_person_id 
    end as person_id
    from seat_reservation as c
)
select * from base;

END

/*

You work for an airline, and you've been tasked with improving the procedure for reserving and buying seats.
You have the table seats, which describes seats in the airplane. It has the following columns:

seat_no - The unique number of the seat;
status - The status of the seat (0 indicates free, 1 indicates reserved, and 2 indicates purchased);
person_id - The ID of the person who reserved/purchased this seat (0 if the corresponding status is 0).
You also have the table requests, which contains the following columns:

request_id - The unique ID of the request;
request - The description of the request (1 indicates reserve, 2 indicates purchase);
seat_no - The number of the seat that the person want to reserve/purchase;
person_id - The ID of the person who wants to reserve/purchase this seat.
A person can reserve/purchase a free seat and can purchase a seat that they have reserved.

Your task is to return the table seats after the given requests have been performed.

Note: requests are applied from the lowest request_id; it's guaranteed that all values of seat_no in the table requests are presented in the table seats.

Example

For the given tables seats

seat_no	status	person_id
1	1	1
2	1	2
3	0	0
4	2	3
5	0	0
and requests

request_id	request	seat_no	person_id
1	1	3	4
2	2	2	5
3	2	1	1
the output should be

seat_no	status	person_id
1	2	1
2	1	2
3	1	4
4	2	3
5	0	0
*/