use osha_severe_injuries;

- *******************************
- data exploration - total number of injury reports
- *******************************

/*
select COUNT(*) as totalreports
from severe_injuries si;
*/

- *******************************
- data exploration - Top highest 10 of employers reported
- *******************************

/*
select 
	si.Employer,
	COUNT(*) as top10employer
from 
	severe_injuries si 
group by si.Employer 
order by top10employer desc 
limit 10; 
*/

- *******************************
- data exploration - standardizing the employer names 
- adding a column for the clean data
- query to standardize the higher reporting employer names 
- *******************************

/*
alter table severe_injuries 
add column employer_clean varchar(500);
*/

/*
UPDATE severe_injuries
SET employer_clean =
    CASE
        when lower(Employer) like '%u.s. postal service%' then 'US Postal Service'
        when lower(Employer) like '%united states postal service%' then 'US Postal Service'
        when lower(Employer) like '%usps%' then 'US Postal Service'
        when lower(Employer) like '%ups%' then 'UPS'
        when lower(Employer) like '%united parcel service%' then 'UPS'
        when lower(Employer) like '%united parcel service, inc%' then 'UPS'
        when lower(Employer) like '%walmart%' then 'Walmart'
        when lower(Employer) like '%wal-mart%' then 'Walmart'
      	when lower(Employer) like '%walmart, inc%' then 'Walmart'
        when lower(Employer) like '%tyson%' then 'Tyson Foods'
        when lower(Employer) like '%publix%' then 'Publix Super Markets'
     	when lower(employer) like '%Cochran%' then '#1 Cochran'
        when lower(employer) like '%1 priority%' then '1 Priority Environmental Services'
        when lower(employer) like '%1888 Industrial%' then '1888 Industrial Services'
        when lower(employer) like '%1st Call%' then '1st Call Business Employment Service'
        when lower(employer) like '%FedEx%' then 'FedEx Freight'
        when lower(employer) like '%International Paper%' then 'International Paper'
        when lower(employer) like '%Home Depot%' then 'Home Depot'
        when lower(employer) like '%Lowe%' then 'Lowes Home Improvement'
        
        ELSE Employer
    END;
*/

/*
select 
	si.employer_clean ,
	COUNT(*) as top10employer
from 
	severe_injuries si 
group by si.employer_clean  ;
*/

- *******************************
- data exploration - Total Injuries by type 
- *******************************

/*
select 
	si.NatureTitle, 
	COUNT(*) AS InjuryType
from 
	severe_injuries si 
group by 
	si.NatureTitle
order by 
	InjuryType desc;
*/

- *******************************
- data exploration - standardizing the Injuries by Type
- adding a column for the clean data
- query to standardize the injury by type data 
- *******************************

/*
alter table severe_injuries 
add column naturetitle_clean varchar(500);
*/

update severe_injuries
set naturetitle_clean =
    case
        when lower(naturetitle) like '%fracture%' then 'fracture'
        when lower(naturetitle) like '%amputat%' then 'amputation'
        when lower(naturetitle) like '%cut%'
          or lower(naturetitle) like '%laceration%' then 'cut / laceration'
        when lower(naturetitle) like '%burn%' then 'burn'
        when lower(naturetitle) like '%crushing%' then 'crushing injury'
        when lower(naturetitle) like '%soreness%'
          or lower(naturetitle) like '%pain%' then 'soreness / pain'
        when lower(naturetitle) like '%internal%' then 'internal injury'
        when lower(naturetitle) like '%traumatic%' then 'traumatic injury'
        when lower(naturetitle) like '%eye%' then 'eye injury'
        when lower(naturetitle) like '%heat%' then 'heat injury'
        else lower(naturetitle)
    end;

- *******************************
- data exploration - Total Injuries by type using clean data
- *******************************

/*
select 
	si.NatureTitle_clean, 
	COUNT(*) AS InjuryType
from 
	severe_injuries si 
group by 
	si.NatureTitle_clean
order by 
	InjuryType desc;
*/

- *******************************
- data exploration - Total outcome type and percentage or total 
- *******************************

/*
select 
	sum(si.Hospitalized ) as TotalHospitalized,
	sum(si.Amputation ) as TotalAmputations,
	sum(si.LossOfEye ) as TotalLossOfEye,
	Count(*) as TotalReports,
	round(sum(si.Hospitalized ) / Count(*) * 100, 2) as PercentHospitalized,
	round(sum(si.Amputation ) / Count(*) * 100, 2) as PercentAmputation,
	round(sum(si.LossOfEye ) / Count(*) * 100, 2) as PercentLossOfEye
from 
	severe_injuries si 
*/

- *******************************
- data exploration - state with highest number of reports   
- *******************************

/*
select 
	si.State,
	count(*) as TotalReportsByState
from 
	severe_injuries si 
group by 
	si.State 
order by totalreportsbystate desc;
*/

- *******************************
- data exploration - earliest and latest reporting dates   
- *******************************

/*
select
	min(si.eventdate) as EarliestReportDate,
	max(si.eventdate) as LastReportDate
from 	
	severe_injuries si 
*/