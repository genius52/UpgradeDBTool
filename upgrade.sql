use rt_tms;
alter table tmsaccessorychunk add column uid varchar(64);
alter table tmsaccessorychunk drop column accessoryuid;
alter table tmsaccessorychunk drop column commissionedunituid;
alter table tmsaccessorychunk drop column mu;
alter table tmsaccessorychunk add column mu_dx float;
alter table tmsaccessorychunk drop column mu_dr;
alter table tmsaccessorychunk drop column mu_da;
alter table tmsaccessorychunk drop column mu_dv;
alter table tmsaccessorychunk drop column hvl_slope;
alter table tmsaccessorychunk drop column density;
alter table tmsaccessorychunk add column datatype int;
alter table tmsaccessorychunk drop column mcphoparam1;
alter table tmsaccessorychunk drop column mcphoparam2;
alter table tmsaccessorychunk drop column mcphoparam3;
alter table tmsaccessorychunk drop column mcphoparam4;
alter table tmsaccessorychunk drop column mcphoparam5;
alter table tmsaccessorychunk drop column mcphoparam6;
alter table tmsaccessorychunk drop column mcphooffaxisvec;
alter table tmsaccessorychunk add column algorithmtype int;
alter table tmsaccessorychunk drop column crc;
alter table tmsaccessorychunk drop column updatetime;
alter table tmsaccessorychunk drop column primary;
alter table tmsaccessorychunk drop column ENGINE;
alter table tmsaccessorychunk drop column DEFAULT;
alter table tmsaccessorychunk drop column create;
alter table table2 drop column valueaa;
alter table table2 add column aaa float;
alter table table2 add column create table;
alter table oldtable add column asff int;
