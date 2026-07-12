use osha_severe_injuries;


-- ************************************************
-- Naics join for industry analysis  
-- ================================================
-- The naics and severe injury tables are joined together to complete an analysis on industry names versus the codes. 
-- The naics table was referenced 4 times with a different alias (n6, n4, n3, and n2) for a different matching strategy to identify the industry.
-- The matching strategy is a hierarchy to match all 6 digits first, if nothing returned, the query moves to 4, then 3, then 2, until it reaches the 'unknown industry'
-- Searching by 5 digits would have created redundacy within the query and was not needed based ont the analysis completed in Microsoft Excel. 
-- The left join creats what can be considered "phantom columns" in the background.  The aliases (n6, n4, etc) label each "phantom columns" for the query to know which
-- match attempt it is referring to
-- The Coalesce function is what creates the heirarchy of the "how" to search and return values.  If the first match attempt did not find a match, then it moves to the next 
-- value to find a match, the hierarchy will continue on until it reaches the end and results in an "unknown industry". 
-- Industry name is an alias for the Coalesce function to name the column 
-- Left join was used to match every record, if possible.  The left join created what can be described as phantom columns. 
-- A standard join would have dropped records if a match was not found. 
-- Intersect and inner join were not good options for the same reason, the intersect and inner join would have looked for exact matches.  
-- Right join would not have worked for the desired outcome either.  The right join would keep every record from the second table (Naics), which would not have served 
-- the purpose desired for analysis.
-- ************************************************

/*
select 
    lj.id,
    lj.employer,
    lj.city,
    lj.state,
    lj.primarynaics,
    coalesce(
        n6.2022NaicsTitle,
        n4.2022NaicsTitle,
        n3.2022NaicsTitle,
        n2.2022NaicsTitle,
        'unknown industry'
    ) as industryname
from osha_severe_injuries.severe_injuries lj
left join osha_severe_injuries.naics n6 
    on lj.primarynaics = n6.2022NaicsCode
left join osha_severe_injuries.naics n4 
    on left(lj.primarynaics, 4) = n4.2022NaicsCode
left join osha_severe_injuries.naics n3 
    on left(lj.primarynaics, 3) = n3.2022NaicsCode
left join osha_severe_injuries.naics n2 
    on left(lj.primarynaics, 2) = n2.2022NaicsCode;
*/

-- ************************************************
-- how many matched and how many returned unknown industry 
-- ==================================================
-- The case expression provided a way to do a condition logic on the results from the coalesce statement.  The left join was also placed in this query since the 
-- "phantom columns" disappear once the query is run.
-- ************************************************

/*
select 
    case 
        when coalesce(n6.`2022NaicsTitle`, n4.`2022NaicsTitle`, n3.`2022NaicsTitle`, n2.`2022NaicsTitle`) is null 
        then 'unknown industry'
        else 'matched'
    end as match_status,
    count(*) as total
from osha_severe_injuries.severe_injuries lj
left join osha_severe_injuries.naics n6 
    on lj.primarynaics = n6.`2022NaicsCode`
left join osha_severe_injuries.naics n4 
    on left(lj.primarynaics, 4) = n4.`2022NaicsCode`
left join osha_severe_injuries.naics n3 
    on left(lj.primarynaics, 3) = n3.`2022NaicsCode`
left join osha_severe_injuries.naics n2 
    on left(lj.primarynaics, 2) = n2.`2022NaicsCode`
group by match_status;
*/

-- ************************************************
-- Industries with the most severe injuries 
-- ************************************************

/*
select 	
	coalesce(
		n6.`2022NaicsTitle`,
		n4.`2022NaicsTitle`,
		n3.`2022Naicstitle`,
		n2.`2022naicstitle`,
		'unknown industry'
	) as industryname,
	count(*) as totalreports,
	sum(lj.hospitalized) as hospitalizations,
	sum(lj.amputation) as amputations,
	sum(lj.lossofeye) as lossofeye
from osha_severe_injuries.severe_injuries lj
left join osha_severe_injuries.naics n6
	on lj.PrimaryNaics = n6.`2022NaicsCode` 
left join osha_severe_injuries.naics n4
	on left(lj.PrimaryNaics, 4) = n4.`2022NaicsCode` 
left join osha_severe_injuries.naics n3
	on left(lj.PrimaryNaics, 3) = n3.`2022NaicsCode` 
left join osha_severe_injuries.naics n2
	on left(lj.PrimaryNaics , 2) = n2.`2022NaicsCode` 
group by industryname 
order by totalreports desc;
*/

-- ************************************************
-- percentage rates by industry
-- ************************************************

/*
select 
    coalesce(
        n6.`2022NaicsTitle`,
        n4.`2022NaicsTitle`,
        n3.`2022NaicsTitle`,
        n2.`2022NaicsTitle`,
        'unknown industry'
    ) as industryname,
    count(*) as totalreports,
    round(sum(lj.hospitalized) / count(*) * 100, 2) as pcthospitalized,
    round(sum(lj.amputation) / count(*) * 100, 2) as pctamputation,
    round(sum(lj.lossofeye) / count(*) * 100, 2) as pctlossofeye
from osha_severe_injuries.severe_injuries lj
left join osha_severe_injuries.naics n6 
    on lj.primarynaics = n6.`2022NaicsCode`
left join osha_severe_injuries.naics n4 
    on left(lj.primarynaics, 4) = n4.`2022NaicsCode`
left join osha_severe_injuries.naics n3 
    on left(lj.primarynaics, 3) = n3.`2022NaicsCode`
left join osha_severe_injuries.naics n2 
    on left(lj.primarynaics, 2) = n2.`2022NaicsCode`
group by industryname
order by totalreports desc;
*/

