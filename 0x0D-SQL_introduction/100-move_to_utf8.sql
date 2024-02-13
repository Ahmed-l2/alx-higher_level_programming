-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
use hbtn_0c_0;
alter database hbtn_0c_0 character set utf8mb4 collate utf8mb4_unicode_ci;
alter table first_table convert to character set utf8mb4 COLLATE utf8mb4_unicode_ci;
