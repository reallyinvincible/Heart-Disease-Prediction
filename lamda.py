import json
import boto3

def lambda_handler(event, context):

    # The SageMaker runtime is what allows us to invoke the endpoint that we've created.
    runtime = boto3.Session().client('sagemaker-runtime')
    params = event['queryStringParameters']
    val = json.dumps(params)
    print("Params:", params)
    print("Val", val)
    response = runtime.invoke_endpoint(EndpointName = 'sagemaker-scikit-learn-2020-01-10-12-19-15-408',
                                      ContentType = 'text/plain',
                                      Body = val)
    print("Response", response)
    result = response['Body'].read().decode('utf-8')
    result = json.loads(result)
    print("New Result", result)
    params['prediction'] = result['prediction']
    print("New params", params)
    result = json.dumps(params)
    
    return {
        'statusCode' : 200,
        'headers' : { 'Content-Type' : 'text/plain', 'Access-Control-Allow-Origin' : '*' },
        'body' : result
    }
