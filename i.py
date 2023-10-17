import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Define your user data 
vm2_user_data = """
#!/bin/bash
# Install Docker and pull NGINX and MongoDB containers
# Run your NGINX and MongoDB containers here

yum update -y
yum install docker -y
systemctl start docker
docker run -p 8081:80 -d nginx
docker run -p 8082:80 -d nginx
docker run --name mongodb1 -d -p 27017:27017 mongo

"""

vm3_user_data = """
#!/bin/bash
# Install Docker and pull NGINX and MongoDB containers
# Run your NGINX and MongoDB containers here

yum update -y
yum install docker -y
systemctl start docker
docker run -p 8081:80 -d nginx
docker run -p 8082:80 -d nginx
docker run --name mongodb2 -d -p 27017:27017 mongo

"""
# Launch VM2
response_vm2 = ec2.run_instances(
    ImageId='ami-041feb57c611358bd',
    Name='VM2',
    InstanceType='t1.micro',
    
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=['sg-0194eebdc2e23d176']


)

# Launch VM3
response_vm3 = ec2.run_instances(
    ImageId='ami-041feb57c611358bd',
    Name='VM3',
    InstanceType='t1.micro',
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=['sg-0194eebdc2e23d176']
   
)

# Print the instance IDs or perform other operations as needed
print("VM2 Instance ID:", response_vm2['Instances'][0]['InstanceId'])
print("VM3 Instance ID:", response_vm3['Instances'][0]['InstanceId'])
