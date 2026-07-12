use osha_severe_injuries

- **************************************
- data cleaning - date column
- added new column as a date 
- changed dates from a string to a date 
- **************************************

/*
alter table severe_injuries 
add column eventdate_clean date;
*/

/*
UPDATE severe_injuries
SET eventdate_clean = str_to_date(EventDate , '%m/%d/%Y');
/*

- **************************************
- data cleaning - date column
- confirming date range is correct per the dataset 
- **************************************

/*
select 
	min(si.eventdate_clean ) as earliestdate,
	max(si.eventdate_clean ) as latestdate
from severe_injuries si ;
*/

- **************************************
- data cleaning - date column
- dropping the eventdate column and renaming the eventdate_clean to eventdate 
- **************************************

/*
alter table severe_injuries 
drop column eventdate;
*/

/*
alter table severe_injuries 
rename column eventdate_clean to eventdate
*/

- **************************************
- data cleaning - removing leading and trailing spaces 
- **************************************

/*
update severe_injuries si 
set
	ID = trim(si.ID ),
	UPA = trim(si.UPA ),
	Employer = trim(si.Employer ),
	Address1 = trim(si.Address1 ),
	Address2 = trim(si.Address2 ),
	City = trim(si.City ), 
	State = trim(si.State ),
	Zip = trim(si.Zip ),
	latitude = trim(si.Latitude ),
	longitude = trim(si.Longitude ),
	PrimaryNaics = trim(si.PrimaryNaics ),
	Hospitalized = trim(si.Hospitalized ),
	Amputation = trim(si.Amputation ),
	LossOfEye = trim(si.LossOfEye ),
	Inspection = trim(si.Inspection ),
	FinalNarrative = trim(si.FinalNarrative ),
	Nature = trim(si.Nature ),
	NatureTitle = trim(si.NatureTitle ),
	PartOfBody = trim(si.PartOfBody  ),
	PartOfBodyTitle = trim(si.PartOfBodyTitle ),
	Event = trim(si.Event ),
	eventtitle = trim(si.EventTitle ),
	Source = trim(si.Source ),
	SourceTitle = trim(si.SourceTitle ),
	FederalState = trim(si.FederalState );
*/


	
	
