# Run an SPSS in the cloud using AWS
The repository for Ossian is [here](https://github.com/CSTR-Edinburgh/Ossian) and Merlin [here](https://github.com/CSTR-Edinburgh/merlin). Since these systems are quite complicated and computationally heavy we will be using AWS virtual machines.

# Setting up AWS
1. Create a free tier account [here](https://aws.amazon.com/). Note you will have to input credit card information. Don't worry about being charged since you will select the free tier account which gives you 750 compute hours for free for 12 months. When this course has finished you can delete your AWS account without any charges being made. If you want to be extra secure, visit the [billing preference page](https://console.aws.amazon.com/billing/home?#/preferences) and select to receive free tier usage alerts.
2. Sign in to the AWS console
3. Select `Launch a virtual machine` under the `Build a solution` row.
4. Select the `Ubuntu Server 18.04 LTS (HVM), SSD Volume Type` 64-bit (x86) variant.
5. Select the `t2.micro` instance type, press `review and launch` and then `launch`
6. When prompted, choose `reate a new key pair`, select any name and press `download key pair`. Move the key to some location where you are unlikely to delete it. Modify permissions (giving you sole read access) with e.g. `chmod 400 <key_name>.pem` on Linux.

# Connecting to the virtual machine
We will be using SSH to connect to the machine remotely. Make sure that your machine has an SSH client, otherwise install one. The following guide is a shorter version of this [AWS guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html).
1.