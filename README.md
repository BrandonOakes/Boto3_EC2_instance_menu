# **Boto3 EC2 Menu**

### Creates custom session based on user's IAM credientials, allowing the user to review and start/stop their specified EC2 Instance.

#### *See requirements below before running the EC2 Menu script*

---
### **_Requirements_**

**1.** From the command line make sure you have Python 3

        python3 --version

Click this link <https://docs.brew.sh/Installation> if you need help downloading Python 3

**2.** Set up your virtual environment

        python3 -m venv myvenv

You can activate your virtual environment by running:

        source myvenv/bin/activate

Enter the command ```deactivate``` when you want to exit your virtual environment

**3.** Install **AWS CLI**:

 <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html>

 **4.** Now that you have the AWS CLI you will want to configure your device to store your user's IAM **AWS Access Key ID** and **Secret Access Key**. This Access Key and Secret Key are given to you as a download when you initially create you IAM user on AWS. Following the link below for more information concerning IAM set up.

  <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>

 Once you have your Access Key and Secret Key run the following:

        aws configure --profile <Your_IAM_User>

You will be given the following options, fill them out accordingly:

        AWS Access Key ID:
        AWS Secret Access Key:
        Default region name:
        Default output format:

**5.** Install script requirements (make sure your virtual environment is activated):

    pip3 install -r requirements.txt

**6.** Now run  ```python3 instance-ec2-aws.py``` and you are good to go.

### Disfrutar
