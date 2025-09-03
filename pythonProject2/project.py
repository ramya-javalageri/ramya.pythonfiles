

# class Feedback:
#     def _init_(self,feedback_list):
#         self.feedback_list = []
#
#     def add_feedback(self,feedback):
#
#         self.feedback_list=[]
#         self.feedback_list.extend(feedback)
#         print(self.feedback_list)
#         print("Feedback added successfully!")
#
#     def view_feedback(self):
#
#         if not self.feedback_list:
#             print("No feedback available.")
#
#         else:
#             print("Feedback List:")
#             for i, feedback in enumerate(self.feedback_list, 1):
#                 print(f"{i}. {feedback}")
#
#     def update_feedback(self, index, updated_feedback):
#
#         if index < 1 or index > len(self.feedback_list):
#             print("Invalid index.")
#
#         else:
#             self.feedback_list[index - 1] = updated_feedback
#             # print(self.feedback_list)
#             print("Feedback updated successfully!")
#
#     def delete_feedback(self, index):
#
#         if index < 1 or index > len(self.feedback_list):
#             print("Invalid index.")
#
#         else:
#             del self.feedback_list[index - 1]
#             print(self.feedback_list)
#             print("Feedback deleted successfully!")
#
#
# def main():
#
#     feedback_manager = Feedback()
#
#     user_name = input('Enter your name:')
#
#     stakeholders_name = ['a', 'b', 'c', 'd']
#
#     if user_name in stakeholders_name:
#         print('hello ',user_name)
#         user_id = input('Enter your id:')
#
#         if user_id == 'abc@123':
#             user_project = int(input('Enter project id:'))
#
#             if user_project ==11:
#                 print('access granted to give feedback')
#
#                 while True:
#                     print("\n1. Add Feedback")
#                     print("2. View Feedback")
#                     print("3. Update Feedback")
#                     print("4. Delete Feedback")
#                     print("5. Exit")
#
#                     choice = input("Enter your choice: ")
#
#                     if choice == '1':
#
#                         print('please provide feedback for the following questions? ')
#                         #feedback=input("Enter your satisfaction rating (1-5):\n What do you like most \n What needs improvement? \n Any additional comments?\n" ).split(',')
#                         feedback_manager.add_feedback(feedback)
#
#                     elif choice == '2':
#
#                         feedback_manager.view_feedback()
#
#                     elif choice == '3':
#
#                         index = int(input("Enter index of feedback to update: "))
#                         updated_feedback = input("Enter updated feedback: ")
#                         feedback_manager.update_feedback(index, updated_feedback)
#
#                     elif choice == '4':
#
#                         index = int(input("Enter index of feedback to delete: "))
#                         feedback_manager.delete_feedback(index)
#
#                     elif choice == '5':
#
#                         print("Exiting program.")
#                         break
#
#                     elif choice=='0':
#                         main()
#
#                 else:
#                     print("Invalid choice. Please try again.")
#
#             else:
#                 print('Enter valid project_id')
#
#         else:
#             print('Enter correct id')
#
#     else:
#         print('Enter valid name')
#
# main()
#

class Feedback:
    def _init_(self,feedback_list):
        self.feedback_list = []

    def add_feedback(self,q1,q2,q3,q4):

        self.feedback_list=[]
        self.feedback_list.extend(q1)
        self.feedback_list.extend(q2)
        self.feedback_list.extend(q3)
        self.feedback_list.extend(q4)
        print(self.feedback_list)
        print("Feedback added successfully!")

    def view_feedback(self):

        if not self.feedback_list:
            print("No feedback available.")

        else:
            print("Feedback List:")
            for i, feedback in enumerate(self.feedback_list, 1):
                # print(i,'.',"['",feedback,"']")
                print(f"{i}. {feedback}")

    def update_feedback(self, index, updated_feedback):

        if index < 1 or index > len(self.feedback_list):
            print("Invalid index.")

        else:
            self.feedback_list[index - 1] = updated_feedback
            print(self.feedback_list)
            print("Feedback updated successfully!")

    def delete_feedback(self, index):

        if index < 1 or index > len(self.feedback_list):
            print("Invalid index.")

        else:
            del self.feedback_list[index - 1]
            print(self.feedback_list)
            print("Feedback deleted successfully!")


def main():

    feedback_manager = Feedback()

    user_name = input('Enter your name:')

    stakeholders_name = ['jack','virat','smirithi','shreyanka']

    if user_name in stakeholders_name:
        print('hello ',user_name)
        user_id = input('Enter your id:')

        if user_id == 'ectech@24':
            user_project = input('Enter project id:')

            if user_project =='bitm24':
                print('access granted to give feedback')

                while True:
                    print("\n1.Give Feedback")
                    print("2. View Feedback")
                    print("3. Update Feedback")
                    print("4. Delete Feedback")
                    print("5. Exit")

                    choice = input("Enter your choice: ")

                    if choice == '1':

                        print('please provide feedback for the following questions? ')
                        #feedback=input("Enter your satisfaction rating (1-5):\n What do you like most \n What needs improvement? \n Any additional comments?\n" ).split(',')
                        q1=input("Enter your satisfaction rating (1-5):").split(' ')
                        q2=input("What do you like most ").split(' ')
                        q3=input("What needs improvement?").split(' ')
                        q4=input(" Any additional comments?").split(' ')
                        feedback_manager.add_feedback(q1,q2,q3,q4)

                    elif choice == '2':

                        feedback_manager.view_feedback()

                    elif choice == '3':

                        index = int(input("Enter index of feedback to update: "))
                        updated_feedback = input("Enter updated feedback: ")
                        feedback_manager.update_feedback(index, updated_feedback)

                    elif choice == '4':

                        index = int(input("Enter index of feedback to delete: "))
                        feedback_manager.delete_feedback(index)

                    elif choice == '5':

                        print("Exiting program.")
                        break

                    elif choice=='0':
                        main()

                else:
                    print("Invalid choice,Please try again.")

            else:
                print('Enter valid project_id')

        else:
            print('Enter correct id')

    else:
        print('Enter valid name')

main()