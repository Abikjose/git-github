#!/usr/local/bin/python3.6
import boto3
iam = boto3.client('iam')

a = input("Please enter the username: ")
print("User: " + a)

if len(iam.list_groups_for_user(UserName = a)['Groups']) > 0:
    b = iam.list_groups_for_user(UserName = a)['Groups'][0]['GroupName']
    print ("The GroupName for the user {} is {}".format(a,b))
    print ("Removing user from Group......")

    iam.remove_user_from_group(GroupName = b, UserName=a)
    if iam.remove_user_from_group(GroupName = b, UserName=a)['ResponseMetadata']['HTTPStatusCode'] == 200:
        print ("The user has been removed from group {}".format(b))
    else:
        print ("Oops!!! something has gone wrong")
else: 
    print ("User is not in any group")

try:
    iam.delete_login_profile(UserName= a)
    print ("User profile has been removed")
except:
    pass
        


if len(iam.list_attached_user_policies(UserName=a)['AttachedPolicies'][0]['PolicyArn']) > 0:
    print ("User has policy attached")
    PolicyArn = []
    for i in iam.list_attached_user_policies(UserName=a)['AttachedPolicies']:
        Policy_Name.append(i['PolicyArn'])
        for j in Policy_Name:
            iam.detach_user_policy(UserName=a,PolicyArn=j)
            print("User's policies has been removed")
else: 
    print ("User has no policies attached")
    
try:
    iam.delete_user(UserName = a)
    print ("User has been removed")
except:
    pass
