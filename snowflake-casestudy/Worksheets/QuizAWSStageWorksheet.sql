CREATE OR REPLACE STAGE ms_s3_stage
  URL='<S3 bucket URL>'
  CREDENTIALS = (
    AWS_KEY_ID = '<AWS KEY>'
    AWS_SECRET_KEY = 'AWS Secret'
  )
  FILE_FORMAT = (
    TYPE = 'CSV'
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    SKIP_HEADER = 1
  );

LIST @ms_s3_stage;
