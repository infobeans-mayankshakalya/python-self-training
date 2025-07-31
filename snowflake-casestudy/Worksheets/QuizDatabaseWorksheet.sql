CREATE OR REPLACE DATABASE QUIZ_COLLECTION_DB;

USE DATABASE QUIZ_COLLECTION_DB;

CREATE OR REPLACE SEQUENCE que_id
START = 1
INCREMENT = 1;

CREATE OR REPLACE WAREHOUSE QUIZ_COLLECTION_WH;
-- ALTER WAREHOUSE QUIZ_COLLECTION_WH START;

-- Create example table 1
create or replace table quiz_questionnaire_temp(
  id int DEFAULT que_id.nextval, 
  question varchar,
  correct_answers varchar,
  explaination varchar,
  tech_domain varchar);

create or replace table quiz_questionnaire(
  id int DEFAULT que_id.nextval, 
  question varchar,
  correct_answers varchar,
  explaination varchar,
  tech_domain varchar);

-- Create a stream object
create or replace stream quiz_questionnaire_stream on table quiz_questionnaire_temp;


SHOW TASKS;
SHOW STREAMS;
DESC STREAM quiz_questionnaire_stream;


CREATE OR REPLACE TASK LOAD_FROM_S3_TO_TEMP
    WAREHOUSE = QUIZ_COLLECTION_WH
    SCHEDULE = 'USING CRON */10 * * * * UTC' -- EVERY 10TH MINUTE
AS
    COPY INTO quiz_questionnaire_temp
    FROM @ms_s3_stage
    FILE_FORMAT = (TYPE = 'CSV')
    ON_ERROR=CONTINUE;

ALTER TASK LOAD_FROM_S3_TO_TEMP RESUME;

SELECT * FROM quiz_questionnaire_temp;

select * from quiz_questionnaire_stream;

SELECT * FROM quiz_questionnaire;

SELECT * FROM QUIZ_COLLECTION_DB.INFORMATION_SCHEMA.LOAD_HISTORY;

-- TRUNCATE TABLE quiz_questionnaire;

SELECT * FROM quiz_questionnaire_temp;

-- Consume stream object
INSERT INTO quiz_questionnaire_temp 
    SELECT 
    que_id.nextval,
    qqs.question,
    qqs.correct_answers,
    qqs.explaination,
    qqs.tech_domain,
    FROM quiz_questionnaire_stream qqs;


-- Get changes on data using stream (INSERTS)

// Combine streams and tasks

CREATE OR REPLACE TASK quiz_questionnaire_task
    WAREHOUSE = COMPUTE_WH
    SCHEDULE = '1 MINUTE'
    WHEN SYSTEM$STREAM_HAS_DATA('QUIZ_QUESTIONNAIRE_STREAM')
    AS 
INSERT INTO quiz_questionnaire 
    SELECT 
    QS.id,
    QS.question,
    QS.correct_answers,
    QS.explaination,
    QS.tech_domain,
    FROM QUIZ_QUESTIONNAIRE_STREAM QS;

ALTER TASK quiz_questionnaire_task RESUME;


CREATE OR REPLACE VIEW top_domains_by_question_count AS
SELECT
  tech_domain,
  COUNT(*) AS question_count
FROM
  quiz_questionnaire
GROUP BY
  tech_domain
ORDER BY
  question_count DESC;

SELECT * From TOP_DOMAINS_BY_QUESTION_COUNT;