drivers = LOAD 'drivers.csv' USING PigStorage(',');
drivers_raw = FILTER drivers BY $0>1;
driver_details = FOREACH drivers_raw GENERATE $0 AS driverId, $1 AS name;
timesheet = LOAD 'timesheet.csv' USING PigStorage(',');
raw_timesheet = FILTER timesheet by $0>1;
timesheet_log = FOREACH raw_timesheet GENERATE $0 AS driverId, $2 AS hours, $3 AS miles;
grouped_driver = GROUP timesheet_log BY driverId;
min_max = FOREACH grouped_driver GENERATE group AS driverId,
	MIN(timesheet_log.hours) AS min_hours,
	MAX(timesheet_log.hours) AS max_hours,
	MIN(timesheet_log.miles) AS min_miles,
	MAX(timesheet_log.miles) AS max_miles;
join_driver_driverstats = JOIN min_max BY driverId, driver_details BY driverId;
driver_stats = FOREACH join_driver_driverstats GENERATE $0 AS driverId, $6 AS name, $1 AS min_hours, $2 AS max_hours, $3 AS min_miles, $4 AS max_miles;
STORE driver_stats INTO 'driver_metrics';
