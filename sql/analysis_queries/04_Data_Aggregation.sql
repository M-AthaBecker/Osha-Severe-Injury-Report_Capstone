use osha_severe_injuries;

-- ================================================
-- data aggregation
-- ================================================

-- ================================================
-- data aggregation = incidents by report type 
-- ================================================

/*
select 
	si.EventTitle ,
	count(*) as TotalIncidentsReport
from 
	severe_injuries si 
group by 	
	eventtitle 
order by totalincidentsreport desc; 
*/

-- ================================================
-- data aggregation - count of body part impacted 
-- ================================================

/*
select 
	si.PartOfBodyTitle ,
	Count(*) as TotalBodyPartImpacted
from 
	severe_injuries si 
group by 
	si.PartOfBodyTitle 
order by totalbodypartimpacted desc;
*/

-- ================================================
-- data aggregation - Day of the week with most incidents 
-- ================================================

/*
select 
	DAYNAME(si.eventdate ) as DayOfWeek,
	Count(*) as Incidents
from 
	severe_injuries si 
group by 
	dayofweek 
order by
	Incidents desc;
*/

-- ================================================
-- data aggregation - Monthly Trend of Incidents between 1/1/2025 - 10/31/2025 
-- ================================================

/*
select 
	Date_format(si.eventdate , '%y-%m') as month,
	Count(*) as Incidents
from 	
	severe_injuries si 
where si.eventdate between '2025-01-01' and '2025-10-31'
group by `month` 
order by `month` ;
*/

-- ================================================
-- data aggregation - Monthly Trend of Incidents between 1/1/2025 - 10/31/2025 
-- ================================================

/*
select
	QUARTER(si.eventdate ) as Quarter,
	Count(*) as Incidents 
from
	severe_injuries si 
group by quarter 
order by quarter;
*/

-- ================================================
-- data aggregation - Correlation between hospitalization and amputation 
-- ================================================

/*
select 
	(count(*) * sum(Hospitalized * Amputation) - 
     sum(Hospitalized) * sum(Amputation)) /
    (sqrt(COUNT(*) * sum(Hospitalized * Hospitalized) - 
     sum(Hospitalized) * sum(Hospitalized)) *
     sqrt(COUNT(*) * sum(Amputation * Amputation) - 
     sum(Amputation) * sum(Amputation))) AS Correlation
from 
	severe_injuries si ;
*/


