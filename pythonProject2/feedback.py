# class feedback:
#     def __init__(self,):
def main():
    user_name=input('Enter your name:')

    stakeholders_name=['a','b','c','d']

    if user_name in stakeholders_name:
        print('hello')
        user_id = input('Enter your id:')
        if user_id=='abc@123':
            user_project=int(input('Enter project id:'))
            project_id=[11,22,33,44,55,66]
            if user_project in project_id:
                print('access granted to give feedback')
            else:
                print('Enter valid project_id')
        else:
            print('Enter correct id')
    else:
        print('Enter valid name')
                # while True:
                #     project_name=input('Enter a project name:')
                #     print('ENTER\n 1:EXCELLENT\n 2:GOOD\n 3:AVERAGE \n 4')
main()

