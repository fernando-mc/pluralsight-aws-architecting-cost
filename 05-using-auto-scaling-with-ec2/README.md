# Create a keypair

1. Navigate to the EC2 Console
2. Go to the "Network & Security" section on the left and click "Keypairs"
3. Create and download a keypair called demo5

# Creating an Launch Template
1. EC2 Console
2. Create Launch Template
    New template
    Launch tempalte name - LT_demo
    Source template - None
    AMI - Search for AMI --> Quickstart --> search for "Amazon Linux 2" 
        --> select the (x86) architecture
        --> In us-east-1 this is currently `ami-0de53d8956e8dcf80`
    Instance Type - t3a.nano
    Key pair name - demo5 (the one you just created)
    Network type - VPC
    Security Groups - Default security group (present on all new AWS accounts)

# Creating an Auto Scaling Group
1. EC2 Console
2. Auto Scaling section
3. Create Auto Scaling group
4. Select Launch Template and scroll down to select the LT_demo you just created
5. Next step:
    Group Name - ASG_demo
    Group size - 1
    Subnet - Add us-east-1a, us-east-1b
    Advanced Details
        Health check grace period - 60 seconds
6. Next - Configure Scaling Policies
    Option 2 - Use scaling policies to adjust the capacity of this group
    Scale between 1 and 2 instances
    Click - Scale the Auto Scaling group using step or simple scaling policies
        Increase Group Size
            Add new alarm
            Uncheck "Send a notification to"
            Rule details:
                Whenever `Average` of `CPU Utilization` is `>=` `80` percent for at least `1` consecutive period(s) of `1 Minute`
            Take action:
                `Add 1 instances` 
            And then wait:
                `60` seconds before allowing another scaling activity 
        Decrease Group Size
            Add new alarm
            Uncheck "Send a notification to"
            Whenever `Average` is `<=` `45`
            Rule details:
                Whenever `Average` of `CPU Utilization` is `<=` `45` percent for at least `1` consecutive period(s) of `1 Minute`
            Take action:
                `Remove 1 instances` 
            And then wait:
                `60` seconds before allowing another scaling activity 
        Launch the Auto Scaling group


# Connecting to and stressing your machine 

1. SSH into the instance that spins up in your Auto Scaling group
2. If the connection fails add a rule to the security group it lives inside of
    Allow SSH traffic from your IP
3. Download and run the `stress` tool:
    ```bash 
    # Get access to non-included extras tools
    sudo amazon-linux-extras install epel
    # Install the stress tool
    sudo yum install -y stress
    # Stress one of the t3a.nano's two CPU cores
    stress --cpu 1 --timeout 30m
    ```

4. Watch as the low utilization alarm is triggered and goes away
5. Then stop the previous command and stress both CPU cores: 
    ```bash
    # Stress both of the t3a.nano's CPU cores for 30 minutes
    stress --cpu 2 --timeout 30m
    ```
6. Watch as the high utilization command is triggered and requires a new instance to spin up
7. Stop the previous command
8. Watch as the instance is shut down