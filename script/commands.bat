docker build -t bezalelshteren/tweet-test:1.0 .

docker push bezalelshteren/tweet-test:1.0

oc create deployment tweet-test-deployment --image=docker.io/bezalelshteren/tweet-test:1.0

oc expose deployment tweet-test-deployment --port=8004 --name=tweet-test-service

oc expose svc/tweet-test-service --name=sqlserver-route

oc get route sqlserver-route
