# st='I like chocolate and drink . my bro also like chocolate and drink .'
# dict_words={}
# for line in st:
#     words=line.split()
#     for word in words:
#         dict_words[word]=dict_words.get(word,0)+1
# list_words=[]
# for key,val in dict_words.items():
#     list_words.append((val,key))
#
# print(list_words)

class FeedbackSystem:
    def __init__(self):
        self.feedback_questions = []

    def create_question(self, question_text):
        question_id = len(self.feedback_questions) + 1
        question = {'id': question_id, 'text': question_text}
        self.feedback_questions.append(question)
        print(f"Question '{question_text}' created with ID {question_id}")

    def read_question(self, question_id):
        for question in self.feedback_questions:
            if question['id'] == question_id:
                print(f"Question ID: {question['id']}, Text: {question['text']}")
                return
        print("Question not found.")

    def update_question(self, question_id, new_text):
        for question in self.feedback_questions:
            if question['id'] == question_id:
                question['text'] = new_text
                print(f"Question ID {question_id} updated.")
                return
        print("Question not found.")

    def delete_question(self, question_id):
        for i, question in enumerate(self.feedback_questions):
            if question['id'] == question_id:
                del self.feedback_questions[i]
                print(f"Question ID {question_id} deleted.")
                return
        print("Question not found.")

    def collect_feedback(self):
        feedback_data = {}
        for question in self.feedback_questions:
            answer = input(f"Feedback for '{question['text']}': ")
            feedback_data[question['id']] = answer
        print("Feedback collected successfully.")
        return feedback_data

# Example usage
def main():

        feedback_system = FeedbackSystem()


        # Admin creates feedback questions
        feedback_system.create_question("How satisfied are you with the project progress?")
        feedback_system.create_question("Do you have any suggestions for improvement?")
        feedback_system.create_question("How much does the project is based on the real-life issues?")
        feedback_system.create_question("Whether all the team members are interactive?")

        # Admin collects feedback
        feedback_data = feedback_system.collect_feedback()
        print("Feedback Data:", feedback_data)

        # Admin updates a question
        feedback_system.update_question(2, "How can we improve our communication?")
        feedback_system.read_question(2)

        # Admin deletes a question
        feedback_system.delete_question(1)
        feedback_system.read_question(1)
