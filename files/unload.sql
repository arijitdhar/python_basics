 UNLOAD ( 'Select "card_id","company_id","card_type_id","card_name","description","mark_for_deletion","system_defined" from "poc_oms"."a_credit_card"') 
 to 's3://levi-cdh-redshift-data-export/Export/poc_oms_2019_12_31_14_13_57/a_credit_card/part_'
 iam_role 'arn:aws:iam::497531642140:role/knowme-qa-redshift' ALLOWOVERWRITE PARALLEL OFF DELIMITER '|' ESCAPE MAXFILESIZE 1024 MB  ;
--END--
 UNLOAD ( 'Select "id","name","address","phone" from "poc_oms"."poc_oms2"')
 to 's3://levi-cdh-redshift-data-export/Export/poc_oms_2019_12_31_14_13_57/poc_oms2/part_'
 iam_role 'arn:aws:iam::497531642140:role/knowme-qa-redshift' ALLOWOVERWRITE PARALLEL OFF DELIMITER '|' ESCAPE MAXFILESIZE 1024 MB  ;
--END--
 UNLOAD ( 'Select "itempk","itemtypepk","langpk","p_description","p_name","p_metadescription","p_metatitle","p_metah1","p_metaname" from "poc_oms"."categorieslp"')
 to 's3://levi-cdh-redshift-data-export/Export/poc_oms_2019_12_31_14_13_57/categorieslp/part_'
 iam_role 'arn:aws:iam::497531642140:role/knowme-qa-redshift' ALLOWOVERWRITE PARALLEL OFF DELIMITER '|' ESCAPE MAXFILESIZE 1024 MB  ;
--END--
 UNLOAD ( 'Select "customer_info_id","external_customer_id","company_id","first_name","last_name","phone_number","email","customer_type","ref_field1","ref_field2","ref_field3","ref_field4","ref_field5","ref_field6","ref_field7","ref_field8","ref_field9","ref_field10","ref_num1","ref_num2","ref_num3","ref_num4","ref_num5","created_source","created_source_type","created_dttm","last_updated_source","last_updated_source_type","last_updated_dttm","is_deleted","external_created_dttm","external_last_updated_dttm","anniversary_dttm","birthday_dttm","occupation","favorite_color","receive_email","receive_mail","denim_size","pant_size","dress_size","jacket_size","shoe_size","skirt_size","top_size","middle_name","tax_id" from "poc_oms"."a_customer_info"')
 to 's3://levi-cdh-redshift-data-export/Export/poc_oms_2019_12_31_14_13_57/a_customer_info/part_'
 iam_role 'arn:aws:iam::497531642140:role/knowme-qa-redshift' ALLOWOVERWRITE PARALLEL OFF DELIMITER '|' ESCAPE MAXFILESIZE 1024 MB  ;
--END--
 UNLOAD ( 'Select "id","name","address","phone" from "poc_oms"."poc_oms1"')
 to 's3://levi-cdh-redshift-data-export/Export/poc_oms_2019_12_31_14_13_57/poc_oms1/part_'
 iam_role 'arn:aws:iam::497531642140:role/knowme-qa-redshift' ALLOWOVERWRITE PARALLEL OFF DELIMITER '|' ESCAPE MAXFILESIZE 1024 MB  ;