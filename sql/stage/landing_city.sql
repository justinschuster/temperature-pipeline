CREATE TABLE IF NOT EXISTS stage.landing_city
(
    city_id VARCHAR(256),
    lat NUMERIC(8, 6),
    long NUMERIC(9, 6),
    elev NUMERIC,
    utc_offset_seconds NUMERIC,
    timezone VARCHAR(256),
    timezon_abbrev VARCHAR(256),
    hourly_units VARCHAR(256)
);

ALTER TABLE stage.landing_city owner to TempPipeUser;