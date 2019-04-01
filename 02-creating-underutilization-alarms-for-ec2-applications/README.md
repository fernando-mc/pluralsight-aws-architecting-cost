# Preparing your alarm Stressing your machine 

1. Create an Amazon Linux 2 EC2 instance
2. SSH into the instance
3. Download and run the `stress` tool:
    ```bash 
    # Get access to non-included extras tools
    sudo amazon-linux-extras install epel

    # Install the stress tool
    sudo yum install -y stress

    # Stress a single CPU core for 30 minutes
    stress --cpu 1 --timeout 30m
    ```
4. Create an alarm for CPU underutilization
5. Stop the stress testing
6. Confirm the alarm works as expected