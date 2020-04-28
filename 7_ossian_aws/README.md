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
1. Find the public DNS of your instance by going to the AWS console > select services > select EC2 > click instances. The instance public DNS is located in the table under `Public DNS (IPv4)`.
2. Then run `ssh -i /path/to/key.pem ubuntu@<your_public_dns>`
3. Type in `yes` when prompted
You have now successfully `ssh`ed into the instance.

# Setup the necessary tools for Ossian
1. Install Python : `sudo apt-get install python`
2. Install pip:
    * `curl -O https://bootstrap.pypa.io/get-pip.py`
    * `python get-pip.py --user`
    * `export PATH=$PATH:~/.local/bin`
    * `pip --version`
3. Install other system packages:
    * `sudo apt-get update`
    * `sudo apt install python2.7-dev`
    * `sudo apt-get install build-essential autoconf libtool pkg-config python-opengl  python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev`
    * `sudo apt install sox`
4. Install Python requirements:
    * `pip install scipy --user
    * `pip install configobj --user
    * `pip install scikit-learn --user
    * `pip install regex --user
    * `pip install lxml --user
    * `pip install argparse --user
    * `pip install bandmat  --user
    * `pip install theano --user
    * `pip install matplotlib --user
    * `pip install soundfile --user
5. Clone the Ossian repository: `git clone -b rvk2019 https://github.com/CSTR-Edinburgh/Ossian.git`
6. Setup Ossian tools:
    * Create HTK credentials [http://htk.eng.cam.ac.uk/register.shtml](here) and then run:
        * `export HTK_USERNAME=<your_htk_username>`
        * `export HTK_PASSWORD=<your_htk_password>`
    * `cd Ossian`
    * `OSSIAN=$PWD`
    * `./scripts/setup_tools.sh $HTK_USERNAME $HTK_PASSWORD`
7. Verify that everything is working by running a toy example in romanian:
    * Get the data:
        * `cd $OSSIAN`
        * `wget https://www.dropbox.com/s/uaz1ue2dked8fan/romanian_toy_demo_corpus_for_ossian.tar?dl=0`
        * `tar xvf romanian_toy_demo_corpus_for_ossian.tar\?dl\=0`
    * Prepare the acoustic and duration models using Ossian: `python ./scripts/train.py -s rss_toy_demo -l rm naive_01_nn`
    * Train the duration model on CPU: `export THEANO_FLAGS=""; python ./tools/merlin/src/run_merlin.py $OSSIAN/train/rm/speakers/rss_toy_demo/naive_01_nn/processors/duration_predictor/config.cfg`
    * Train the acoustic model on CPU: `export THEANO_FLAGS=""; python ./tools/merlin/src/run_merlin.py $OSSIAN/train/rm/speakers/rss_toy_demo/naive_01_nn/processors/acoustic_predictor/config.cfg`
    * These steps take some time to finish and a lot of stuff should have been printed to the shell as a result. If everything is OK you should now be able to synthesize speech in Romanian. To do this:
        * `mkdir $OSSIAN/test/wav/`
        * `python ./scripts/speak.py -l rm -s rss_toy_demo -o ./test/wav/romanian_toy_HTS.wav naive_01_nn ./test/txt/romanian.txt`
        * Then copy the output via ssh to your machine: `scp -i ossian.pem ubuntu@<your_public_dns>:/home/ubuntu/Ossian/test/wav/romanian_toy_HTS.wav .`
        * You can now play the synthesized output on your machine`