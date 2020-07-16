__author__ = '220152'

def sentence_maker(phrase):
    interrogatives = ("how", "why", "when")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

end_string = "\end"
results = []

while True:
    user_input = input("Say something: ")
    if user_input == end_string:
        break;
    else:
        results.append(sentence_maker(user_input))
        continue;

final_result = " ".join(results)
print(final_result)




