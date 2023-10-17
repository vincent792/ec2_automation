import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Define your user data scripts for VM2 and VM3 (as previously mentioned)

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
