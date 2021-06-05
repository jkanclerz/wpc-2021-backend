## Variables
BUCKET_NAME=${BUCKET_NAME}
FUNCTION_NAME=${FUNCTION_NAME}

## Zip archive
rm lambdaCode.zip || true
zip -r lambdaCode.zip ./* --exclude 'deploy.sh' --exclude 'lambdaCode.zip'

## copy to s3
aws s3 cp lambdaCode.zip s3://${BUCKET_NAME}/code/${FUNCTION_NAME}/lambdaCode.zip

## update function code
aws lambda update-function-code --function-name ${FUNCTION_NAME} --s3-bucket ${BUCKET_NAME} --s3-key code/${FUNCTION_NAME}/lambdaCode.zip --publish